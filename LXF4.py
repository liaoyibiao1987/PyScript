# -*- coding: utf-8 -*-
##########################################
print("集合".center(40,'='))
print('把不同的元素组成一起形成集合，是python基本的数据类型。集合元素(set elements):组成集合的成员 \npython的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.  \nsets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作')


se = set([11,22,33,44])
print(se)
print(type(se))
se = {'liu','yao'}
print(se)
print(type(se))

lie = [1,2,3,4,5]
print(lie)
print(type(lie))

se.add('123')
print(se)

se.clear()
print(se)

##  copy(浅拷贝)
se_1 = {'liu','yao'}
se_2 = se_1.copy()
print(se_2)

##  difference差异比较
print("======difference差异比较======")
se_1 = {'liu','yao','shi','shei'}
se_2 = {'haode','shi','liu'}
print(se_1.difference(se_2))
print(se_2.difference(se_1))

##  difference_update差异更新
se_1 = {'shi', 'yao', 'liu'}
se_2 = {'shi', 'liu', 'haode'}
se_1.difference_update(se_2)
print(se_1)

##  discard移除指定元素
se_1 = {'shi', 'yao', 'shei', 'liu'}
se_1.discard('shei')
print(se_1)

##  intersection取交集并且建立新的集合
se_1 = {'liu','yao','shi','sha','bi'}
se_2 = {'liu','yao','shi','er','bi'}
print(se_1.intersection(se_2))
print(se_1)

##  intersection_update取交集并且更新原来的集合
se_1 = {'liu','yao','shi','sha','bi'}
se_2 = {'liu','yao','shi','er','bi'}
se_1.intersection_update(se_2)
print(se_1)

##  isdisjoint判断没有交集，没有返回true，有返回false
se_1 = {'liu','yao','shi','sha','bi'}
se_2 = {'liu','yao','shi','er','bi'}
print(se_1.isdisjoint(se_2))

##  issubset判断是否为子集
se_1 = {'liu','yao'}
se_2 = {'liu','yao','shabi'}
#判断se_1是否为se_2的子集
print(se_1.issubset(se_2))
#判断se_1是否为se_2的父集
print(se_1.issuperset(se_2))
#pop删除并且返回 set “se_1”中的一个不确定的元素, 如果为空则引发 KeyError
print(se_1.pop())

#remove删除指定元素集合
se_1 = {'liu','yao','sha','bi'}
se_1.remove('bi')
print(se_1)

# symmetric_difference取两个集合的差集，并建立新的元素
se_1 = {'liu','yao','sha','bi'}
se_2 = {'liu','yao','shabi'}
b = se_1.symmetric_difference(se_2)
print(b)

# symmetric_difference_update取两个集合的差集，更新原来的集合对象
se_1 = {'liu','yao','sha','bi'}
se_2 = {'liu','yao','shabi'}
se_3 = se_1.symmetric_difference_update(se_2)
print(se_1)
print(se_3)

# union并集
se_1.union(se_2)
print(se_1)

# update更新集合
se_1.update('liuyao')
print(se_1)

# 与列表和元组不同，集合是无序的，也无法通过数字进行索引。此外，集合中的元素不能重复。例如，如果检查前面代码中t集合的值，结果会是：
hello = set("Hello")
print(hello)


#   x in s
#   测试 x 是否是 s 的成员
  
#   x not in s
#   测试 x 是否不是 s 的成员
#   a = t | s # t 和 s的并集
#   b = t & s # t 和 s的交集
#   c = t – s # 求差集（项在t中，但不在s中）
#   d = t ^ s # 对称差集（项在t或s中，但不会同时出现在二者中）
#   请注意：非运算符版本的update(),intersection_update(),difference_update()和symmetric_difference_update()将会接受任意iterable作为参数。从2.3.1版本做的更改：以前所有参数都必须是sets。
#   还请注意：这个模块还包含一个union_update()方法，它是update()方法的一个别名。包含这个方法是为了向后兼容。程序员们应该多使用update()方法，因为这个方法也被内置的set()和frozenset()类型支持。


#   s.update(t)
#   s |= t
#   返回增加了 set “t”中元素后的 set “s”
     
#   s.intersection_update(t)
#   s &= t
#   返回只保留含有 set “t”中元素的 set “s”
     
#   s.difference_update(t)
#   s -= t
#   返回删除了 set “t”中含有的元素后的 set “s”
     
#   s.symmetric_difference_update(t)
#   s ^= t
#   返回含有 set “t”或者 set “s”中有而不是两者都有的元素的 set “s”

##
old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}
new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}
#获取old_dict元素
old = set(old_dict.keys())
print(old)
#获取new_dict元素
new = set(new_dict.keys())
print(new)
#要更新的集合元素（交集）
update_set = old.intersection(new)
print(update_set)
#获取要删除的集合元素（差集）
delete_set = old.difference(new)
print(delete_set)
#获取要添加的集合元素()
add_set = new.difference(update_set)
print(add_set)


# 014
# 只能修改函数内部的变量的例子:
def powerOnLocal(appleEaten):  
    print('苹果被吃了!'), # 注意,这里的逗号是为了不让<a href="http://lib.csdn.net/base/python" class='replace_word'
                     # title="Python知识库" target='_blank' style='color:#df3434;
                                         # font-weight:bold;'>Python</a>自动换行
    appleEaten = True  
# end of def
appleEaten = False  
powerOnLocal(appleEaten)  
if appleEaten == False:  
    print('哈哈!还有苹果!')
else:  
    print('呜~呜~呜~')
# 可以通过函数修改全局变量的例子:
def powerOnGlobal():  
    global appleEaten # 去到全局中抓一个叫"appleEaten"的家伙来
    print('苹果被吃了!',)
    appleEaten = True  
# end of def
powerOnGlobal()  
if appleEaten == False:  
    print('哈哈!还有苹果!')
else:  
    print('呜~呜~呜~')