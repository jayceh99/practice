import socket
import time
import requests

def socket_check():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('iiiip',61000))
    if result == 0:
        monitor(1)
    else:
        monitor(10)
    sock.close()
def monitor (live):
    ip = 'iiiip'
    seconds_since_epoch = time.time()
    seconds_since_epoch = seconds_since_epoch * 1000000000
    seconds_since_epoch  = format(seconds_since_epoch , '.0f')
    data =  "Flask_blood,host=180 Live=%s  %s" % (live,seconds_since_epoch)
    url = 'http://'+ip+':8086/write?consistency=any&db=telegraf' 
    response = requests.post(url, data,headers={'Connection':'close'},timeout = 5)

if __name__ == "__main__":
    socket_check()