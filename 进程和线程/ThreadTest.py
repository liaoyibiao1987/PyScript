import time
import threading as th
class ThreadTest(object):
    """description of class"""
    def loop(self):
        print('current thread %s' % th.current_thread)
        n = 0
        while n < 5:
            n = n + 1
            print('thread %s >>> %s' % (th.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % th.current_thread().name)
    def TestLoop(self):
        print('thread %s is running...' % th.current_thread().name)
        t = th.Thread(target = self.loop, name='LoopThread')
        t.start()
        t.join()
        print('thread %s ended.' % th.current_thread().name)

    balance = 0
    __lock = th.Lock()
    def change_it(self, n):
        # 先存后取，结果应该为0:
        #global balance
        self.balance = self.balance + n
        print('当前banlce %s' % self.balance)
    def Run_thread(self, n):
        for i in range(1000):
            # 先要获取锁:
            self.__lock.acquire()
            try:
                # 放心地改吧:
                self.change_it(n)
            finally:
                # 改完了一定要释放锁:
                self.__lock.release()

if __name__ == "__main__":
    testthread = ThreadTest()
    
    #testthread.TestLoop()
    testthread.Run_thread(2)