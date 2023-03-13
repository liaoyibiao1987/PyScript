import itertools
import time

def TestIteCount():
    natuals = itertools.count(30,30) #count(初始值，步长)会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出
    for x in natuals:
        print(x)
        if x > 200:
            break


def TestIteCount2():
    natuals = itertools.count(1,2)
    ns = itertools.takewhile(lambda x: x <= 100, natuals) #takewhile()等函数根据条件判断来截取出一个有限的序列
    for x in ns:
        print(x)

def TestIteCycle():
    cs = itertools.cycle('ABC')
    count = 0
    for x in cs:
        count += 1
        print(x)
        if(count > 10):
            break


def TestIteRepeat():
    ns = itertools.repeat('Abc', 3)#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
    count = 0
    for x in ns:
        count += 1
        print(x)
        if(count > 10):
            break

def TestIteChain():#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
    for c in itertools.chain('ABC', 'XYZ'):
        print(c)

def TestIteGroupBy():
    for key, group in itertools.groupby('AAaaaaaABBccccBCCAAA', lambda c: c.upper()):
        print(key, list(group))


def GetPi(N):
    '''
     获取圆周率
    '''
    natodd = itertools.takewhile(lambda x: x < 2 * N ,itertools.count(1,2))
    parfactor = 4
    retPi = 0
    for x in natodd:
        retPi +=  parfactor / x
        #print("%s  %s" % (x,parfactor))
        parfactor = -parfactor
    print(retPi)

if __name__ == '__main__':
    TestIteCount()
    TestIteCycle()
    TestIteRepeat()

    TestIteCount2()
    TestIteChain()
    TestIteGroupBy()

    GetPi(30000000)