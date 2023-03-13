import sys
sys.path.append("/to/path/win32file")
sys.path.append("/to/path/win32con")
import win32file
import win32con

def fab(max):
    a,b = 0,1
    while a < max:
        yield a
        a,b = b,a + b
    return 32768

def inner():
    coef = 1
    total = 0
    while True:
        try:
            input_val = yield total
            total = total + coef * input_val
        except SwitchSign:
            coef = -(coef)
        except BreakOut:
            return total

def outer1():
    print("Before inner(), I do this.")
    i_gen = inner()
    input_val = None
    ret_val = i_gen.send(input_val)
    while True:
        try:
            input_val = yield ret_val
            ret_val = i_gen.send(input_val)
        except StopIteration:
            break
        except Exception as err:
            try:
                ret_val = i_gen.throw(err)
            except StopIteration:
                break
    print("After inner(), I do that.")

def outer2():
    print("Before inner(), I do this.")
    yield from inner()
    print("After inner(), I do that.")

for x in fab(600):
    print(x)  
      
print(fab(600))
print("分割线".center(30,'='))
mylist = [x * x for x in range(3)] #所有你可以使用 for ..  in ..
                                   #语法的叫做一个迭代器：列表，字符串，文件……你经常使用它们是因为你可以如你所愿的读取其中的元素，但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。
for i in mylist :
    print(i)
print("分割线2".center(30,'='))
for i in mylist :
    print(i)

mygenerator = (x * x for x in range(60))
from collections import Iterable
print(isinstance(mygenerator, Iterable))

for i in mygenerator:
    print(i)

print("分割线3".center(30,'='))
for i in mygenerator:
    print(i)
#看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 for i in mygenerator ,
#因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…

#print(list(outer2()))
for i in range(3):
    print(i)


print("分割线4".center(30,'='))
xiaoke = [2,3,4,5]
# 生成器generator，类似于list，但是是把[]改为()
gen = (a * a for a  in xiaoke)
for  i  in gen:
    print(i)


print("分割线5".center(30,'='))
def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

t = test()
print(t.__next__())
#使用send执行 输出结果: (可见next输出temp为none , 而send 则把值传递进了生成器)
t.send("1231231231223123")
print(t.send("hahahahhahaha"))


from functools import reduce
sum = reduce(lambda x , y : x + y, (1,2,3,4,5,6,7))  

from collections import Iterator
print(isinstance([],Iterator)) #判断一个对象是否是Iterator对象 next()实现方法
print(isinstance(iter([]),Iterator)) #强制转换
print(isinstance([], Iterable)) #判断一个对象是否是Iterable对象 list、tuple、dict、set、str

print(isinstance((x for x in range(10)), Iterable))
print(isinstance((x for x in range(10)), Iterator))