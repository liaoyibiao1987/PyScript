#import module
import os
from nt import mkdir
##从某个模块导入某个功能
#from module.xx.xx import xx
##从某个模块导入某个功能，并且给他个别名
#from module.xx.xx import xx as rename
##从某个模块导入所有
#from module.xx.xx import *

#模块分为三种：
#自定义模块
#内置模块
#开源模块

#vim moudle_test.py
#写入如下代码
#!/usr/bin/env python3

#调用
#vim test.py
#!/usr/bin/env python3
import sys
sys.path.append('模块')
sys.path.append('模块和变量访问域')

from usemodule import testclass
testc = testclass("AAAA")
print(testc._argprotect)

print('自定义 moudle')

import 子模块


print("\n\r","分割线:os模块".center(40,'-'),"\n\r")
#x = 子模块.defualtArg("11",32)
print(os.getcwd())

#os.chdir("目录名") 改变当前脚本工作目录
#os.chdir('c:/windows')

#os.curdir 返回当前目录: ('.')
os.curdir

print(os.getcwd())
#os.pardir 获取当前目录的父目录字符串名：('..')
print(os.pardir)

#os.makedirs('目录1/目录2') 可生成多层递归目录
os.makedirs('/pingpingliao/moudle/')
os.removedirs('/pingpingliao/moudle/')

#os.removedirs('目录') 若目录为空,则删除,并递归到上一级目录,如若也为空,则删除,依此类推
#>>> os.removedirs('/python/moudle')
#a目录中除了有一个b目录外，再没有其它的目录和文件。
#b目录中必须是一个空目录。 如果想实现类似rm -rf的功能可以使用shutil模块
os.makedirs('/a/b')
os.removedirs('/a/b')

#os.mkdir('目录') 生成单级目录；相当于shell中mkdir 目录
os.mkdir('/python')

#os.rmdir('目录') 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir
os.rmdir('/python')

#os.listdir('目录') 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.listdir('/windows'))

#os.remove()删除一个文件
#os.rename("原名","新名") 重命名文件/目录
#os.stat('path/filename') 获取文件/目录信息
print(os.stat('c:/windows/iis7.log'))
#os.sep 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.sep)
#os.linesep 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.linesep)
#os.pathsep 输出用于分割文件路径的字符串
print(os.pathsep)
#os.name 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.name)
#os.system("pwd") 运行shell命令，直接显示
#os.system('cmd')
#os.environ 操作系统环境变量
print(os.environ)


print("\n\r","分割线:path模块".center(40,'-'),"\n\r")
#path
path = "c:\\windows\system32"
#os.path模块主要用于文件的属性获取，
print(os.path.abspath(path)) #返回path规范化的
print(os.path.split(path)) #将path分割成目录和文件名二元组返回
print(os.path.dirname(path)) #返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(path))
#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists(path)) #如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs(path)) #如果path是绝对路径，返回True
print(os.path.isfile(path)) #如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir(path)) #如果path是一个存在的目录，则返回True。否则返回False
#os.path.join(path1[, path2[, ...]]) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime(path)) #返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime(path)) #返回path所指向的文件或者目录的最后修改时间


print("\n\r","分割线:sys模块".center(40,'-'),"\n\r")
#sys模块 用于提供对解释器相关的操作
sys.argv   #命令行参数List，第一个元素是程序本身路径
sys.modules #返回系统导入的模块字段，key是模块名，value是模块
#sys.exit(8)        #退出程序，正常退出时exit(0)
print(sys.version)        #获取Python解释程序的版本信息
print(sys.maxsize)         #最大的Int值
print(sys.path)           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)       #返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
print(sys.modules.keys()) #返回所有已经导入的模块名
print(sys.modules.values()) #返回所有已经导入的模块
print(sys.exc_info())     #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
#sys.exit(0)        #退出程序，正常退出时exit(0)
print(sys.hexversion)     #获取Python解释程序的版本值，16进制格式如：0x020403F0
print(sys.version)        #获取Python解释程序的
print(sys.api_version)   #解释器的C的API版本
print(sys.version_info)    #‘final’表示最终,也有’candidate’表示候选，serial表示版本级别，是否有后继的发行
print(sys.displayhook("print") )     #如果value非空，这个函数会把他输出到sys.stdout，并且将他保存进__builtin__._.指在python的交互式解释器里，’_’ 代表上次你输入得到的结果，hook是钩子的意思，将上次的结果钩过来
print(sys.getdefaultencoding())    #返回当前你所用的默认的字符编码格式
print(sys.getfilesystemencoding()) #返回将Unicode文件名转换成系统文件名的编码的名字
#print(sys.setdefaultencoding(""))#用来设置当前默认的字符编码，如果name和任何一个可用的编码都不匹配，抛出 LookupError，这个函数只会被site模块的sitecustomize使用，一旦别site模块使用了，他会从sys模块移除
print(sys.builtin_module_names)    #Python解释器导入的模块列表
print(sys.executable)              #Python解释程序路径
print(sys.getwindowsversion())     #获取Windows的版本
print(sys.copyright)               #记录python版权相关的东西
print(sys.byteorder)      #本地字节规则的指示器，big-endian平台的值是’big’,little-endian平台的值是’little’
#print(sys.exc_clear())    #用来清除当前线程所出现的当前的或最近的错误信息
print(sys.exec_prefix)    #返回平台独立的python文件安装的位置
print(sys.stderr)         #错误输出
print(sys.stdin)          #标准输入
print(sys.stdout)         #标准输出
print(sys.platform)       #返回操作系统平台名称
print(sys.path)           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.maxunicode)     #最大的Unicode值
#print(sys.maxint)         #最大的Int值
print(sys.version)        #获取Python解释程序的版本信息
print(sys.hexversion)     #获取Python解释程序的版本值，16进制格式如：0x020403F0




