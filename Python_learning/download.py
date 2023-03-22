import requests
import time
class download ():
    def __init__(self,name,url) :
        self.file_name = name
        self.url = url


    def downloadfile(self):
        headers = {'Proxy-Connection': 'keep-alive'}
        r = requests.get(self.url,stream=True,headers=headers)
        length = float(r.headers['Content-length'])
        f = open(self.file_name,'wb')
        count = 0
        count_tmp = 0

        time1 = time.time()
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk) 
                count += len(chunk)
                if time.time() - time1 > 1:
                    self.p = count / length * 100
                    self.speed = (count - count_tmp) / 1024 / 1024 / 1
                    count_tmp = count
                    print(self.file_name + ': ' + '{:.2f}'.format(self.p) + '%' + ' Speed: ' +  '{:.2f}'.format(self.speed)  + 'M/S')
                    time1 = time.time()
        f.close()



def loop (download_q):
    download_q.downloadfile()
def main ():
    name = 'python.exe'
    url = 'https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe'
    download_q = download(name,url)
    loop (download_q)
if __name__ == '__main__':
    main()