#subprocess最早是在2.4版本中引入的。
#subprocess模块用来生成子进程，并可以通过管道连接它们的输入/输出/错误，以及获得它们的返回值。
#它用来代替多个旧模块和函数:
#os.system
#os.spawn*
#os.popen*
#popen2.*
#commands.*
#运行python的时候，我们都是在创建并运行一个进程。像Linux进程那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。
#在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序。
#subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。
#另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。

import subprocess

#call 执行命令，返回状态码 shell = True ，允许 shell 命令是字符串形式
print("call".center(40,'-'))
ret = subprocess.call(['ls','-l'],shell = True)

#check_call 执行命令，如果执行状态码是 0 ，则返回0，否则抛异常
print("check_call".center(40,'-'))
subprocess.check_call(["ls", "-l"],shell = True)

#check_output 执行命令，如果状态码是 0 ，则返回执行结果，否则抛异常
#subprocess.check_output(["echo", "Hello World!"])
#subprocess.check_output("exit 1", shell=True)
#ret = subprocess.check_output(["ls", "-l"])
print("check_output, shell=True为必须参数，【shell=True shell 命令是字符串形式】".center(40,'-'))
x = subprocess.check_output(["echo", u"Hello World!"],shell=True) 
print(x)

#subprocess.Popen(...)
#用于执行复杂的系统命令
#参数：
#args：shell命令，可以是字符串或者序列类型（如：list，元组）
#bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
#stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
#preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
#close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
#所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
#shell：同上
#cwd：用于设置子进程的当前目录
#env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
#universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
#startupinfo与createionflags只在windows下有效
#将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
print("Popen".center(40,'-'))
res = subprocess.Popen(["mkdir","sub"],shell = True)
res2 = subprocess.Popen("mkdir sub_1", shell=True)


#终端输入的命令分为两种：
#输入即可得到输出，如：ifconfig
#输入进行某环境，依赖再输入，如：python
print("open Popen".center(40,'-'))
handle = open(r'd:\tmp.log','wt')  
subprocess.Popen(['ipconfig','-all'], stdout=handle)  

from sys import stdout
from sys import stdin

#cmdline = ['cmd', '/k']
#cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#cmd.stdin.write("echo hi\n".encode('utf-8'))#would like this to be written to
#the cmd prompt
#for line in iter(cmd.stdout.readline,""):
#    print(line)
#    cmd.stdin.write("echo hi again\n")#would like this to be written to the
#    cmd prompt
pythonobj = subprocess.Popen(["python"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE,shell = True)
pythonobj.stdin.write(b"print(\"hello1\")")
pythonobj.stdin.write(b"print(\"hello2\")")
pythonobj.stdin.write(b"print(\"hello3\")")
pythonobj.stdin.write(b"print(\"hello4\")")
pythonobj.stdin.close()
 
cmd_out = pythonobj.stdout.read()
pythonobj.stdout.close()
cmd_error = pythonobj.stderr.read()
pythonobj.stderr.close()
 
print(cmd_out)
print(cmd_error)

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out_error_list = obj.communicate(b"print(\"hello\")",100)
print(out_error_list)


if "check_output" not in dir(subprocess): # duck punch it in!
 def f(*popenargs, **kwargs):
  if "stdout" in kwargs:
   raise ValueError('stdout argument not allowed, it will be overridden.')
  process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
  output, unused_err = process.communicate()
  retcode = process.poll()
  if retcode:
   cmd = kwargs.get("args")
   if cmd is None:
    cmd = popenargs[0]
   raise subprocess.CalledProcessError(retcode, cmd)
  return output
 subprocess.check_output = f