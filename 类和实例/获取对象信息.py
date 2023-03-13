from 继承和多态 import *


print('获取对象信息开始了'.center(60,'='))
print(type(123))
print(type(int))
print(type(123) == type(456))


a = Animal()
d = Dog()
c = Cat()

if(isinstance(d,Animal)):
    print("Animal Yesssssss........")
if(isinstance(b'a', bytes)):
    print("Bytes Noooooooo.....")


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x') )# 有属性'x'吗？
print(hasattr(obj, 'y') )
setattr(obj, 'y', 19)
print(getattr(obj, 'y') )