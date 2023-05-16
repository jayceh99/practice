import time
import datetime
import json
import requests
class notify ():
    def __init__(self,token) :
        self.headers = {
                "Authorization": "Bearer " + ""+token+"",
                "Content-Type": "application/x-www-form-urlencoded"} 
    def line_notify(self): 
        
        params = {'message':'\ntest\n123~'}

        r = requests.post("https://notify-api.line.me/api/notify",headers=self.headers, params=params)

        return r.status_code

def main ():
    f = open('config.json')
    tmp = f.read()
    f.close()
    p = json.loads(tmp)
    token = (p['token'])
    hot_blood_q =notify(token)
    hot_blood_q.line_notify()


if __name__ == '__main__':
    main()