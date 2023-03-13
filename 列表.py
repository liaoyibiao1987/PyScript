# 022  
listNum1 = [1, 3]  
listNum2 = [2, 4]  
listStr1 = ['a', 'c']  
listStr2 = ['b', 'd']  
# 列表的合并  
list1 = listNum1 + listStr1  
for ele in list1:  
    print (ele   ) 
print ('/n'   ) 
# 判断列表中是否包含某元素  
print ('b' in list1  )
print( 1 in list1  )
# 删除某个元素  
for ele in list1:  
    print (ele  )  
del list1[1]  
for ele in list1:  
    print (ele   ) 
print ('/n'   ) 
# 对列表进行排序  
list1 = listNum1 + listNum2 + listStr1 + listStr2  
for ele in list1:  
    print (ele   ) 
print ('/n'   ) 
#list1.sort()  
for ele in list1:  
    print (ele   ) 
print ('/n'  )
# 对列表进行倒排序  
list1 = listNum1 + listNum2 + listStr1 + listStr2  
for ele in list1:  
    print (ele   ) 
print ('/n'   ) 
#list1.sort(reverse = True)  
for ele in list1:  
    print (ele   ) 
print ('/n'   ) 
# 对列表进行逆序  
list1 = listNum1 + listNum2 + listStr1 + listStr2  
for ele in list1:  
    print (ele )   
print ('/n' )   
list1.reverse()  
for ele in list1:  
    print( ele )   
print ('/n' )   
# 删除列表中连续的一部分  
list2 = listNum1 + listNum2 + listStr1 + listStr2  
list1 = list2  
#list1.sort()  
for ele in list1:  
    print( ele ) 
print ('/n' )   
del list1[0:2]  
for ele in list1:  
    print( ele  )  
print ('/n'  )  
# <a href="http://lib.csdn.net/base/python" class='replace_word' title="Python知识库" target='_blank' style='color:#df3434; font-weight:bold;'>Python</a>中列表比较的是值而不是引用  
list3 = [1, 3, 'a', 'c']  
list4 = listNum1 + listStr1  
print( list3 == list4, '/n'  )
# 列表竟然可以比较大小  
list5 = ['b', 'c']  
list6 = ['a', 'z']  
print (list5 > list6, '/n')  
# 提取元素  
list1 = listNum1 + listNum2 + listStr1 + listStr2  
print (list1   ) 
print (list1[7]   ) 
print( list1[0:4]   ) 
# 列表的拼接  
list1 = [1,2,3]  
list2 = [2,3,4]  
list1 += list2  
print (list1, '/n' )   
# 列表的翻倍  
list1 = [1,2,3]  
i = 3  
list1 *= i  
print (list1   ) 
# 添加元素的两种方法  
list1 = [1,2,3]  
list1 += [4]  
print (list1   ) 
list1 = [1,2,3]  
list1.append(4)  
print (list1   ) 
# 取得元素个数的方法  
list1 = [1,2,3]  
print (len(list1)  )  
# 取得特定元素的个数  
list1 = [1,2,2,3,4,4,4]  
print (list1.count(2)  )  
print (list1.count(4), '/n'   ) 
# 在列表中寻找特定的元素  
list1 = ['a', 'b', 'c', 'a', 'b', 'c', 'a']  
print (list1.index('a')  )  
print (list1.index('a', 1)  )  
# 在指定位置插入元素  
list1 = ['我', '爱', '你']  
for ele in list1:  
    print( ele,   ) 
print ('/n'   ) 
list1.insert(2, '不')  
list1.insert(3, '爱')  
for ele in list1:  
    print (ele,   ) 
print ('/n'   ) 
# 将最后放入的元素弹出  
list1 = ['dudu', 'gogo', 'lulu']  
print (list1   ) 
list1.pop()  
print (list1   ) 
print (list1.pop()   ) 
# 删除第一个匹配的元素  
list1 = ['dudu', 'gogo', 'lulu', 'gogo']  
print (list1 )   
list1.remove('gogo')  
print (list1 ) 