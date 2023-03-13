from global_var import GLOBAL_VAR

def append():
    global GLOBAL_VAR

    print('m22: before append:            ', id(GLOBAL_VAR), GLOBAL_VAR)
    GLOBAL_VAR.append('m2')
    print('m22: after append:             ', id(GLOBAL_VAR), GLOBAL_VAR)

def assign():
    global GLOBAL_VAR

    print('m22: before assiging:          ', id(GLOBAL_VAR), GLOBAL_VAR)
    GLOBAL_VAR = ['m2']
    print('m22: after assiging:           ', id(GLOBAL_VAR), GLOBAL_VAR)