try:
    with open("myfile.txt",mode="a+") as f:
        for i in range(65535):
            f.write("AAAA\n")
        for line in f:
            print(line, end="")
    raise NameError("java, C#")
except Exception as err:
    print(type(err)) # the exception instance
    print(err.args) # arguments stored in .args
    print(err)
    #raise
except NameError as err2:
    print("跳过")
    pass
finally:
    print("跳过错误")
    pass


from functools import reduce
import logging
import math
logging.basicConfig(filename="config.log",filemode="w",format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",level=logging.INFO)


def str2int(val):
    if val.isdigit:
        ret = int(val)
        assert (not(math.isnan(ret)) and ret > 0), '转换失败'  #凡是用print()来辅助查看的地方，都可以用断言（assert）来替代 assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
                                                              #如果断言失败，assert语句本身就会抛出AssertionError：
        return ret
    else:
        raise ValueError
def calc(exp):
    ss = exp.split('+')
    #ns = map(lambda x: int(x), ss)
    ns = map(str2int , ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    print('100 + 200 + 345 =', calc('100 + 200 + 345'))
    print('99 + 7.6 + 88 =', calc('99 + 7.6 + 88'))

if (__name__ == "__main__"):
    try:
        main()
    except Exception as ex:
        logging.exception(ex)
        logging.error(ex)
    finally:
        print("OVER".center(30,'='))
