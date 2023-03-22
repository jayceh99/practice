import time
import datetime
import requests
from lxml import etree , html


class hot_blood ():
    def __init__(self) :
        self.headers = {
                "Authorization": "Bearer " + "tokkkkkkkkkken",
                "Content-Type": "application/x-www-form-urlencoded"} 

    def line_notify(self,message): 
        
        params = {'message':message}

        r = requests.post("https://notify-api.line.me/api/notify",headers=self.headers, params=params)

        return r.status_code

    def get_blood(self):
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
        
        tmp = ''
        for i in range (0,7):
            if addr[i] != '':
                tmp  = tmp + day_stack[i]+'\n'+addr[i]+'\n'
        if tmp == '':
            tmp = '這週\n'+day_stack[0]+'~'+day_stack[6]+'\n沒有捐血車'
        return tmp

def monitor ():
    ip = 'iiiiiip'
    seconds_since_epoch = time.time()
    seconds_since_epoch = seconds_since_epoch * 1000000000
    seconds_since_epoch  = format(seconds_since_epoch , '.0f')
    data =  "BloodNotify,host=180 Live=1  %s" % (seconds_since_epoch)
    url = 'http://'+ip+':8086/write?consistency=any&db=telegraf' 
    response = requests.post(url, data,headers={'Connection':'close'},timeout = 5)

def check_time():
    pass
def main ():
    f = open('time.txt','r')
    time_q = f.read()
    if float(time_q) < time.time():
        hot_blood_q =hot_blood()
        hot_blood_q.line_notify(hot_blood_q.get_blood())
        monitor()
    else:
        monitor()
#    test()
if __name__ == '__main__':
    main()