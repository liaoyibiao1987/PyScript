# -*- coding: utf-8 -*-
print(r"我们的家乡")

#单下划线（_）
#通常情况下，会在以下3种场景中使用：

#1、在解释器中：在这种情况下，“_”代表交互式解释器会话中上一条执行的语句的结果。这种用法首先被标准CPython解释器采用，然后其他类型的解释器也先后采用。

#Python

#>>> _ Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#NameError: name '_' is not defined
#>>> 42
#>>> _
#42
#>>> 'alright!' if _ else ':('
#'alright!'
#>>> _
#'alright!'

#2、作为一个名称：这与上面一点稍微有些联系，此时“_”作为临时性的名称使用。这样，当其他人阅读你的代码时将会知道，你分配了一个特定的名称，但是并不会在后面再次用到该名称。例如，下面的例子中，你可能对循环计数中的实际值并不感兴趣，此时就可以使用“_”。
#n = 42
#for _ in range(n):
#    do_something()
#3、国际化：也许你也曾看到”_“会被作为一个函数来使用。这种情况下，它通常用于实现国际化和本地化字符串之间翻译查找的函数名称，这似乎源自并遵循相应的C约定。例如，在Django文档“转换”章节中，你将能看到如下代码：

#Python

#from django.utils.translation import ugettext as _
#from django.http import HttpResponse
#def my_view(request):
#	output = _("Welcome to my site.")
#	return HttpResponse(output)
#可以发现，场景二和场景三中的使用方法可能会相互冲突，所以我们需要避免在使用“_”作为国际化查找转换功能的代码块中同时使用“_”作为临时名称。

' a test module '
import sys

#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
__author__ = 'pingping liao'
name = "whole global name" #模块全局变量
class testclass:
    name = "class global name"   #类全局变量
    _argprotect = "_argprotect"     #有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
                                    #当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    __argprivate = '__argprivate'   #双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
    def __init__(self, newPersionName):
        #self.name = newPersionName;
        #此处，没有使用self.name
        #而使得此处的name，实际上仍是局部变量name
        #虽然此处赋值了，但是后面没有被利用到，属于被浪费了的局部变量name
        name = newPersionName
    def test(self):
        args = sys.argv
        if len(args) == 1:
            print('Hello, world!')
        elif len(args) == 2:
            print('Hello, %s!' % args[1])
        else:
            print('Too many arguments!')
    def _test2protect(self):
        print('_test2protect is running...')
    def _private_1(self, name):
        return 'Hello, %s' % name
    def __test3private():
        print('__test3private is running...')
    if __name__ == '__main__':
        test()