class Student(object):
    def set_age(self, age): # 定义一个函数作为实例方法
        self.age = age
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age2(self, age): # 定义一个函数作为实例方法
    self.age = age + 100
from types import MethodType
s2 = Student()
#
#给一个实例绑定的方法，对另一个实例是不起作用的：
#
print(r'实例绑定的方法，其他实例无法生效'.center(60,'='))
s2.set_age = MethodType(set_age2, s2)
s2.set_age(20)
print(s2.age)
s.age = 20
print(s.age)
#
#为了给所有实例都绑定方法，可以给class绑定方法
#
print(r'给类绑定方法，所有实例都生效'.center(60,'='))
def set_score(self, score):
    self.score = score
Student.set_score = set_score

s.set_score(20)
s2.set_score(20)
print(s.score)
print(s2.score)


print(r'使用__slots__限制添加'.center(60,'='))

#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student2(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s3 = Student2()
s3.name = 'pingpingliao'
print(s3.name)
s3.age = 20
print(s3.age)
#s3.score = 99 # 绑定属性'score'
#print(s3.score)
