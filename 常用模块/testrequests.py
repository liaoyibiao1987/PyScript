import requests

def TestGet():
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    r = requests.get('https://www.baidu.com/',headers)
    #print(r.text)
    print(r.status_code)
    print(r.encoding)
    #print(r.content)
    print(r.headers)
    print(r.headers['Content-Type'])


def TestPost():
    upload_files = {'file': open('常用模块/test.jpg', 'rb')}
    cs = {'token': '12345', 'status': 'working'}
    r2 = requests.post('https://www.baidu.com/', files=upload_files,cookies=cs)
    print(r2.status_code)
    print(r2.encoding)
    #print(r.content)
    print(r2.headers)
    print(r2.headers['Content-Type'])

if __name__ == '__main__':
   TestPost()

    