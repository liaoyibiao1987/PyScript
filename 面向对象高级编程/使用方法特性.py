class Student(object):
    def __init__(self, *args, **kwargs):
        self._score = 69

    @property
    def score(self):
         return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def age(self):
        return 2018 - self._score

# @score.setter 和 @property结合分别将非法作为属性来启用
#score可读可写的属性 ; age只读属性
a = Student()
#a.score = 20
print('a.score: {0} , age: {1}'.format(a.score , a.age))