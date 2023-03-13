#coding=utf-8

class Student(object):
    def __init__(self, path=''):
        self.name = path
        self.a = 0
        self.b = 1
        self._path = path
    def __str__(self): #但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看
        return 'Student object (name: %s)' % self.name

    #这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    #解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的
    __repr__ = __str__ #所以，有个偷懒的写法


    #如果一个类想被用于for ...  in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    #然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    #正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
    #Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
    #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    '''   
            def __getattr__(self, attr):
                if attr == 'score':
                    return '你获取到了一个不存在的属性'
                elif attr == 'age':
                    return lambda: 25
                raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    '''
    #这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
    #这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
    #现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
    #http://api.server/user/friends
    #http://api.server/user/timeline/list
    #如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
    #利用完全动态的__getattr__，我们可以写出一个链式调用
    def __getattr__(self, attr):
        if attr == 'score':
            return '你获取到了一个不存在的属性'
        elif attr == 'age':
             return lambda: 25
        return Student('%s/%s' % (self._path, attr))


    #一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
    #任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self):
        print('My name is %s.' % self.name)

class A:
    def foo(self): pass
    bar = foo
    #method 是一种 function，method 有一个__func__ 属性，指向一个 function。
    #A().foo 即为第一种方法创建的 method，A().bar 则为第二种。那段话的意思是: A().bar.__func__ 不是指向 A().foo，而是指向 A().foo.__func__。


if __name__ == '__main__':
    n = Student('XNames')
    for x in n:
        print(x)

    print('Fib(object) 第{0}个 ：{1}'.format(30,n[29]))
    print('Fib(object) 第{0}个 ：{1}'.format([0,30],n[:30]))

    print(n.score, n.age())

    print(n.status.user.timeline.list)


    s = Student('Michael')
    s()

    #那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
    print(callable(Student()))
    print(callable(max))
    print(callable([1, 2, 3]))