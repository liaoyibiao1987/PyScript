sumtime = 0

def move(ls):
    global sumtime
    sumtime += 1
    print('第 %d 次移动' % sumtime)
    print("把第 %d 号盘，将 %s 移动到 %s" % ls)

def Hnuota(N,A,B,C):
    if(N == 1):
        move((1,A,C))
    else:
        Hnuota(N - 1,A,C,B)
        move((N,A,C))
        Hnuota(N - 1,B,A,C)      
#Move([1,'A','B'])
#print("".join(list(tuple([1,'A','B']))))
#Move(tuple([1,'A','B']))
Hnuota(3,'A','B','C')
print("移动完毕")



