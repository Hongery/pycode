# 定义一个生成器函数
from msilib.schema import Class


def gen(meet_yield):
    print('hello')
    if meet_yield:
        print('yield')
        yield 666
        print('back')
    print('bye')
    return 'result'

g1 = gen(False)

x1 = next(g1)
print(x1)
# hello
# bye
# execption stop Iteration

g2 = gen(True)

x2 = next(g2)
print(x2)
# hello
# yield
# 666

# 为数据实现__iter_接口
class MyCustomDataIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index < self.data.size:
            return self.data.get_value(self.index)
        else:
            raise StopIteration

# 可迭代数据类
class MyCustomData:
    @property
    def size(self): #假设数据大小
        return self.size
    
    def get_value(self, index): # 假设通过索引得到数据
        return index
    
    def __iter__(self):
        return MyCustomDataIterator(self)# 构建迭代器