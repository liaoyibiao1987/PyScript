#import random
#import time
#import queue
#from multiprocessing import freeze_support
#from multiprocessing.managers import BaseManager

## 从BaseManager继承的QueueManager:
#class QueueManager(BaseManager):
#    pass

#class Ask_Master:
#    def __init__(self):
#        # 绑定端口5000, 设置验证码'abc': manager这种属性不能用双下划线
#        self.manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')        
#        # 发送任务的队列:
#        self._task_queue = queue.Queue()
#        # 接收结果的队列:
#        self._result_queue = queue.Queue()
#    #@property
#    def task_queue(self):
#        return self._task_queue  # 返回发送任务队列

#    #@task_queue.setter
#    #def task_queue(self, value):
#    #    if not isinstance(value, int):
#    #        raise ValueError('score must be an integer!')
#    #    if value < 0 or value > 100:
#    #        raise ValueError('score must between 0 ~ 100!')
#    #    self._task_queue = value

#    def result_queue(self):
#        return self._result_queue

#    def Start(self):
#        # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
#        QueueManager.register('get_task_queue', callable = self._task_queue)
#        QueueManager.register('get_result_queue', callable =  self._result_queue)
#        #assert f(3,4) == 7
#        try:
#            # 启动Queue:
#            self.manager.start()
#            # 获得通过网络访问的Queue对象:
#            task = self.manager.get_task_queue()
#            result = self.manager.get_result_queue()# 放几个任务进去:
#            for i in range(10):
#                n = random.randint(0, 10000)
#                print('Put task %d...' % n)
#                task.put(n)
#            # 从result队列读取结果:
#            print('Try get results...')
#            for i in range(10):
#                r = result.get(timeout=10)
#                print('Result: %s' % r)
#        except Exception as ex:
#            print(ex)
     
#    # 关闭:
#    def Stop(self):
#        self.manager.shutdown()
#        print('master exit.')

#if __name__ == "__main__":
#    freeze_support()
#    master = Ask_Master()
#    master.Start()

#当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用
#但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

# coding=utf-8

import random
import time
#import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Queue

class QueueManager(BaseManager):  # 从BaseManager继承的QueueManager:
    pass

class Ask_Master(object):
    def __init__(self, **kwargs):
        # windows需要写ip地址
        self.manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')        
        # 发送任务的队列:
        self._task_queue = Queue()
        # 接收结果的队列:
        self._result_queue = Queue()

    # windows下运行
    #廖雪峰的教程有问题 不要用系统的queue 需要用 multiprocessing的 queue

    #You need to change “from queue import Queue” to “from multiprocessing import Queue”.
        #The root reason is the former Queue is designed for threading module
        #Queue while the latter is for multiprocessing.Process module.
        #For details, you can read some source code or contact me!

    #multiprocessing passes tasks (which include check_one and data) to the worker processes through a Queue.Queue. 
    #Everything put in the Queue.Queue must be pickable. Queues themselves are not pickable:
    def return_task_queue(self):
        return self._task_queue  # 返回发送任务队列
    def return_result_queue(self):
        return self._result_queue # 返回接收结果队列
    def start(self):
        # 把两个Queue都注册到网络上, callable参数关联了Queue对象,它们用来进行进程间通信，交换对象
        #QueueManager.register('get_task_queue', callable=lambda: task_queue)
        #QueueManager.register('get_result_queue', callable=lambda:
        #result_queue)

        QueueManager.register('get_task_queue', callable=self.return_task_queue)   
        QueueManager.register('get_result_queue', callable=self.return_result_queue)
        # 绑定端口5000, 设置验证码'abc':
        #manager = QueueManager(address=('', 5000), authkey=b'abc')
        # windows需要写ip地址
        manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
        self.manager.start()  # 启动Queue:
        # 获得通过网络访问的Queue对象:
        task = self.manager.get_task_queue()  
        result = self.manager.get_result_queue()
        for i in range(10):   # 放几个任务进去:
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n)
        # 从result队列读取结果:
        print('Try get results...')  
        for i in range(10):
            # 这里加了异常捕获
            try:
                r = result.get(timeout=5)
                print('Result: %s' % r)
            except Queue.Empty:
                 print('result queue is empty.')
            # 关闭:
    def stop(self):
        self.manager.shutdown()
        print('master exit.')
if __name__ == '__main__':
    freeze_support()
    print('start!')
    master = Ask_Master()
    master.start()