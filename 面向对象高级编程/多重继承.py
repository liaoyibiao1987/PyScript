class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass


print(r'如果需要“混入”额外的功能，通过多重继承就可以实现。这种设计通常称之为MixIn'.center(60,'='))

#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。C++也可以
#只允许单一继承的语言（如Java）不能使用MixIn的设计。
class Dog(Mammal, Flyable, Runnable):
    pass