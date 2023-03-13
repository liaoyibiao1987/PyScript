class Integer(int): 
   name = 'my integer'
 
   def increase(self, num):
       return num + 1
 
# -------------------
#和 dict 类似，type 也是一个工厂构造函数，调用其将返回 一个type类型的实例（即 类）。
Integer2 = type('Integer2', (int,), {
   'name': 'my integer',
   'increase': lambda self, num: 
                   num + 1    # 很酷的写法，不是么
    })

Integer3 = IntMeta('Integer3', (int,), {})

print(Integer2.increase(None,3))

i1 = Integer()
print(i1.increase(3))