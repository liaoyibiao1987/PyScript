# -*- coding: utf-8 -*-
#def 发送邮件(内容)
#    #发送邮件提醒
#    连接邮箱服务器
#    发送邮件
#    关闭连接
    
#while True：
#    if cpu利用率 > 90%:
#        发送邮件('CPU报警')
    
#    if 硬盘使用空间 > 90%:
#        发送邮件('硬盘报警')
    
#    if 内存占用 > 80%:
#        发送邮件('内存报警')

#   函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
#   任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
#   函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
#   函数内容以冒号起始，并且缩进。
#   Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
##   def：表示函数的关键字
##   函数名：函数的名称，日后根据函数名调用函数
##   函数体：函数中进行一系列的逻辑计算，如：实现报警，发送邮件。
##   参数：为函数体提供数据
##   返回值：当函数执行完毕后，可以给调用者返回数据。
import sys
import webbrowser

def OpenLink(url):
    #发送邮件提醒
    webbrowser.Opera.open(url, new=0, autoraise=True)

print(webbrowser.get())
#OpenLink('www.baidu.com')
#x = webbrowser.Opera()
#x.open('www.baidu.com')

#defualt argument
def defualtArg(name, age=21):
    print("%s:%s" % (name,age))
defualtArg('刘德华')

#sync argument
#   参数前一个“*”：在函数中会把传的参数转成一个元组。
def syncArgument(*args):
    print(type(args))
    print(args)
# 执行方式一
syncArgument(11,33,4,4454,5)
# 执行方式二
li = [11,2,2,3,3,4,54]
syncArgument(*li)
syncArgument(li)

#   “**args”的参数：函数中被转成一个字典。
#sync argument dictianary
def syncDict(**kwargs):
    print(type(kwargs))
    print(kwargs)
# 执行方式一
#syncDict(name='liuyao',age = 21)
syncDict(name='liuyao',age = 21)
# 执行方式二
li = {'name':'liuyao','age':21,'job':'IT'}
syncDict(**li)

#   也是没问题的，需要注意的是必须*args在前**kwargs在后，参数也是一样。
def mixSyncArg(*args,**kwargs):
    print("%s----%s" % (args,kwargs))
mixSyncArg(1,2,a=1,b=2)
list_1 = [1,2]
dic = {'a':1,'b':2}
mixSyncArg(list_1,dic)    #   Result：([1, 2], {'b': 2, 'a': 1})----{} 后面的字典竟然是空的- -！

#       我们需要叫函数知道那个变量是*args的参数，哪个是**args的参数，正确传参写法：
mixSyncArg(*list_1,**dic)


#------------inner function---------------
print(chr(56))

#   all()集合中的元素都为真的时候为真,若为空串返回为True
li = ['yao','liu']
li_1 = []
print(all(li))
print(all(li_1))    

#   ord()返回字符对应的ASC码数字编号
print(ord('A'))

#   bin(x)将整数x转换为二进制字符串
print(bin(3256))
#   bool(x)返回x的布尔值
print(bool(0),bool(1))

#   dir()不带参数时，返回当前范围内的变量、方法和定义的类型列表，带参数时，返回参数的属性、方法列表。
print(dir())
#print(dir(list))
#print(dir(webbrowser.Opera))

#   eval()将字符串str当成有效的表达式来求值并返回计算结果。
name = '[[1,2], [3,4], [5,6], [7,8], [9,0]]'
a = eval(name)
b = eval("1 + 2 / 3")
print("%s - %s - %s" % (name,type(name),b))

#   filter(function, iterable)函数可以对序列做过滤处理
def guolvhanshu(num):
    if num > 5 and num < 10:
        return num
seq = (12,50,8,17,65,14,9,6,14,5)
result = filter(guolvhanshu,seq)
print(list(result))

#   hex(x)将整数x转换为16进制字符串
print(hex(123))

#   id()返回对象的内存地址
print(id(seq))
#   len()返回对象的长度
print(len(name))

#   map遍历序列，对序列中每个元素进行操作，最终获取新的序列。
li = [11, 22, 33]
li_1 = map(lambda a: a + 100, li)
print(li_1)
print(list(li_1))

li = [11, 22, 33]
sl = [1, 2, 3]
lit = map(lambda a, b: a + b, li, sl)
print(list(lit))

#   oct()八进制转换
print(oct(10))
print(hex(10))

#   .range()产生一个序列，默认从0开始
#line 1：array = [1, 2, 5, 3, 6, 8, 4]一个乱序的list没什么好解释的
#line 2：for i in range(len(array) - 1, 0,
#-1):这就是上边给的例子的第二条，我们替换下就成为range(6,1,-1)，意思是从6到1间隔-1,也就是倒叙的range(2,7,1),随后把这些值循环赋给i，那么i的值将会是[6,
#5, 4, 3, 2]
#line 3：for j in range(0, i):这是一个循环赋值给j，j的值将会是[0, 1, 2, 3, 4, 5][0, 1, 2, 3,
#4][0, 1, 2, 3][0, 1, 2][0, 1]
#那么上边两个循环嵌套起来将会是
#i------------6
#j------------0j------------1j------------2j------------3j------------4j------------5
#i------------5
#j------------0j------------1j------------2j------------3j------------4
#i------------4
#j------------0j------------1j------------2j------------3
#i------------3
#j------------0j------------1j------------2
#i------------2
#j------------0j------------1
#line 4：if array[j] > array[j + 1]:
#>>> array = [1, 2, 5, 3, 6, 8, 4]
#>>> array[0]
#1
#>>> array[1]
#2
#>>> array[2]
#5
#>>> array[3]
#3
#>>> array[4]
#6
#>>> array[5]
#8
#>>> array[6]
#4
#其实·就是使用这个把这个没有顺序的array = [1, 2, 5, 3, 6, 8, 4]排序
#line 5：array[j], array[j + 1] = array[j + 1], array[j] 替换赋值
#line 6：打印出来
#其实要想省事儿，sort()函数一句就能搞定.......
array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array) - 1, 0, -1):
    print(i)
    for j in range(0, i):
        print(j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)

