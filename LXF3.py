# -*- coding: utf-8 -*-

#列表：shoplist = ['apple', 'mango', 'carrot', 'banana']
#字典：di = {'a':123,'b':'something'}
#集合：jihe = {'apple','pear','apple'}
#元组： t = 123,456,'hello'

##########################################
print('列表 List'.center(40,'='))
## append(self, p_object)用于在列表末尾添加新的对象，obj -- 添加到列表末尾的对象，该方法无返回值，但是会修改原来的列表。
lie = [1,2,3,4,5]
lie.append(6)
print(type(lie))
print(lie.count(2))     ## count(self, value)用于统计某个元素在列表中出现的次数，value -- 列表中统计的对象，返回元素在列表中出现的次数。
##
list2 = ['a', 'b', 'c', 'd', 'f']
lie.extend(list2)
print(lie)

lie.insert(2,'6')       ## insert(self,index,p_object)用于将指定对象插入列表，index--对象obj需要插入的索引位置，obj--要插入列表中的对象，该方法没有返回值，但会在列表指定位置插
print(lie)

print(lie.pop())        ## pop(self,index=None)用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值，index--可选参数，要移除列表元素的对象，该方法返回从列表中移除的元素对象。
print(lie)

lie.reverse()
print(lie)              ## reverse(self)用于反向列表中元素，该方法没有返回值，但是会对列表的元素进行反向排序
##
lie = [1,2,3,4,5,2,112,12]
lie.sort()              ## sort(self,cmp=None,key=None,reverse=False)用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数，该方法没有返回值，但是会对列表的对象进行排序。
print(lie)
##lie.sorted()
print(lie)

#
array = [1, 2, 5, 3, 6, 8, 4]
array[0:] #列出0以后的
array[1:] #列出1以后的
array[:-1] #列出-1之前的
print(array[3:-3]) #列出3到-3之间的
print(array[::2])
print(array[2::])
#如果想让他们颠倒形成reverse函数的效果
print(array[::-1])


#在运行zip(*xyz)之前，xyz的值是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
#那么，zip(*xyz) 等价于 zip((1, 4, 7), (2, 5, 8), (3, 6, 9))
#所以，运行结果是：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
#注：在函数调用中使用*list/tuple的方式表示将list/tuple分开，作为位置参数传递给对应函数（前提是对应函数支持不定个数的位置参数）
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
u = zip(*xyz)
print(list(u))
v = zip(xyz)
print(list(v))

#运行的结果是：
#[(1, 1, 1), (2, 2, 2), (3, 3, 3)]
#它的运行机制是这样的：
#[x]生成一个列表的列表，它只有一个元素x
#[x] * 3生成一个列表的列表，它有3个元素，[x, x, x]
#zip(* [x] * 3)的意思就明确了，zip(x, x, x)
x = [1, 2, 3]
r = zip(* [x] * 3)
print(list(r))

print(list(map(lambda x, y: (x * y, x + y), [1, 2, 3], [4, 5, 6])))  # [(4, 5), (10, 7), (18, 9)]
#print(list(map(None, [1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]
                                                                   #print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]
                                                                   #
from functools import reduce
print(reduce(lambda x, y: x + y, range(1, 3)))
print(reduce(lambda x, y: x + y, [1, 3, 5, 7, 9], 100))#reduce()还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100

############################################
print('元组 Tuple'.center(40,'='))
print('元组可以在映射中当作键使用；\r\n元组作为很多内建函数和方法的返回值存在。\r\n元组的元素是不能被修改，但元素的元素能可以被被修改的')
print('元祖'.center(40,'-'))

boy = ('kelin','yaoyao','liuyao','shabi')
print(type(boy))
print(boy.count('yaoyao'))
print(boy.index('liuyao'))

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

#############################################
print('字典 dic'.center(40,'='))
print('当数据量达到上百万时，循环字典就不适合用dict.items()，因为首先会把一对对key和value转化为列表，然后在循环遍历输出，会增加内存使用。建议使用如下')
aa = {1:'a',2:'b'}
for k in aa:
    print(k,aa[k])
for k in aa.keys():
    print(k,aa[k])

##  clear(self)用于删除字典内所有元素，该函数没有任何返回值。
dic = {'k1':'v1','k2':'v2'}
print(dic)
dic.clear()
print(dic)

##  copy(self)返回一个字典的浅复制。
dic = {'k1':'v1','k1':'v2'}
print(dic.copy())
dic2 = dic.copy()
for k in dic2:
    print(k,dic2[k])

##  get(self,k,d=None)返回指定键的值，如果值不在字典中返回默认值，key--字典中要查找的键，default--如果指定键的值不存在时，返回该默认值值。
dic = {'k1':'v1','k2':'v2'}
print(dic.get('k1'))
print(dic.get('k3'),'AAA')

##  has_key(self,k)用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false，k--要在字典中查找的键。注：3.x已删除该函数

##  items(self)以列表返回可遍历的(键, 值) 元组数组。
dic = {'name':'yaoyao','age':'21','job':'IT'}
print(dic.items())
##  iteritems(self)项可迭代。注：3.x已删除该函数
##  iterkeys(self)key可迭代。注：3.x已删除该函数
##  itervalues(self)value可迭代。注：3.x已删除该函数


##  keys(self)以列表返回一个字典所有的键。
dic = {'name':'yaoyao','age':'21','job':'IT'}
print(dic.keys())

##  pop(self, k, d=None)获取并在字典中移除，k -- 要在字典中查找的键。
dic = {'name':'yaoyao','age':'21','job':'IT'}
print(dic.pop('job'))
print(dic)

##  popitem(self)获取并在字典中移除
dic = {'name':'yaoyao','age':'21','job':'IT'}
print(dic.popitem())
print(dic)

##  setdefault(self, k, d=None)如果key不存在，则创建，如果存在，则返回已存在的值且不修改
dic = {'name':'yaoyao','age':'21','job':'IT'}
dic.setdefault('sex')
dic.setdefault('name')
print(dic)

##  update(self, E=None, **F)更新
dic = {'name':'yaoyao','age':'21','job':'IT'}
dic_1 = {'sex':'man'}
dic.update(dic_1)
print(dic)

##  values(self)以列表返回字典中的所有值。
dic = {'name':'yaoyao','age':'21','job':'IT'}
vals = dic.values()
print(vals)
print("dic type:{0} ; vals type:{1}".format(type(dic),type(vals)))

##  viewitems(self)所有项，只是将内容保存至view对象中。注：3.x已删除该函数