import re
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。。
#re.match(pattern, string, flags=0)

#pattern 匹配的正则表达式
#string 要匹配的字符串。
#flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。


#使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
#group(num=0) 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#groups() 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
print(re.match('www', 'www.yaomr.com'))
#显示如下：
#<_sre.SRE_Match object; span=(0, 3), match='www'>
#如果要显示匹配几个字符
print(re.match('www', 'www.yaomr.com').span())
#效果：0, 3)
#如果匹配不到则返回:
print(re.match('www', 'ww.yaomr.com'))
#显示：None

#
res = re.match('\d+', '123uuasf')
if res:
    print(res.group())
else:
    print(None)
#如果匹配成功显示：
#123
#如果匹配失败：
#None


##re.search方法
#re.search 扫描整个字符串并返回第一个成功的匹配。函数语法同re.match方法
#案例1：
print(re.search('www', 'www.yaomr.com').span())  # 在起始位置匹配
print(re.search('yao', 'www.yaomr.com').span())         # 不在起始位置匹配
#返回：
obj = re.search('\d+', 'u12345uu888asf')
print(obj)

obj = re.search('\d+', r'最像考拉的动物是什么12？')
print(obj)

strS = r'01.最像考拉的动物是什么12？'
obj = re.search('(\d*)', strS)
print(obj)

text = obj.span()
print(text)

if(text[0] == 0):
    x = int(text[1])
    print(x)
    strS = strS[x:]
    print(strS)


print(type(obj.span()))

print("end".center(20,'='))
#<_sre.SRE_Match object span = (1, 4), match = '123' >
obj.group()
#'123'