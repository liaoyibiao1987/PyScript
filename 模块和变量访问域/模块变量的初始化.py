def foo(arg):
    arg = 2
    print(arg)

a = 1
foo(a)  # 输出：2
print(a) # 输出：1
##################################################################################
def bar(args):
    args.append(1)

b = []
print(b) #输出：[]
print(id(b)) # 输出：4324106952
bar(b)
print(b) #输出：[1] 执行 append 方法前 b 和 arg 都指向（绑定）同一个对象，执行 append
         #方法时，并没有重新赋值操作，也就没有新的绑定过程，append 方法只是对列表对象插入一个元素，对象还是那个对象，只是对象里面的内容变了。
print(id(b))  # 输出：4324106952

#python
#中一切皆为对象，数字是对象，列表是对象，函数也是对象，任何东西都是对象。而变量是对象的一个引用（又称为名字或者标签），对象的操作都是通过引用来完成的。例如，[]是一个空列表对象，变量
#a 是该对象的一个引用
#a = []
#a.append(1)
#在 python 中，「变量」更准确叫法是「名字」，赋值操作 = 就是把一个名字绑定到一个对象上。就像给对象添加一个标签。


#这段代码是初学者最容易犯的错误，用可变(mutable)对象作为参数的默认值。函数定义好之后，默认参数 a_list 就会指向（绑定）到一个空列表对象
#每次调用函数时，都是对同一个对象进行 append 操作。因此这样写就会有潜在的bug，同样的调用方式返回了不一样的结果。
def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list
print(bad_append('one'))
print(bad_append('one'))

#而正确的方式是，把参数默认值指定为None
def good_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list

print(good_append('one'))
print(good_append('one'))