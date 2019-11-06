#### Python内置函数

##### `abs()`
- `abs(x)`函数返回数字x的绝对值
- `x`-- 数值表达式，可以是整数，浮点数，复数。
```python
abs(-5)
# 结果：5
```
##### `any()`与`all()`
- `all()`函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
- 元素除了是 0、空、None、False 外都算 True
- `any()`所有元素有一个为 TRUE，则返回 True
```python
# all any
print(all([0,1,1]))
print(any([0,1,1]))
```
**结果：**

```
False
True
```
##### `divmod()`
- `divmod(a,b)`获取`a/b`的商和余数
- a和b都为数字，非复数
```python
divmod(10,3)
# 结果：(3, 1)
```

##### `id()`
- `id(object)`用于获取对象的内存地址
```python
id(1)
# 结果：94066107511680
```

##### `dir()`
- `dir()` 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
- 如果参数包含方法`__dir__()`，该方法将被调用。如果参数不包含`__dir__()`，该方法将最大限度地收集参数信息
```python
print(dir()) #  获得当前模块的属性列表
print('='*50)
print(dir({})) # 查看字典的方法
```
结果：
```
['In', 'Out', '_', '_1', '_2', '_3', '_4', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i10', '_i2', '_i3', '_i4', '_i5', '_i6', '_i7', '_i8', '_i9', '_ih', '_ii', '_iii', '_oh', 'exit', 'get_ipython', 'quit']
==================================================
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

##### `iter()`和`next()`
- `iter()` 用来生成迭代器
- `next()` 返回迭代器的下一个元素
```python
l = iter([1,2,3])
next(l)
# 结果：1 
```

##### `filter()`
- `filter(function, iterable)`,function -- 判断函数,iterable -- 可迭代对象
- 用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换

```python
fil = filter(lambda x : x>10, [1,8,10,12,20]) # 获取大于10的元素
list(fil) # 转为list
# 结果：[12, 20]
```
##### `eval()`
- `eval()` 函数用来执行一个字符串表达式，并返回表达式的值
```python
a = 10
str1 = '(1+5-3)*a' # 运算
print('计算结果：',eval(str1))

str2 = '[1,2,3]'
print(f'对象转换：{eval(str2)} 类型：{type(eval(str2))}')
```
结果：
```
计算结果： 30
对象转换：[1, 2, 3] 类型：<class 'list'>
```

##### `enumerate()`
- 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中,返回 enumerate(枚举) 对象
```python
names = ['niko','lufy','marry']

for index,value in enumerate(names):
    print(f'index:{index} value:{value}')
```
结果：
```
index:0 value:niko
index:1 value:lufy
index:2 value:marry
```

##### `isinstance()`
- ` isinstance(object, classinfo)`
- 判断一个对象是否是一个已知的类型，类似 `type()`
- `type()` 不会认为子类是一种父类类型，不考虑继承关系
- ` isinstance()` 会认为子类是一种父类类型，考虑继承关系

```python
a = 1
isinstance(a,int) # True
isinstance(a,str) # False
# 是元组中的任意一个也返回True
isinstance(a,(str,int,list)) # True

# type() 与 isinstance()区别
class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    #  True
type(A()) == A        #  True
isinstance(B(), A)    #  True
type(B()) == A        # False
```

##### `zip()`
- 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存
- 可以使用 list() 转换来输出列表
- 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用` * `号操作符，可以将元组解压为列表

```python
a = [1,2,3]
b = [4,5,6]
c = ['a','b','c','d']

ab = zip(a,b) # <zip at 0x7fc418d6b248>
print(list(ab))

print(list(zip(a,c))) # 与长度最短的一致

data = zip(*zip(a,b))# 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(list(data))
```
结果：
```
[(1, 4), (2, 5), (3, 6)]
[(1, 'a'), (2, 'b'), (3, 'c')]
[(1, 2, 3), (4, 5, 6)]
```

##### `map()`
- `map(function, iterable, ...)`
- 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表

```python
nums = [1,2,3,4,5]
m = map(lambda x : pow(x,2),nums) # 对nums中的元素进行平方
print(list(m))

nums2 = [10,20,30,40,50] 

sum_num = map(lambda x,y:x+y, nums,nums2) # 提供了两个列表，对相同位置的列表数据进行相加
print(list(sum_num))
```
结果：
```
[1, 4, 9, 16, 25]
[11, 22, 33, 44, 55]
```

