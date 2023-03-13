# -*- coding: utf-8 -*-
from socket import *
HOST='127.0.0.1'
PORT=50007
Buffsize = 1024
s=socket(AF_INET,SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
    #这两个函数都可以读取用户的输入，不同的是input（）函数要求用户输入有效的表达式（会自动转数据类型），而raw_input()函数将用户输入的任意类型数据都转换为一个字符串。
    cmd = input("Please input cmd:")       #与人交互，输入命令
    #eval_r(input())  在Python 3中，将raw_input()重命名为 input()，这样一来，无需导入也可从标准输入获得数据。
    #如需要保留2.X版本的 input() 功能， 可以使用 eval_r(input())， 效果基本相同。
        ###s.sendall(cmd)      #把命令发送给对端
        ###data=s.recv(1024)     #把接收的数据定义为变量
        ###print(data)   #输出变量
    if not cmd:
        continue
    s.send(cmd.encode("utf-8"))
    data = s.recv(Buffsize)
    if not data:
        continue
    print(data.decode("utf-8"))
s.close()   #关闭连接