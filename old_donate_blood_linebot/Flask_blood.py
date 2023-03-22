from distutils.log import info
import requests
from flask import Flask
import time
import datetime
from selenium import webdriver
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


def get_blood():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("headless")
    chrome = webdriver.Chrome(r'./chromedriver', chrome_options=options)
    chrome.get("https://www.tp.blood.org.tw/Internet/taipei/LocationWeek.aspx?site_id=2")
    time.sleep(2)
    x = chrome.find_element_by_id('CalendarContentWeek')
    week = ['','星期日','星期一','星期二','星期三','星期四','星期五','星期六']
    tmp = '\n'
    x = str(x.text).split('星期')
    for i in range (0,len(x)):
        x[i] = x[i].split('\n')
    for j in range (1,8):
        for i in range (0,len(x[j])):
            if '林口區' in x[j][int(i)]:
                tmp = tmp+week[j]+':  '+x[j][int(i)]+'\n'
    if tmp == '\n':
        tmp = '這週沒有捐血車~'
    return tmp
    
app = Flask(__name__)
@app.route("/now",methods=['GET'])
def now_info():
    now_info = get_blood()
    return now_info
@app.route("/update" , methods=['GET'])
def test():
    nowtime = datetime.datetime.now() + relativedelta(months=3)
    unixtime = time.mktime(nowtime.timetuple())
    f = open('time.txt','w')
    f.write(str(unixtime))
    f.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=61000,debug=True,threaded=True)
