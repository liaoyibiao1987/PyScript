#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('包含中文的str')
print(ord("中"))

print(chr(25991))
print('\u4e2d\u6587')

print(b'ABC'.decode('ascii') + b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('中文'.encode('utf-8') + 'ABC'.encode('ascii'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len('中文') ,len('中文'.encode('utf-8')) , len(b'\xe4\xb8\xad\xe6\x96\x87')) 


#参数化输入
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('i am %s my hobby is %s' % ('lhf','alex'))
print('i am %s my hobby is %s' % ('lhf',[1,2]))
print("percent %.2f %%" % 99.976234444444444444) 

print('i am %(name)+60s my hobby is alex' % {'name':'lhf'})
print('i am \033[43;1m%(name)+60s\033[0m my hobby is alex' % {'name':'lhf'})

print("i am {0}, age {1}, really {0}".format("seven", 18))
 
## ** 代表传字典 * 代表传列表
print("i am {}, age {}, {}".format(*["seven", 18, 'alex']))
print("i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18}))
print("i am {0[0]}, age {0[1]}, really {0[2]}, hi {1[2]}".format([1, 2, 3], [11, 22, 33]))
print("i am {0:s}, age {1:d}, money {2:f}".format("seven", 18, 88888.1))## s 代表字符串 d 代表整数
print("i am {:s}, age {:d}".format(*["seven", 18]))## * 代表列表

##2进制 8进制 10进制 x与X: 16进制 %：百分比
print("numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2))
print("numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%} ,{0:*^30} ,{0:#x},{0:,.2%},{0:$^30,.2%}".format(15))
print('{:+f}; {:+f}'.format(3.14, -3.14))

import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))
#d = dict(who='tim')
#Template('Give $who $100').substitute(d)

width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
        #print("i am {0}, age {1}, money {2}".format(num, base, width))
        #print("i am {0}, age {1}, money {2}".format(num, base=base, width=width))
    print() #打印换行
print("====================使用list和tuple、dic==========================")
list_test = ['Michael', 'Bob', 'Tracy']
list_test.append(3)
list_test.insert(3,4)
list_test.copy()
print(list_test)

tuple_test = ("A" , "B" , "C")              #tuple一旦初始化就不能修改
print(tuple_test)

dic_test = {"AAAA":23 , "BBB":43}
print(dic_test["AAAA"])

print("=========================逻辑运算符=========================")
#condition1 = True
#condition2 = False
#if(condition1 and condition2):
#    print("成功")
#elif(condition1 or condition2):
#    print("失败")

#if(not condition2):
#    print("not condition2")

#LuckyNum = 6
#while True:
#  InLuckyNum = int(input('please your lucky number:'))
#  if InLuckyNum == LuckyNum:
#      print('bingo ')
#      break
#  elif InLuckyNum < LuckyNum:
#     print('please input big')
#  else:
#      print('please input small')
0
#for letter in 'Python': # 第一个实例
#   print( '当前字母 :', letter)
#fruits = ['banana', 'apple', 'mango']
#for fruit in fruits: # 第二个实例
#   print ('当前字母 :', fruit)
#print("Good bye!")
locknumber = 20
for i in range(3):
    input_number = int(input("请输入一个数字"))
    if input_number == locknumber:
        print("真幸运")
        break
    elif input_number < locknumber:
        print("数字太小")
    else:
        print("数字太大")