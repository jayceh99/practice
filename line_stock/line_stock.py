from urllib import request
import time
import requests
import json


class line_stock :
    def __init__(self,stock_num) :
        self.stock_num = stock_num


    def request_info(self):
        url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_'+self.stock_num+'.tw&json=1&delay=0'
        r = requests.get(url)
        self.info = json.loads(r.text)
        return self.info
    def info_name(self):
        info_name = self.info['msgArray'][0]['n']
        #print (info_name)
        return info_name
    def info_buy(self):
        info_buy = self.info['msgArray'][0]['a'].split('_')
        return info_buy[0]
    def info_sell(self):
        info_sell = self.info['msgArray'][0]['b'].split('_')
        return info_sell[0]


def main():
    f = open('stock_num.txt','r')
    stock_num = f.read().split('\n')
    
    for num in stock_num :
        line_stock_q = line_stock(num)
        line_stock_q.request_info()
        print (line_stock_q.info_name(),'\nBuy '+line_stock_q.info_buy()+'\nSell '+line_stock_q.info_sell()+'\n')    

if __name__ == '__main__':
    main()
#####