from flask import Flask,request
import time

app = Flask(__name__)
@app.route("/ntp",methods=['GET'])
def ntp():
    start_time = '23:43:23'
    realtime = time.strftime("%H:%M:%S;" + start_time, time.localtime()) 

    return realtime

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True,threaded=True)