# -*- coding: UTF-8 -*- 
#coding=utf-8 
      
from __future__ import division
print('10 / 3 =', 10 / 3)
print('10.0 / 3 =', 10.0 / 3)
print('10 // 3 =', 10 // 3)

# -*- coding: UTF-8 -*- 只能放在所有代码的开始的第一行第一列
#coding=utf-8
#encoding:utf-8
# u + 'XXX'打印unicode字符
print(u'hello world s的速度')

      

print('hello', 'word')
print('200 + 300 = ', 200 + 300)
print(u'你好世界')
'xxx' is unicode
u'xxx' is unicode
'xxx' is str
b'xxx' is str
#!/usr/bin/env python
name = raw_input('please input name :')

print(name)

if (name == "1"):
    print("1")
else:
    print("2")


name = input("name:")
age = input("age:")
job = input("job:")
print('''
    Infomation of %s
             name:%s
              age:%s
              job:%s
    ''' % (name,name,age,job))
name = raw_input("请输入你的名字:".decode('utf-8').encode('gbk'))
name.encode('gb18030')
print(u'你的名字是：' + name)