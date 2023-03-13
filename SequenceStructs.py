
#coding=utf-8
# -*- coding: UTF-8 -*-       只能放在所有代码的开始的第一行第一列

#lee = ['tell me way','yes I will tell to you']
#johon = ['how are you','you are so crazy']

#arrlist = [lee,johon]
#print arrlist

#print arrlist[0]


#teststr = 'When something has happen, Don\'t do anything'
#print teststr[-1]
#for x in teststr:
#    print '--' + x

#-----------------------------------------------------------------------------------------
#yearStr = raw_input('please input a year:')[2:4]
#yearStr = yearStr[1]
#print yearStr


#months = ['January',
#	'February',
#	'March',
#	'April',
#	'May',
#	'June',
#	'July',
#	'August',
#	'September',
#	'October',
#	'November',
#	'December']

#endings = ['st','nd','rd'] + 17 * ['th'] \
#		+ ['st','nd','rd'] + 7 * ['th'] \
#		+ ['st']
#year = raw_input('year :')

#month = raw_input('Month :')

#day = raw_input('day :')

#monthnumber = int(month) - 1
#daynumber = int(day) - 1

#monthname = months[monthnumber]
#ordinal = day + endings[daynumber]

#print monthname + ' ' + ordinal + ',' + year
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
#tags = 'I have a dream that one day every valley shall be exalted, ' \
# 'and every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight; \"and the glory of the Lord shall be revealed and all flesh shall see it together.\"?'
tags = '123456789' \
 'ABCDEFGHIJKLMN'

print (tags[0: -10])	# index 0 - (end - 10)  ->  asc
print (tags[10:])	# index 10 - end  ->  asc
print (tags[-1:])
print (tags[-1:3] )
print (tags[20 : 5: -2]) # index 5 - 20  ->  desc step = 2
print( tags[20 : 0: -2]) # 5 - 10 


#name  = list('z_index')
#print name
#del name[2:4]
#print name

#name[2:4] = list('Hoooooo')
#print name

#name[1:] = []
#print name

#name.append('some append')
#print name
#print name.count('some append')
#print name.count([0,4])
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
#sentence = raw_input('sentecn: ')
#screenwidth = 102
#textwidth = len(sentence)
#boxwidth = textwidth + 6
#leftmargin = (screenwidth - boxwidth) // 2

#print ' ' * leftmargin + '+' + '-' * (boxwidth - 2) + '+'
#print ' ' * leftmargin + '|  ' + ' ' * textwidth + '  |'
#print ' ' * leftmargin + '|  ' + sentence + '  |'
#print ' ' * leftmargin + '|  ' + ' ' * textwidth + '  |'
#print ' ' * leftmargin + '+' + '-' * (boxwidth - 2) + '+'
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
#prmission = 'some people'
#print 's' in prmission
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
#database = [['tom','1002'],
#    ['sam','1003'],
#    ['thomas','1004'],
#    ['thompson','1005'],]
#username = raw_input('user name :')
#paswd = raw_input('password :')

#if [username , paswd] in database :
#    print 'Access granted'
#else
#    print 'Access defend'
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
#number = [1,20,330,100]
#print str(max(number)) + str(min(number))

#a = [1,2,3]
#b = [4,5,6]

#a.extend(b)
#print a

#del a[3:]
#print a

#a[len(a):] = b
#print a

##print a.index(5) # + a.index(20)
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
#numbers = [1,2,3,4]
#numbers.insert(3,'hours')
#print numbers

##numbers = [1,2,3,4,5,6,7]                 #numbers = ['1','2','3','4']
##numbers[3,3] = 'four'
##print numbers
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
#---queue
#numbers = [1,2,3,4,5,6,7]
#listappend = list([8,9,10,11])
#numbers.append(listappend)
#print numbers.pop()
#print numbers.pop(3)
#print numbers


##---stack
#numbers = [1,2,3,4,5,6,7]
#listappend = list([8,9,10,11])
#numbers.insert(0,listappend)
#print numbers.pop()
#print numbers
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
## remove
#numbers = [1,2,3,-4,5,-6,7]
#numbers.remove(3)
#print numbers

## reverse
#numbers.reverse()
#print numbers
#print list(reversed(numbers))

## sort
#numbers2 = numbers # reference transmission
#numbers2.sort()
#print numbers

#numbers2 = numbers[:] # object clone
#numbers2.sort()
#print numbers

#numbers2 = sorted(numbers) # Does not affect the original data
#print numbers
#print numbers2

#numbers.sort(reverse = False)
#print numbers
#numbers.sort(reverse = True)
#print numbers

#numbers2 = numbers.sort() # waring ->error operating
#print numbers
#print numbers2 == None
#print numbers2 == 'None'
#print numbers2 is None


#numbers = ['1','2','hey','andy lau','70','3000']
#numbers.sort(key = len) # Does not affect the original data
#print numbers

#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
hongxing = 1,2,3,5
print(hongxing)
hongxing = (20,0)
print(hongxing)

print(2 * (80 + 1))
print(2 * (80 , 1 ,))

hongxing = (1,2,3,4)
#hongxing[1] = 6 #----'tuple' object does not support item assignment
print(hongxing.__str__())
print(list(hongxing))
#-----------------------------------------------------------------------------------------

#----------------列表可以修改，元组(不可变)不能。--------------------------------------------
#----------------哪些地方需要使用元组-------------------------------------------------------
#----------------元组可以在映射(和集合的成员)中作为键(key)使用，而列表不行---------------------
#----------------元组作为很多内建函数和方法的返回值存在---------------------------------------
 

#1、字典
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}

#字典转为字符串，返回：<type 'str'> {'age': 7, 'name': 'Zara', 'class': 'First'}
print(type(str(dict)), str(dict))

#字典可以转为元组，返回：('age', 'name', 'class')
print(tuple(dict))
#字典可以转为元组，返回：(7, 'Zara', 'First')
print(tuple(dict.values()))

#字典转为列表，返回：['age', 'name', 'class']
print(list(dict))
#字典转为列表
print(dict.values)

#2、元组
tup = (1, 2, 3, 4, 5)

#元组转为字符串，返回：(1, 2, 3, 4, 5)
print(tup.__str__())

#元组转为列表，返回：[1, 2, 3, 4, 5]
print(list(tup))

#元组不可以转为字典

#3、列表
nums = [1, 3, 5, 7, 8, 13, 20]

#列表转为字符串，返回：[1, 3, 5, 7, 8, 13, 20]
print(str(nums))

#列表转为元组，返回：(1, 3, 5, 7, 8, 13, 20)
print(tuple(nums))

#列表不可以转为字典

#4、字符串

#字符串转为元组，返回：(1, 2, 3)
print(tuple(eval("(1,2,3)")))
#字符串转为列表，返回：[1, 2, 3]
print(list(eval("(1,2,3)")))
#字符串转为字典，返回：<type 'dict'>
print(type(eval("{'name':'ljq', 'age':24}")))
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------