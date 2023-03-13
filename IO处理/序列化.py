import pickle
import json

class 序列化(object):
    """description of class"""
    @staticmethod
    def usepickle():
        d = dict(name='Bob', age=20, score=88)
        data = pickle.dumps(d)
        print(data)

        reborn = pickle.loads(data)
        print(reborn)

        with open('dump.txt', 'wb') as output:
            pickle.dump(d, output)
        with open('dump.txt', 'rb') as input:
            d = pickle.load(input)
            print(d)
    @staticmethod
    def usejson():
        '''
            JSON类型	Python类型
            {}	dict
            []	list
            "string"	str
            1234.56	int或float
            true/false	True/False
            null	None
        '''
        d = dict(name='Bob', age=20, score=88)
        json.dumps(d)
        print(d)

        json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def student2dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'score': self.score
        }

if __name__ == "__main__":
    序列化.usepickle()
    序列化.usejson()
    s = Student('Bob', 20, 88)
    #print(json.dumps(s))
    print(json.dumps(s, default=Student.student2dict))
    print(json.dumps(s, default=lambda obj: obj.__dict__))