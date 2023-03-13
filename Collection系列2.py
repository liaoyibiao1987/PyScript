# -*- coding: utf-8 -*-

#   collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型，分别是：
#   OrderedDict类：排序字典，是字典的子类。引入自2.7。
#   namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
#   Counter类：为hashable对象计数，是字典的子类。引入自2.7。
#   deque：双向队列。引入自2.4。
#   defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。
print("有序字典(orderedDict )")
import collections
info = collections.OrderedDict({'name':'liuyao','age':21})
print(type(info))
print(info.keys())
print(info.values())

#   move_to_end将指定的键值对从开头移动到末尾。
info.move_to_end('name')
print(info)

#   pop删除字典键值，返回删除的键值的values
print(info.pop('age'))
print(info)

from functools import reduce
print(reduce(lambda x, y: x + y, [1,2,3,4,5]))
#   clear清除有序字典的值
info = collections.OrderedDict({"A":2,'V':2,'C':3,'D':89})
info.clear()
print(info)


print('\r\n默认字典(defaultdict)')
print('这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.')
print('defaultdict是对字典的类型的补充，他默认给字典的值设置了一个类型。创建一个默认字典，value值类型为列表.dic = collections.defaultdict(list)')

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
##  defaultdict可以接受一个内建函数list作为参数。其实呢，list()本身是内建函数，但是再经过更新后，python里面所有东西都是对象，所以list改编成了类，引入list的时候产生一个类的实例。
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)
x = list(d.items())
print(x)

dic = collections.defaultdict(list)
dic['k1']
print(dic)
print(dic.keys())
print(dic.values())
dic['k1'].append('v1')
print(dic.values())

print('可命名元组(namedtuple)')
tu = collections.namedtuple('tu',['x','y','z'])  #创建一个类,类名为Point
yao_tu = tu(11,22,33)
print(yao_tu)
print(yao_tu.x)  #直接通过命名元素去访问元组对应的元素,
print(yao_tu[1])  #等同于上面这种方式,但是没有上面这种方式可读性强
print(yao_tu.y)
print(yao_tu.z)
x,y,z = yao_tu #unpack
print(x,y,z)
d = yao_tu._asdict()
print(d['x'])
e = tu(**d)
print(e)

#什么是星号变量（*）
#最初，星号变量是用在函数的参数传递上的，在下面的实例中，单个星号代表这个位置接收任意多个非关键字参数，在函数的*b位置上将其转化成元组，而双星号代表这个位置接收任意多个关键字参数，在**b位置上将其转化成字典：
#* 该位置接受任意多个非关键字（non-keyword）参数，在函数中将其转化为元组（1,2,3,4）
#** 该位置接受任意多个关键字（keyword）参数，在函数**位置上转化为词典 [key:value, key:value ]
#unpack参数星号*把序列/集合解包（unpack）成位置参数，两个星号**把字典解包成关键字参数
def foo(*args, **kwarg):
    for item in args:
        print(item)
    for k,v in kwarg.items():
        print(k,v)
    print(30 * '=')

if __name__ == '__main__':
    #foo(1, 2, 3, a=4, b=5)
    #foo(2, 3, a=4, b=5, c=1)
    v = (1, 2, 4)
    v2 = [11, 15, 23]
    d = {'a':1, 'b':12}
    #   (1, 2, 4)
    #   {'a': 1, 'b': 12}
    foo(v, d)
    #   1
    #   2
    #   4
    #   a 1
    #   b 12
    foo(*v, **d)
    #   [11, 15, 23]
    #   {'a': 1, 'b': 12}
    foo(v2, d)
    #   11
    #   15
    #   23
    #   a 1
    #   b 12
    foo(*v2, **d)



print('双向队列(deque)')
que = collections.deque(['sb','liu','yao'])
print(que)

#   追加元素到队列
que.append('wo')
print(que)

#   追加元素到队列左侧
que.appendleft('zuo')
print(que)

#   统计元素个数
print(que.count('zuo'))
#   que.clear()

#   extend扩展元素
que.extend(['a','b','c'])
print(que)

#   extendleft从左侧扩展
que.extendleft(['zuo4','zuo5','zuo6'])
print(que)

#   pop删除
print(que.pop())
print(que)

#   popleft从左侧开始删除
print(que.popleft())
print(que)
 
#   reverse顺序反转
print(que.reverse())
print(que)

#   remove删除指定元素
que.remove('sb')
print(que)

