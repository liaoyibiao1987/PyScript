import aiml
os.chdir('.//alice') # 将工作区目录切换到刚才复制的alice文件夹
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

alice.respond('hello')



from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')