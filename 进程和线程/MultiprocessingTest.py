# coding=utf-8
from multiprocessing import Pool,Queue,Lock,Pipe
from multiprocessing import Process
import os, time, random
import subprocess

class MultiprocessingTest(object):
    """description of class"""
    @staticmethod
    def TestFork():
        print('显示当前进程 %s %s' % (os.getppid() , os.getpid()))
        #pid = os.fork() # Only works on Unix/Linux/Mac:
        #if pid == 0:
        #    print('I am child process (%s) and my parent is %s.' %
        #    (os.getpid(), os.getppid()))
        #else:
        #    print('I (%s) just created a child process (%s).' % (os.getpid(),
        #    pid))
#==================测试多进程=========
def TestMulit(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

#==================测试线程池=========
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
def TestPool():
    p = Pool(4)                 #task 0，1，2，3是立刻执行的，而task
                                #4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
    for i in range(5):          #如果改成：p =
                                #Pool(5)就可以同时跑5个进程。Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
        p.apply_async(long_time_task, args=(i,)) #进程池
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()                    #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close(),调用close()之后就不能继续添加新的Process了
    print('All subprocesses done.')

#==================测试子进程=========
def Testsubprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
    #如果子进程还需要输入，则可以通过communicate()方法输入
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    #print(output.decode('utf-8'))
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)

#==================测试进程见通讯=========
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
def TestIPC():
    '''
    Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
    '''
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

#==================测试queue=========
# 写入 worker
def inputQ(queue):
    while True:
        info = "进程号 %s : 时间: %s" % (os.getpid(),int(time.time()))
        queue.put(info)
        time.sleep(1)
# 获取 worker
def outputQ(queue,lock):
    while True:
        info = queue.get()
#        lock.acquire()
        print(str(os.getpid()) + '(get):' + info)
#        lock.release()
        time.sleep(1)

def Testqueue():
    record1 = []   # store input processes
    record2 = []   # store output processes
    lock = Lock()    # To prevent messy print
    queue = Queue(3)
 
    # input processes
    for i in range(10):
        process = Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)
 
    # output processes
    for i in range(10):
        process = Process(target=outputQ,args=(queue,lock))
        process.start()
        record2.append(process)


#==================测试pipe=========
def send(pipe):
    pipe.send(['spam'] + [42, 'egg'])
    pipe.close()

def talk(pipe):
    pipe.send(dict(name = 'Bob', spam = 42))
    reply = pipe.recv()
    print('talker got:', reply)
    pipe.close()

def TestPipe(): #Pipe实例成双成对,传入进程的头一个被用来发送，后一个被用来收取
    (con1, con2) = Pipe()
    sender = Process(target = send, name = 'send', args = (con1,))
    sender.start()
    print("con2 got: %s" % con2.recv())#从send收到消息
    #con2.close() #主进程的不需要回收了

    (parentEnd, childEnd) = Pipe()
    child = Process(target = talk, name = 'talk', args = (childEnd,))
    child.start()
    print('parent got:', parentEnd.recv())
    parentEnd.send({x * 2 for x in 'spam'})
    child.join()
    print('parent exit')


def son_process(x, pipe):
    (_out_pipe,_in_pipe) = pipe

    # 关闭fork过来的输入端
    print("_in_pipe在子进程被关闭了。%s; %s" % (_out_pipe, _in_pipe))
    _in_pipe.close()
    while True:
        try:
            msg = _out_pipe.recv()
            print(msg)
        except EOFError:
            # 当out_pipe接受不到输出的时候且输入被关闭的时候，会抛出EORFError，可以捕获并且退出子进程
            break
def TestPipe2():
    (out_pipe, in_pipe) = Pipe(True)                                     #Pipe实例化一次则新建一个管道，但是每次传入到其他进程都会新建一对（个）通道。
    son_p = Process(target=son_process, args=(100, (out_pipe, in_pipe))) #out_pipe，in_pipe传到里面会copy一个副本，in_pipe副本也需要被关闭的，其实不用传入进去
                                                                         #多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享
    son_p.start() 
    # 等pipe被fork 后，关闭主进程的输出端
    # 这样，创建的Pipe一端连接着主进程的输入，一端连接着子进程的输出口
    out_pipe.close()
    for x in range(10,100,6):
        in_pipe.send(x)
    print("in_pipe在主进程被关闭了。%s; %s" % (out_pipe, in_pipe))
    in_pipe.close()
    son_p.join()
    print("主进程也结束了")

def son_process2(pi):
    for x in range(1,60):
        print('开始发送消息'.center(30,'='))
        pi.send("消息ID:"+ str(x))
        time.sleep(0.1)

def son_process3(pi):
    while True:
        msg = pi.recv()
        print("son_process3 收到消息 :" + msg)

def TestPipe3():##一边发 两边收,默认只有轮询两边一边收一次
    (out_pipe, in_pipe) = Pipe(True)    #Pipe(True) 后面的true 传入的表示out_pipe 都可读可写，
                                        #所以下面传入的是（1.in_pipe->2.out_pipe）还是（1.out_pipe->2.in_pipe）都无关紧要，反正都可以做为端点去收发
                                        #in_pipe、out_pipe类似于windows中管道的地址"../pip/XXX/xxx" 传入的子进程的只是一个副本（或者说“字符串表示的实体”）
    #in_pipe.close()#传入到子进程后再关闭输入端
    son_p = Process(target=son_process2, args=(in_pipe,)) 
    son_p.start() 
    #in_pipe.close()#传入到子进程后再关闭输入端，因为这个mainthread 已经用不着输入端了 in_pipe
    son_p2 = Process(target=son_process3, args=(out_pipe,)) 
    son_p2.start()
    #如果没有下面这句，则可以out_pipe.close(),因为输入端已经传入两个子进程，无所谓关闭和打开了。
    #out_pipe.close()
    #son_p.join() #阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。
    #son_p2.join()
    while True:
        msg = out_pipe.recv()
        print("TestPipe3 收到消息 :" + msg)


if __name__ == '__main__':
    #MultiprocessingTest.TestFork()
    
    #print("测试多进程".center(50,'='))
    #p = Process(target = TestMulit, args = ('test',))
    #print('Child process will start.')
    #p.start()
    #p.join()
    #print('Child process end.')

    
    #print("测试线程池".center(50,'='))
    #TestPool()

    #print("测试子进程".center(50,'='))
    #Testsubprocess()
    
    #print("测试进程见通讯".center(50,'='))
    #TestIPC()

    #print("测试queue".center(50,'='))
    #Testqueue()

    #TestPipe()

    TestPipe3()
    #TestPipe2()