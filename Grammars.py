# print absolute value of an integer:
# -*- coding: UTF-8 -*-       只能放在所有代码的开始的第一行第一列
import urllib
import urllib.request
import sys

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
a = 0xa5b4c3d2
if a >= 0:
    print(a)
else:
    print(- a)
print(0xFFFFFFFF / 1024 / 1024 / 1024)

print('\n\n\r')
number = 12.3e10
print(number)

print(2 ** (10))

print(eval(repr('AB')) == 'A')

print(repr(20000022222))


a = 'FF'
print(int(a,16) + 1)
#/*python2中而对于,input(),它希望能够读取一个合法的,python表达式,即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个SyntaxError*/
#number1 = input("please input number 1:")
#print(number1 * 10)
#print(int(input("please input number 2:")) * 10)

#python2已经被合并到input函数了
#number2 = raw_input("please input number 2:")
#print(number2 * 10)
print(r'\n\r')
print('c:\\python')
print('c:\npython')
#print 'c:\npython\\' 有些版本错误 print 'c:\npython' + '\\'

#python区分大小写 \n \N
print(r'''AAAAA 这个区分大小写\n       \N
            BBBBBB
            CCCCCC''')
print(u'我们的大家')
print(u'\u4e25')

us = u'严'
print(us.encode('gbk'))
print(us.encode('gb2312'))
print(us.encode('gb18030'))
#help()
# 获得系统默认编码格式
sysCharType = sys.getfilesystemencoding()
print(sysCharType)
# 获取页面
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}  
req = urllib.request.Request(r"http://www.baidu.com/", headers=headers)  


html = urllib.request.urlopen(req).read()

sysHtml = html.decode(sysCharType).encode('utf-8')
utf8String = bytes.decode(sysHtml)
#print(sysHtml)
print(type(sysHtml))
with open("baidu.html", 'wb+') as f:
    f.write(sysHtml)


s = '百度一下，你就知道'

#if sysHtml.find(s) != -1:
#    print('未经转化 字符匹配')
#else:
#    print('未经转化 字符不匹配')
if utf8String.find(s) != -1:
    print('经过转化 字符匹配')
else:
    print('经过转化 字符不匹配')