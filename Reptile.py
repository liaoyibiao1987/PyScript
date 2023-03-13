# -*- coding: UTF-8 -*-       只能放在所有代码的开始的第一行第一列
import urllib
import urllib.request

res = urllib.request.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
print(res.read().decode("utf-8"))

"xxxx"

divm = divmod(20,6)
print(divm[0])

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('lily',20,job = "ITer")

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) #a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) #a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}