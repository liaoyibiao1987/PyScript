from io import StringIO
from io import BytesIO

class do_str_byte(object):
    """description of class"""
    @staticmethod
    def TestString():
        f = StringIO()
        print(f.write('hello'))
        f.write(' ')
        print(f.write('world!'))
        print(f.getvalue())
    
    @staticmethod
    def TestByte():
        f = BytesIO(b'\xff\xb8\xad\xe6\x96\xfe')
        f.write('中文'.encode('utf-8'))
        print(f.getvalue())
        f.read()

if __name__ == '__main__':
    do_str_byte.TestString()
    do_str_byte.TestByte()