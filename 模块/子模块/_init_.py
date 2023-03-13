class Person:  
    population = 0 #这个变量是属于整个类的  
    def __init__(self, name):  
        self.name = name  
        print ('初始化 %s' % self.name  )
        Person.population += 1  
    # end of def  
    def __del__(self):  
        print ('%s says bye.' % self.name  )
        Person.population -= 1  
        if Person.population == 0:  
            print ('我是最后一个人了！'  )
        else:  
            print ('还有%d个人。' % Person.population  )
        # end of if  
    # end of def  
    def sayHi(self):  
        print ('Hi, my name is %s' % self.name  )
    # end of def  
    def howMany(self):  
        print( Person.population ) 
    # end of def  
# enf of class  
ning = Person('Ning')  
ning.sayHi()  
ning.howMany()  


while True:  
    try:  
        x = int(raw_input('Input a number:'))  
        y = int(raw_input('Input a number:'))  
        z = x / y  
    except (ValueError, ev):  
        print ('That is not a valid number.', ev ) 
    except( ZeroDivisionError, ez):  
        print ('Divisor is zero:', ez)  
    except:  
        print ('Unexpected error.')  
        raise  
    else:  
        print ('There is no error.' ) 
        break 
    finally:  
        print('Closed the file.'  )
    # end of try  
# end of while  
print (x,'/',y,'=',x/y)  