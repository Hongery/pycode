def gen():
    print('hello')
    if 0:
        yield

g = gen()
print(g)
# <generator object gen at 0x7fc0f8092150>
print(type(gen)) # class function
print(type(g)) # generator 生成器


import inspect
#  是函数，也是生成器函数
print(inspect.isfunction(gen)) #True
print(inspect.isgeneratorfunction(gen)) #True

# 生成器函数不是generator
print(inspect.isgenerator(gen)) # False
print(inspect.isgenerator(g)) #True
