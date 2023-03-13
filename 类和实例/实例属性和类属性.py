
classname2 = ''
class Student(object):
    classname = 'Student'
    def __init__(self, name):
        global classname2
        self.name = name
        classname2 = name

x = Student(r'试试')

if __name__ == '__main__':
    print(x.name)
    print(x.classname)
    print(classname2)
