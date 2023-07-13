python pytype 是什么  
pytype是一个python代码静态类型检查工具。常用lint工具可以标记常见的错误，如拼写错误的属性名称、不正确的函数调用等等。  
Pytype是一个静态分析器；它不执行它所运行的代码。



1. 静态类型检查：Pytype可以帮助开发人员在编码阶段捕获潜在的类型错误。通过对代码进行静态分析和推断，它可以发现变量类型不匹配、函数参数错误以及其他类型相关的问题
2. 提高代码质量：静态类型检查可以提高代码的可读性和维护性。通过显式地声明变量和函数的类型，可以使代码更易于理解，并减少由于类型错误引起的bug。
3. pytype可以推理代码类型.在没有定义类型的场景下
```python
def f():
    return "PyCon"
def g():
    return f() + 2019

# pytype: line 4, in g: unsupported operand type(s) for +: 'str'
# and 'int' [unsupported-operands]
```
4. 比较宽松.在其他类型检测工具失败
```python
from typing import List
def get_list() -> List[str]:
    lst = ["PyCon"]
    lst.append(2019)
    return [str(x) for x in lst]
# mypy: line 4: error: Argument 1 to "append" of "list" has
# incompatible type "int"; expected "str"    
```

所以pytype能做哪些事情
1. 函数类型检查

2. 变量类型检查

3. 能够抑制错误  
x = a.foo  # pytype: disable=attribute-error

pytype的缺点
1. 不支持动态类型检查
```python
def unannotated(x, y):
  return " + ".join(x, y)
```
2. 不支持

3. 重写方法与被重写方法不匹配
```python
class A:
  def f(self, x: int) -> None:
    pass

class B(A):
  def f(self, x:int, y: int) -> None:  # signature-mismatch
    pass
```