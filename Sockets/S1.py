﻿# -*- coding: utf-8 -*-
from socket import *
from time import *
#import commands   #执行系统命令模块

endings = ["st","nd","rd"] + 17 * ["th"]\
           +["st","nd","rd"] + 3 * ["th"]\
           +["st"]
#updsocket = socket(AF_INET,SOCK_DGRAM)
HOST = '127.0.0.1'
PORT = 50007
BuffSize = 1024

s = socket(AF_INET,SOCK_STREAM)   #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))   #套接字绑定的IP与端口
s.listen(1)         #开始TCP监听
while True:
       conn,addr = s.accept()   #接受TCP连接，并返回新的套接字与IP地址
       print('Connected by',addr)    #输出客户端的IP地址
       while 1:
            #data = conn.recv(1024)    #把接收的数据实例化
            #cmd_status,cmd_result = commands.getstatusoutput(data)   #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
            #if len(cmd_result.strip()) == 0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
            #    conn.sendall('Done.')
            #else:
            #    conn.sendall(cmd_result)   #否则就把结果发给对端（即客户端）
        data = conn.recv(BuffSize)
        if not data:
            break
        conn.send(b'[%s] %s' % (bytes(ctime(),"utf-8"),data))
conn.close()     #关闭连接