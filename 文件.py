# -*- coding: utf-8 -*-
#w      以写方式打开，
#a      以追加模式打开 (从 EOF 开始, 必要时创建新文件)
#r+     以读写模式打开
#w+     以读写模式打开 (参见 w )
#a+     以读写模式打开 (参见 a )
#rb     以二进制读模式打开
#wb     以二进制写模式打开 (参见 w )
#ab     以二进制追加模式打开 (参见 a )
#rb+    以二进制读写模式打开 (参见 r+ )
#wb+    以二进制读写模式打开 (参见 w+ )
#ab+    以二进制读写模式打开 (参见 a+ )
#U"      表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
#rU
#rU + 
from io import FileIO

i = FileIO("ss" ,"w")

with open("a.txt","w") as f:
    f.write("1111111111111111111")
    f.writelines("xcccccc")        #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
    f.isatty()                      #文件是否是一个终端设备文件（unix系统中的
    print(f.tell())

    #   将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，
    #   whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
    f.seek(10,0)
    f.writelines("seek(10,1)")
    f.seek(40,0)
    f.writelines("seek(40,1)")
    #返回文件操作标记的当前位置，以文件的开头为原点
    f.flush()           #把缓冲区的内容写入硬盘

#
my_lambda = lambda arg1, arg2: arg1 + arg2
print(my_lambda(11,334))


#   fp.readlines([size])
#   #其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
#   读取指定字节数据 fp.read([size]) #size为读取的长度，以byte为单位
with open("mode.txt","w+") as mode:
    varx = mode.read(2048)
    print(varx)

# 三元运算
name = 'wupeiqi' if 1 == 1 else 'alex'
print(name)
