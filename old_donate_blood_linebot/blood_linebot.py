import os, sys
import re
import time
from flask import Flask, request, abort, jsonify
import requests
from datetime import datetime,timezone,timedelta

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)



# Channel Access Token
line_bot_api = LineBotApi('kkkkkkey')
# Channel Secret
handler = WebhookHandler('kkkkkkey')

# 監聽所有來自 /callback 的 Post Request
@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text
    

    if input_text == '1':
        req = requests.get('http://iiiiip:61000/update')
        req = req.text
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='捐血時間已更新'))

    elif input_text == '2':
        req = requests.get('http://iiiiip:61000/now')
        req =req.text
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=req))
        
    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入要執行的動作\n更新捐血時間請輸入 1\n查詢當週捐血地點請輸入 2'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)