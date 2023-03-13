from usemodule import testclass

class subtestclass():
    def __init__(self, newPersionName):
        self._argprotect = ""
    def test_():
        pass
    def test2_():
        return 2

if __name__ == '__main__':
    test = testclass("usemodule.testclass")
    test.test()
    test._test2protect()        ##有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
                                #当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    print(test._argprotect)

    test2_()
    print(_)
