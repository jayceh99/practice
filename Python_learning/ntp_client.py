from unicodedata import name
import requests
import os
import time
from datetime import datetime
import pyautogui

class  run ():
    def __init__(self,ip):
        self.server_ip = ip
    def get_sleep_time(self):
        
        realtime = requests.get('http://'+self.server_ip+'/ntp').text

        realtime = realtime.split(';')

        time_1 = datetime.strptime(realtime[0],"%H:%M:%S")
        time_2 = datetime.strptime(realtime[1],"%H:%M:%S")

        sleep_time = time_2 - time_1
        #sleep_time1 = time_1 - time_2
        sleep_time = str(sleep_time)
        h,m,s = sleep_time.split(":")
        self.sleep_time = int(h)*3600 + int(m)*60 +int(s) 
        #print (sleep_time)
    def mouse_control(self):
        time.sleep(self.sleep_time)
        pyautogui.moveTo(1084, 145, duration=1)
        pyautogui.click()

    def take_mouse(self):
        mouse = pyautogui.position()
        print (mouse)
     #   pyautogui.moveTo(1084, 145, duration=1)
     #   pyautogui.click()
def loop (run_q):
    run_q.get_sleep_time()
    run_q.mouse_control()
    #run_q.take_mouse()
def main ():
    ip = '127.0.0.1'
    run_q = run (ip)
    loop(run_q)


if __name__ == '__main__':
	main()