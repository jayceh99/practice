import time
import os
import re
import requests
import xml.etree.ElementTree as XET
class network_traffic():
    def __init__(self) :
        self.pattern = re.compile(r'(?<=Counter32: )\d+\.*')
    def inOctets(self):

        network_in = os.popen('snmpwalk -v 2c -c public iiiiip 1.3.6.1.2.1.2.2.1.10.15')
        now_in = self.pattern.findall(network_in.read())
        now_time = time.time()
        try:
            traffic_in = int(now_in[0]) - self.now_1_in 
            traffic_time = int(now_time) - self.now_1_time
            traffic_in = (int(now_in[0]) - self.now_1_in) / traffic_time
            print (traffic_time)
        except AttributeError as e:
            print (str(e))
            self.now_1_in = int(now_in[0])
            self.now_1_time = int (now_time)
            print (self.now_1_in)
        self.now_1_in = int(now_in[0])
        self.now_1_time = int (now_time)
        


    def outOctets(self):
        network_out = os.popen = ('snmpwalk -v 2c -c public iiiiip 1.3.6.1.2.1.2.2.1.16.15')

def main():
    now_1_time = 0
    now_1_in = 0
    now_1_out = 0
    while True:
        try:
            pattern = re.compile(r'(?<=Counter32: )\d+\.*')
            network_in = os.popen('snmpwalk -v 2c -c public iiiiip 1.3.6.1.2.1.2.2.1.10.16')
            network_out = os.popen('snmpwalk -v 2c -c public iiiiip 1.3.6.1.2.1.2.2.1.16.16')
            now_in = pattern.findall(network_in.read())
            now_out = pattern.findall(network_out.read())
            now_time = time.time()
            traffic_time = int(now_time) - now_1_time
            traffic_in = (int(now_in[0]) - now_1_in) / traffic_time
    
    
            traffic_out = (int(now_out[0]) - now_1_out) / traffic_time
    
            now_1_in = int(now_in[0])
            now_1_out = int(now_out[0])
            now_1_time = int (now_time)
    
            print (traffic_in,traffic_out)
            
    
    
    
    
            ip = 'iiiiip'
            seconds_since_epoch = time.time()
            seconds_since_epoch = seconds_since_epoch * 1000000000
            seconds_since_epoch  = format(seconds_since_epoch , '.0f')
            data =  "network_traffic,host=180 In=%s,Out=%s %s" % (traffic_in,traffic_out,seconds_since_epoch)
            url = 'http://'+ip+':8086/write?consistency=any&db=telegraf'
            response = requests.post(url, data,headers={'Connection':'close'},timeout = 5)
            print (response)
            time.sleep(10)
    

if __name__ == '__main__':
    main()
        
