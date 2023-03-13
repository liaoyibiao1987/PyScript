def MyGenerator():  
    value = yield 1  
    value = yield value  


def consumer():
    r = ''
    while True:
        #print('====' + r)
        #([yield r]整体被视为一个表达式 == send过来的值)
        # [yield r]代表send后返回到生产者数据为r
        n = yield r 
        #n = r
        #print('----' + r)
        if not n:
            print('[CONSUMER] Consuming %s...' % n)
            #return
        else:
            print('[CONSUMER] Consuming %s...receive: %s' % (n,None))
        r = '200 OK'
'''def consumer(pram):
    r = ''
    while True:
        #print('====' + r)
        n = yield print('[CONSUMER] Consuming %s...' % pram)
        #n = r
        #print('----' + r)
        if not n:
            print('====' + r)
            #return
        #print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'''
def produce(c):
    # generator 初始化时还没有被运行, 需要先next(c)或c.send(None)。开始运行之后才能 send() 
    # 下面两句必须先加 (can't send non-None value to a just-started generator)
    c.send(None)   
    #next(c) # 效果与c.send(None)雷同
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n + 9)
        r = c.send(None)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)


    #生成器对象是一个迭代器。但是它比迭代器对象多了一些方法
    #它们包括send方法，throw方法和close方法。这些方法，主要是用于外部与生成器对象的交互
    #gen = MyGenerator()  
    #print(gen.send(None))   
    #print(gen.send(33609))
    #print(gen.send(None))