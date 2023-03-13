import time
import sys
import queue
from multiprocessing.managers import BaseManager
from ask_master import QueueManager
from multiprocessing import spawn

class Task_Worker(object):
    """description of class"""
    def __init__(self):

        #task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中,而Queue之所以能通过网络访问，就是通过QueueManager实现的。
        #由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰

        # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
        QueueManager.register('get_task_queue')
        QueueManager.register('get_result_queue')

        # 连接到服务器，也就是运行task_master.py的机器:
        server_addr = '127.0.0.1'
        print('Connect to server %s...' % server_addr)
        # 端口和验证码注意保持与task_master.py设置的完全一致:
        m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
        # 从网络连接:
        m.connect()
        # 获取Queue的对象:
        self.__task = m.get_task_queue()
        self.__result = m.get_result_queue()

    def start(self):
        # 从task队列取任务,并把结果写入result队列:
        for i in range(10):
            try:
                n = self.__task.get(timeout=1)
                print('run task %d * %d...' % (n, n))
                r = '%d * %d = %d' % (n, n, n * n)
                time.sleep(1)
                self.__result.put(r)
            except Queue.Empty:
                print('task queue is empty.')
        # 处理结束:
        print('worker exit.')
        #data = ((packages, self.set_len, dist.project_name, Version(dist.version)) for dist in self.working_set)
if __name__ == "__main__":
    worker = Task_Worker()
    worker.start()