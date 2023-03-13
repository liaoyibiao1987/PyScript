from multiprocessing import Process
from multiprocessing import Pool
import os, time, random

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':  
    x = (1,2)
    y = ('33333','4','55555555','666')
    z = ((x,par.count,id(par)) for par in y)
    for xx in z:
        print(str(xx))


    print('Parent process %s.' % os.getpid())  
    p = Process(target = run_proc, args = ('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