#   rotate将队列末尾4个元素反转到队列左侧
que.rotate(4)
print(que)


#单向队列 queue（先进先出 FIFO ）
print('单向队列 queue（先进先出 FIFO ）'.center(40,'-'))

import queue
que = queue.Queue(2)
print(que)
que = queue.Queue(maxsize=10)   #   如果maxsize小于1就表示队列长度无限。
print(que)

que.put(['a','d','A','2'])

#   调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。
print(que.get(1,200))
print(que.qsize())
que.put(['a','d','A','2'])
print(que.qsize())
#que.clear()
with que.mutex:
    que.queue.clear()
que.put(('a','d','A','2'))
print(que.qsize())
print(que.empty())
print(que.full())

while not que.empty():
    try:
        que.get(False)
    except Empty:
        continue
    que.task_done()

que.mutex.acquire()
que.queue.clear()
que.all_tasks_done.notify_all()
que.unfinished_tasks = 0
que.mutex.release()

#   q.get([block[, timeout]]) 获取队列，timeout等待时间
#   q.get_nowait() 相当q.get(False)
#   非阻塞 q.put(item) 写入队列，timeout等待时间
#   q.put_nowait(item) 相当q.put(item, False)
#   q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
#   q.join() 实际上意味着等到队列为空，再执行别的操作

#   1.为什么要拷贝？
#       当进行修改时，想要保留原来的数据和修改后的数据
#   2.数字字符串 和 集合 在修改时的差异？ （深浅拷贝不同的终极原因）
#       在修改数据时：
#       数字字符串：在内存中新建一份数据
#            集合：修改内存中的同一份数据
#   3.对于集合，如何保留其修改前和修改后的数据？
#       在内存中拷贝
#   4.对于集合，如何拷贝其n层元素同时拷贝？
#       深拷贝

#   对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一个内存地址。
n1 = 123
n2 = n1
print(id(n1),'==',id(n2))

import copy
n3 = copy.copy(n1)
print(id(n1),'==',id(n3))

#   对于字典、元祖、列表 而言，进行赋值、浅拷贝和深拷贝时，其内存地址的变化是不同的。
#   赋值，只是创建一个变量，该变量指向原来内存地址，如：
n1 = {'k1':'v1','k2':'v2','k3':['liuyao','job']}
n2 = n1
print(id(n1),'==',id(n2))
#浅拷贝，在内存中只额外创建第一层数据
n3 = copy.copy(n1)
print(id(n3), '!=' ,id(n1))
print(id(n3['k3'][0]), '==' ,id(n1['k3'][0]))

n4 = copy.deepcopy(n1)
print(id(n4), '!=' ,id(n1))
print(id(n4['k3'][0]), '!=' ,id(n1['k3'][0]))


print('获取Key'.center(30,'='))


import sys,os,hashlib,time,base64

def encode(string,key):
    result = ''
    result = docrypt(string,key)
    return base64.b32encode(result.encode('utf-8'))

def decode(string,key):
    result = ''
    string = base64.b32decode(string)
    docrypt(string,key)
    return result

def docrypt(string,key):
    string_lenth = len(string)
    result = ''
    box = list(range(256))
    randkey = []
    key_lenth = len(key)

    for i in range(255):
      randkey.append(ord(key[i % key_lenth]))

    for i in range(255):
      j = 0
      j = (j + box[i] + randkey[i]) % 256
      tmp = box[i]
      box[i] = box[j]
      box[j] = tmp

    for i in range(string_lenth):
      a = j = 0
      a = (a + 1) % 256
      j = (j + box[a]) % 256
      tmp = box[a]
      box[a] = box[j]
      box[j] = tmp
      result += chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))
    return result
def GetKey(key):
    # def getodd(liststr):
    #     for i in range(len(liststr)):
    #         yield
    xa = map(lambda a, b: ((ord(b) ^ 0x8A) if (a % 2 == 0) else (ord(b) ^ 0x25)), range(len(key)), key)
    #print(xa) 
    return reduce(lambda x, y: '%s%s' % (x if isinstance(x,str) else chr(x) , chr(y)), xa)
x = bytes(GetKey('111111'), encoding = "utf-8")
y = GetKey('111111')
# aa = b'123456姜军' # bytes can only contain ASCII literal characters.
aa = b'123456'
nn = '123456姜军'
ff = nn.encode() 

print("%s -> %s" % (x , y))
print(encode('HelloWorldTTT','iamthekey'))