# -*- coding: utf-8 -*-

import threading
import time

count = 0
#lock = threading.Lock()


class Counter(threading.Thread):
    def __init__(self, name):
        self.thread_name = name
        #self.lock = threading.Lock()#这是一个简单的Python语法问题,但在逻辑复杂时有可能被忽略,要保证锁对于多个子线程(进程)来说是共用的,即不要在Thread的子类内部创建锁
        super(Counter, self).__init__(name=name)

    def run(self):
        global count
        #global lock
        for i in range(100000):
            #lock.acquire()     #事实上每次运行结果都不相同且不正确,这证明单核CPU+PIL仍无法保证线程安全,需要加锁.
            count = count + 1
            #lock.release()


counters = [Counter('thread:%s' % i) for i in range(5)]

for counter in counters:
    counter.start()

time.sleep(1)
print ('count=%s' % count)