import ctypes
from time import sleep
player = ctypes.windll.kernel32

print \
    ("sss")
if __name__ == '__main__':
    from  urllib import request,parse
    url='http://www.maiziedu.com/user/login/'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        'Origin':'http://www.maiziedu.com',
        'Referer':'http://www.maiziedu.com/',
        'X-Requested-With':'XMLHttpRequest'
    }
    values={
        'account_l':'your account',
        'password_l':'your password'
    }
    postdata=parse.urlencode(values).encode(encoding='utf-8')
     
    req=request.Request(url,headers=headers,data=postdata)
     
    resp=request.urlopen(req)
    print(resp.read().decode('utf-8'))

Fsrkl = [392,392,440,392,523,494,    
              392,392,440,392,587,523,    
              392,392,784,659,523,494,440,    
              689,689,659,523,587,523,494]

Dsrkl = [375,125,500,500,500,1000,    
              375,125,500,500,500,1000,    
              375,125,500,500,500,500,1000,    
              375,125,500,500,500,500,2000]

for x in range(0,len(Fsrkl) - 1,1):
    print(x)
    #sleep(1)
    player.Beep(Fsrkl[x],Dsrkl[x])

print ((-5 + 4j) * (2.3 - 4.6j)) 