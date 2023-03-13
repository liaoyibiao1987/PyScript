
def testm2():
    print('testm2'.center(60,'='))
    import global_var
    import m2
    print('m1: before appending:          ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)
    global_var.GLOBAL_VAR.append('m1')
    print('m1: after appending:           ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)

    print('m1: before calling m2.append():', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)
    m2.append()
    print('m1: after calling m2.append(): ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)

    print('-----------------')

    print('m1: before assigning:          ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)
    global_var.GLOBAL_VAR = ['m1']
    print('m1: after assigning:           ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)

    print('m1: before calling m2.assign():', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)
    m2.assign()
    print('m1: after calling m2.assign(): ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)

def testm22():
    print('testm22'.center(60,'='))
    from global_var import GLOBAL_VAR#此种引用比较难理解，比较危险
    import m22
    print('m1: before appending:          ', id(GLOBAL_VAR), GLOBAL_VAR)
    GLOBAL_VAR.append('m1')
    print('m1: after appending:           ', id(GLOBAL_VAR), GLOBAL_VAR)

    print('m1: before calling m22.append :', id(GLOBAL_VAR), GLOBAL_VAR)
    m22.append()
    print('m1: after calling m22.append():', id(GLOBAL_VAR), GLOBAL_VAR)

    print('-----------------')

    print('m1: before assigning:          ', id(GLOBAL_VAR), GLOBAL_VAR)
    GLOBAL_VAR = ['m1']
    print('m1: after assigning:           ', id(GLOBAL_VAR), GLOBAL_VAR)

    print('m1: before calling m22.assign :', id(GLOBAL_VAR), GLOBAL_VAR)
    m22.assign() #m22模块中GLOBAL_VAR利用from global_var import GLOBAL_VAR导入，导致global GLOBAL_VAR每次调用仍然获取都的编译器第一次加载到的GLOBAL_VAR地址
    print('m1: after calling m22.assign(): ', id(GLOBAL_VAR), GLOBAL_VAR)


if __name__ == "__main__":
    #testm2()
    testm22()

    #总结使用 from global_var import GLOBAL_VAR会在模块