import time
import serial
import threading
import struct
import array

#def ss:
#    now_time = datetime.now()
#    yesterday = now_time + timedelta(days=-1)
#    tomorrow = now_time + timedelta(days=+1)
#    tomorrow = tomorrow.strftime('%Y-%m-%d')
#    print (yesterday)
#    print (tomorrow)
class Test:
    def __init(self):pass
    def f(self):
        print('Hello, World!')

class ComThread:
    def __init__(self, Port='COM10'):
    #构造串口的属性
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.ID = None
        self.data = None
   #定义串口等待的函数
    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()
    #启动串口的函数
    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = 19200
        #设置等待时间，若超出这停止等待
        self.l_serial.timeout = 2
        self.l_serial.open()
        #判断串口是否已经打开
        if self.l_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.runinng,args = ("a"))
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            return False
    def runinng(self,xxx): 
        while(True):
           time.sleep(0.1)
           b_com = self.l_serial.read_until('FE')
           #str = struct.pack("ii", 20, 400)
           #print(struct.unpack("ii", str))
           print(struct.unpack(len(b_com)*'c',b_com))
           print(' '.join([ "%02X" % x for x in b_com ]).strip())
           #print(''.join(map(lambda x:('/x' if len(hex(x))>=4 else '/x0')+hex(x)[2:],a)))
           #print(struct.unpack('ii',b_com))
           #for y in b_com:
           #     print(y)

if __name__ == '__main__':
    #Test().f()
    #hex_string = "deadbeef"
    #print(array.array('B', hex_string))
    ComThread().start()