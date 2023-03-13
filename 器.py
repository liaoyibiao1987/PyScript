
#-----------------迭代器--------- ------
#迭代器是一个流对象，并不是存在的一个完整的可见实体
#可迭代对象（Iterable[for x in y]）和迭代器（Iterator[for x in y & next()/send()/close()]）
#可迭代对象包括 1：如list、tuple、dict、set、str等。2：generator，包括生成器和带yield的generator function。
#迭代对象变迭代器的方法
#1、列表生成式的[]改成()，就创建了一个generator (List = [x * x for x in range(10)] || Generator = (x * x for x in range(10)))
#2、iter(['liu','yao','sb'])
#3、yield return
print('迭代器'.center(40,'-'))

names = iter(['liu','yao','sb'])
print(names)
print(names.__next__())
print(names.__next__())
#_iter__()返回迭代器对象本身
print(names.__iter__())

#-----------------生成器--------- ------
#一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator[直接的做法就是函数中含有yield语法]
#这个yield的主要效果呢，就是可以使函数中断，并保存中断状态，中断后，代码可以继续往下执行，过一段时间还可以再重新调用这个函数，从上次yield的下一句开始执行。
print('生成器'.center(40,'-'))
def cash_money(amount):
    while amount > 0:
        amount -= 100
        yield 1000
        print('随便取')
  
atm = cash_money(500)
print(type(atm))
print(atm.__next__())
print('暂停')
print(atm.__next__())

#-----------------yield异步--------- ------
import time
print('yield异步'.center(40,'-'))
def consumer(name):
    print("%s准备吃包子啦" % (name))
    while True:
        baozi = yield
        print("包子来了[%s],被[%s]吃了!" % (baozi,name))
def producer(name):
    c1 = consumer('mayun')
    c2 = consumer('mahuateng')
    c1.__next__()
    c2.__next__()
    print('%s要开始做包子啦' % (name))
    for i in range(1,3):
        time.sleep(1)
        print('做了两个包子')
        c1.send(i)
        c2.send(i)
producer('刘德华')

#-----------------装饰器--------- ------
#装饰器是函数，只不过该函数可以具有特殊的含义，装饰器用来装饰函数或类，使用装饰器可以在函数执行前和执行后添加相应操作。
#装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用
#概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
print('装饰器'.center(40,'-'))

def login(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        return func()
    return inner
@login
def 功能1():
    print('功能1')
@login
def 功能2():
    print('功能2')
@login
def 功能3():
    print('功能3')
@login
def 功能4():
    print('功能4')

v = login(功能1)


#-----------------递归--------- ------
print('递归'.center(40,'-'))
def calc(n):
    print(n)
    if n / 2 > 1:
        res = calc(n / 2)
        print('res',res)
    print('N',n)
    return n

calc(10)

#-----------------二分法--------- ------
print('二分法'.center(40,'-'))
def binary_search(data_source,find_n):
    mid = int(len(data_source) / 2)
    if len(data_source) >= 1:
        if data_source[mid] > find_n:
            print('data in left of [ID\033[35;1m %s\033[0m]' % data_source[mid])
            binary_search(data_source[:mid],find_n)
        elif data_source[mid] < find_n:
            print('data in right of [ID\033[32;1m %s\033[0m]' % data_source[mid])
            binary_search(data_source[mid:],find_n)
        else:
            print('found find',data_source[mid])
    else:
        print('not found')
if __name__ == "__main__":
    data = list(range(1,10000))
    binary_search(data,360)

#-----------------斐波那契数列--------- ------
print('斐波那契数列'.center(40,'-'))
#斐波那契数列指的是这样的数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
#233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368
def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        func(arg2,arg3,stop)
func(0,1,(100000))

#-----------------二维数组--------- ------
print('二维数组'.center(40,'-'))
data = [[col for col in range(4)] for row in range(4)]
print('-----------------------')
for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):
        tmp = data[c_index][r_index]
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = tmp
    print('----------------------')
    for r in data:
        print(r)

#-----------------冒泡--------- ------
print('冒泡'.center(40,'-'))
data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
print("原始:",data)
previous = data[0]
for j in range(len(data)):
    tmp = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
    print(data)
print("排序之后:",data)
