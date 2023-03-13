#int

def bit_length(self):
    return bin(self + 12)

print(bin(10))
print(bit_length(10))

age = 21
b = 3
c = -34
print(age.__floordiv__(b))
print(age.__eq__(b))
print(c.__pos__())


# float
print("===========================float=========================")
print(float.fromhex('0x1.ffffp10'))
print(2047.984375.hex())
f1 = 10.2
f2 = 10.0
f3 = f2.__divmod__(6)
print(f1.is_integer())
print(f2.is_integer())
print(f3)
print(f1.__floordiv__(3.0))

#string
print("===========================string=========================")
name = 'ABCD ACBD DDBA DDAA'
print(name.capitalize())
print(name.center(40,'*'))
print(name.count('A',1,25))

##format(*args, **kwargs)字符串格式化
name = 'Liuyao'
name = name.casefold()  ## casefold(self)大写转小写
age = '21'
print('姓名{0},年龄{1}'.format(name,age))

name2 = '谁谁谁'
print(name2.encode('Utf-8'))

extab = 'one\ttwo'
print(extab.expandtabs())   ##expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，默认的空格数 tabsize 是
###
name3 = 'yaotwosiji'
print(name3.find('two',1,8))

zifu = 'yao1995'
print(zifu.isalnum())       ## isalnum(self)如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
zifutab = 'yao 1995'
print(zifutab.isalnum())
print(zifutab.isalpha())    ## isalpha(self)如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
print(zifutab.isdigit())    ## isdigit(self)如果字符串只包含数字则返回 True 否则返回 False
print(zifu.islower())       ## islower(self)如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回True，否则返回False
kongge = '    '
print(kongge.isspace())     ## isspace(self)如果字符串中只包含空格，则返回 True，否则返回 False
zifu = 'Liu Yao'
print(zifu.istitle())       ## istitle(self)如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False
zifu2 = 'LIU YAOv'
print(zifu2.isupper())      ## isupper(self)如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回
                            ## False
lj = '^'
name = ('y','a','o')
print(lj.join(name))        ## join(self, iterable)返回通过指定字符连接序列中元素后生成的新字符串

## ljust(self,width,fillchar=None)返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
name = 'LIUYAO'
print(name.lower())          ## lower(self)返回将字符串中所有大写字符转换为小写后生成的字符串

## lstrip(self, chars=None)返回截掉字符串左边的空格或指定字符后生成的新字符串
name = 'liuyaoliuyaoliuyao'
print(name.lstrip('liu'))

## partition(self, sep)返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串
who = 'wo shi liuyao'
print(who.partition('shi'))


## replace(self,old,new,count=None)返回字符串中的old（旧字符串)替换成new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过max次
str1 = 'ni shi wo shi shei shi'
print(str1.replace('shi','ta'))
print(str1.replace('shi','ta',1))


## split(self,sep=None,maxsplit=None)通过指定分隔符对字符串进行切片，如果参数num有指定值，则仅分隔num个子字符串
str1 = 'a1 b2 c3 d4'
print(str1.split())
print(str1.split(' ',2))

## splitlines(self, keepends=False)按照行分隔，返回一个包含各行作为元素的列表，如果num指定则仅切片num个行
str1 = '\na1b2 c3 d4'
str1 = '\na1b2\nc3\nd4\n'
print(str1.splitlines())
print(str1.splitlines(2))

## startswith(self,prefix,start=None,end=None)用于检查字符串是否是以指定子字符串开头，如果是则返回True，否则返回False。如果参数beg和end指定值，则在指定范围内检查
name = 'LIUyao'
print(name.startswith('LI'))
print(name.startswith('ya'))

## swapcase(self)用于对字符串的大小写字母进行转换
name = 'LIUyao'
print(name.swapcase())

## translate(self,table,deletechars=None)根据参数table给出的表(包含256个字符)转换字符串的字符,要过滤掉的字符放到del参数中，table翻译表，翻译表是通过maketrans方法转换而来，deletechars字符串中要过滤的字符列表。

## upper(self)将字符串中的小写字母转为大写字母
name = 'yaoyao'
print(name.upper())

## zfill(self, width)返回指定长度的字符串，width指定字符串的长度。原字符串右对齐，前面填充0。
str1 = 'a1 b2 c3 d4'
print(str1.zfill(10))
print(str1.zfill(15))


def func(*args):
    return args[0]

def func2(**args):
    return args.values