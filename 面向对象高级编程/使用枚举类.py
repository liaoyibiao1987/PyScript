from enum import Enum, unique

@unique #装饰器可以帮助我们检查保证没有重复值。
class 使用枚举类(Enum):
    """description of class"""
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

if __name__ == '__main__':
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name , member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    print(使用枚举类.Mon , 使用枚举类.Mon.value)
    print(使用枚举类.Mon == 使用枚举类(1))
