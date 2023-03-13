import global_var

def append():
    print('m2: before append:             ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)
    global_var.GLOBAL_VAR.append('m2')
    print('m2: after append:              ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)

def assign():
    print('m2: before assiging:           ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)
    global_var.GLOBAL_VAR = ['m2']
    print('m2: after assiging:            ', id(global_var.GLOBAL_VAR), global_var.GLOBAL_VAR)