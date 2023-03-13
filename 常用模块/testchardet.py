import chardet

def test1():
    print(chardet.detect(b'Hello, world!'))
def test2():
    data = '离离原上草，一岁一枯荣'.encode('gbk')
    print(chardet.detect(data))

def test3():
    data = '最新の主要ニュース'.encode('euc-jp')
    print(chardet.detect(data))




if __name__ == '__main__':
    test3()