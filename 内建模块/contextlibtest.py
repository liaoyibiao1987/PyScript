#并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。实现上下文管理是通过__enter__和__exit__这两个方法实现的

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self): # 类似于单元测试的 setUp()和tearDown()
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):# 类似于单元测试的 setUp()和tearDown()
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)
    
@contextmanager #__enter__和__exit__仍然很繁琐 @contextmanager这个decorator接受一个generator，用yield语句把with
                #as var把变量输出出去，然后，with语句就可以正常地工作了
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

@contextmanager #很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
def tag(name):
    print("<%s>" % name)#执行前
    yield
    print("</%s>" % name)#执行后






#@closing如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen

#@contextmanager
#def closing(thing):
#    try:
#        yield thing
#    finally:
#        thing.close()
def TestClosing():
    with closing(urlopen('https://www.python.org')) as page: #closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单,它的作用就是把任意对象变为上下文对象，并支持with语句
        for line in page:
            print(line.decode('utf-8'))

        #urlopen('https://www.python.org') 返回一个实例对象，对象实现close()的方法
    if page:
        print("对象依然存在")
        for line in page:#对象已经exit
            print(line.decode('utf-8'))

#所有的语法糖 不管是否执行过程中是否发生了异常，执行上下文管理器的 exit() 方法，exit() 方法负责执行“清理”工作，如释放资源等。
#如果执行过程中没有出现异常，或者语句体中执行了语句 break/continue/return，则以 None 作为参数调用 exit(None, None, None)
#如果执行过程中出现异常，则使用 sys.exc_info 得到的异常信息为参数调用 exit(exc_type, exc_value, exc_traceback), 如果没有实现exit()方法或者方法返回 False会报错
if __name__ == '__main__':
    with Query('Bob') as q:
        q.query()

    with create_query('Bob') as q:
        q.query()
    with tag("h1"):
        print("hello")
        print("world")

    TestClosing()
