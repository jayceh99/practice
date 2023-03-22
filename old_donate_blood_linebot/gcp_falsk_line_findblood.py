from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import requests
import os
from tabnanny import check
import time
import datetime
from dateutil.relativedelta import relativedelta
from lxml import etree , html
app = Flask(__name__)

line_bot_api = LineBotApi('long tokeeeeeeen')
handler = WebhookHandler('tokeeeeeeen')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #line_bot_api.reply_message(
    #    event.reply_token,
    #    TextSendMessage(text=event.message.text))
    input_text = event.message.text


    if input_text == '更新':
        nowtime = datetime.datetime.now() + relativedelta(months=3)
        unixtime = time.mktime(nowtime.timetuple())
        f = open('time.txt','w')
        f.write(str(unixtime))
        f.close()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='捐血時間已更新'))

    elif input_text == '2':
        day_stack,addr = fineblood()
        tmp = ''
        for i in range (0,7):
            if addr[i] != '':
                tmp  = tmp + day_stack[i]+'\n'+addr[i]+'\n'
        if tmp == '':
            tmp = '這週\n'+day_stack[0]+'~'+day_stack[6]+'\n沒有捐血車'


        req =tmp
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=req))

    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入要執行的動作\n更新捐血時間請輸入 更新\n查詢當週捐血地點請輸入 2'))



def fineblood():
    r = requests.get('https://www.tp.blood.org.tw/Internet/taipei/LocationWeek.aspx?site_id=2')

    data = html.fromstring(r.content)



    day = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr[2]/td[1]/text()')
    day_stack = [0]*7
    addr = [0]*7


    for i in range(1,8):
        tmp = ''
        day = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr['+str(i)+']/td[1]/text()')
        day = str(day).replace('\\r\\n','').replace(' ','').replace('[\'','').replace('\']','')
        day_stack[i-1] = day
        #print (day)
        count = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr['+str(i)+']/td[2]/table/tr')
        for  j in range(1,len(count)+1):
                k = data.xpath('/html/body/div[2]/div/form/div/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/table/tr['+str(i)+']/td[2]/table/tr['+str(j)+']/td/span/text()')
                if '林口區' in str(k) :
                    k = str(k).replace('[\'','').replace('\']','')
                    tmp = tmp + k +'\n'
        addr[i-1] = tmp
                #print (k)
    # print(tmp)
    
    return day_stack , addr
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 62000))
    app.run(host='0.0.0.0', port=port)
    #app.run()