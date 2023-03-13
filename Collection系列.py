# -*- coding: utf-8 -*-

#   collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型，分别是：
#   OrderedDict类：排序字典，是字典的子类。引入自2.7。
#   namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
#   Counter类：为hashable对象计数，是字典的子类。引入自2.7。
#   deque：双向队列。引入自2.4。
#   defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。
print("collections")

# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
print('Counter'.center(40,'-'))

import collections
c = collections.Counter()# 创建一个空的Counter类
print(c)
c = collections.Counter('asdfghjjhgfdqwer')
print(c)
c = collections.Counter({'a': 4, 'b': 2})#从一个字典对象创建
print(c)
c = collections.Counter(a=4, b=2) # 从一组键值对创建
print(c)

#   计数值的访问:当所访问的键不存在时，返回0，而不是KeyError；否则返回它的计数。
c = collections.Counter('AAAA,BBBB,CBAD,BBCD,CDAA')
print(c['A'])

print('Counter Update()'.center(40,'-'))
#   update()更新
c = collections.Counter({'s': 3, 'd': 3, 'a': 2, 'f': 2, 'g': 1})
c.update('update')
print(c)
#   subtract()减少:最后可以出现负数
c.subtract('subtract')
print(c)
#   键的删除当计数值为0时，并不意味着元素被删除，删除元素应当使用del
c['d'] = 0
print(c)
del c['s']
print(c)

print("------迭代器------")
#   迭代器:返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。所有元素按照字母序排序，个数小于1的元素不被包含
print(list(c.elements()))

print("------most_common------")
#   most_common([n]):返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，按照字母序排列
print(c.most_common(1))

#浅拷贝
cc = c.copy()
print(c)

#   算术与集合操作
#   +、-、&、|操作也可以用于Counter。其中&和|操作分别返回两个Counter对象各元素的最小值和最大值。需要注意的是，得到的Counter对象将删除小于1的元素。
print('算术与集合操作')
c = collections.Counter(a=3, b=1,c=2)
d = collections.Counter(a=1, b=2)
print(c + d)
print(c - d)
print(c & d)
print(c | d)

#   一些Counter类的常用操作，来源于Python官方文档
sum(c.values())  # 所有计数的总数
c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
print(c.items())  # 转为(elem, cnt)格式的列表
#       list_of_pairs =(a=4, b=2)
#       collections.Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
c = collections.Counter('AAAA,BBBB,CBAD,BBCD,CDAA')
print(c)
d = c.most_common()[:-2:-1]  # 取出计数最少的n个元素
print(d)
c += collections.Counter()  # 移除0和负值
print(c)