#
for i in range(5):
    print(i)
    i += 2
    print(i)
    print('一轮结束')
i = 0
#
while i < 5:
    print(i)
    i += 2
    print(i)
    print('一轮结束')
a = ['Mary ', 'had', 'a', 'little ', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#   reversed()反转
re = list(range(10))
re_1 = reversed(re)
print(re_1)
print(list(re_1))

#   round()四舍五入
print(round(4.89333332,6))
print(round(5444222233,6))

#"""returns the factorial of n"""
def getFactorial(n):
    if n == 0:
        return 1
    else:
        k = n * getFactorial(n - 1)
        return k
for k in range(1, 70):
    print("factorial of", k,"=", getFactorial(k))

print(r'PapayaWhip\foo')

#int (有符号整数): 通常被称为只是整数或整数，是正或负整数，不带小数点。
#long (长整数 ): 或长，是无限大的整数，这样写整数，后面跟着一个大写或小写的L。
#float (浮点实数值) : 或浮点数，表示实数，并写入一个小数点分隔的整数部分和小数部分。浮点数也可以是科学记数法，用e或E表示的功率10 (2.5e2
#= 2.5 x 102 = 250).
#complex (复数) : 形式如 a + bJ，其中a和b是浮点和J（或j）表示-1的平方根（这是一个虚数）。
#a是数的实部，b是虚部。Python编程不使用复杂的数字。

#   .sum()对集合求和

#   vars()返回对象的变量，若无参数与dict()方法类似。
print(vars())

#   zip()zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print(xyz)
print(*xyz) 
print(list(xyz),"=====")
#   [x] * 3生成一个列表的列表，它有3个元素，[x, x, x]
#   zip(* [x] * 3)的意思就明确了，zip(x, x, x)
x = [1, 2, 3]
r = zip(*[x] * 3)
print(*r)

a = [1, 2, 3, 4, 5, 6]
print([iter(a)])
b = zip(*([iter(a)] * 2))
print(*b)


print("内建立函数".center(20,'='))
from functools import reduce
#   reduce对于序列内所有元素进行累计操作
#   reduce的第一个参数，函数必须要有两个参数
#   reduce的第二个参数，要循环的序列
#   reduce的第三个参数，初始值
li = [11, 22, 33]
result = reduce(lambda arg1, arg2: arg1 + arg2, li)
print(result)


def f(x):
    return x * x
r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

from _functools import reduce
def add(x, y):
    return x + y

list = reduce(add, [0, 1, 0, 0, 0])
print(list)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print("用filter求素数".center(50,'='))
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
    if n < 2600:
        print(n)
    else:
        break

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

print("函数返回值".center(50,'='))
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

print("闭包---> 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量".center(50,'='))
def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)#只是返回了函数地址，没有执行函数
    return fs

f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#===================#===================#===================
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
print(count())
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#===================#===================#===================
print("装饰器".center(20,'='))
def log(func):
    def wrapper(*args, **kw): #名称必须为wrapper
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
print(now())

#x = log(now)
#x()
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

print("@log2".center(20,'='))
@log2('execute')
def now2():
    print('2015-3-25')
print(now2(), now2.__name__) # now2() == None,和两层嵌套的decorator相比，3层嵌套的效果是这样的：(Real)Now = log('execute')(now2)
                             # 经过decorator装饰之后的函数，它们now2的__name__已经从原来的'now2'变成了'wrapper'

#在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
#decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
#再思考一下能否写出一个@log的decorator，使它既支持：
import functools
def logx(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def logy(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#x = logy('execute')(now)
#print(x())
print("@logy".center(20,'='))
@logy('execute')
def now3():
    print('2015-3-25')

print(now3(), now3.__name__) #@functools.wraps(func) 保证运行过后now3.__name__不变
print("偏函数".center(60,'='))
def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))

import functools
int2 = functools.partial(int, base=2)#创建偏函数时，实际上可以接收(函数对象、*args和**kw)这3个参数
                                     #*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
                                                                          #相当于：kw = {'base':2}
max2 = functools.partial(max, 10)   #实际上会把10作为*args的一部分自动加到左边，
                                    #也就是：max2(5, 6, 7)
                                                                     #相当于：
                                                                                                      #args =(10, 5,6, 7)
                                                                                                      #max(*args)
print(max2(5,6,7,15))


if __name__ == '__main__': 
    print(__name__) 




