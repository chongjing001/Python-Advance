#### 1.对私有方法的访问
```python
class A(object):
    def public(self):
        print('Hello public')
        
    def __private(self):
        print('Hello private')
    
    def call_pricate(self):
        self.__private()

a = A()
# 调用公有方法
a.public()
# 调用私有方法
a.__private()  # 报错
# 间接调用私有方法
a.call_pricate()
>>>
Hello public
Hello private

# 了解
a._A__private()
```
***
#### 2.切片的异常（不知怎么描述）
```python
list1 = [1,2,3]
print(list1[3])
# 执行会抛出索引异常
# 但执行[3：],会返回一个新list：[]
print(list1[3:])
>>>
[]
```
***
#### 3.for 死循环
想必大家都知道while死循环,那下面来讨论下for死循环
```python
for i in iter(int,1):
	pass
```
需要知道iter
- 1.将一个可迭代对象转换成迭代器
- 2.它接受一个callable对象，和一个sentinel参数，它会对第一个对象一直运行，直到返回sentinel值才结束
int() - Python内建方法，默认返回0
```python
>>> int()
0
```
**由于int()永远返回0，永远返回不了1，所有这个for循环--->死循环**
***

#### 4.for循环实现的机制
```python
list1 = [1,2,3]
for i in list1:
    print(i)
    
# list1有__iter__()方法，列表-------->可迭代对象    
its = list1.__iter__()
print(its)

print(its.__next__()) # its有__next__ ----> 迭代器
print(its.__next__())
print(its.__next__())
print(its.__next__()) # 抛出异常
>>>
1
2
3
<list_iterator object at 0x7fc580bf7860>
1
2
3
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-48-cf1fea4c7776> in <module>
      9 print(its.__next__())
     10 print(its.__next__())
---> 11 print(its.__next__())

StopIteration: 

```
1.判断对象是否是刻碟带对象，不是的话直接报错，抛出TypeError异常，是的话，调用__iter__方法，返回一个迭代器
2.不断的调用迭代器的 __next__方法，每次按顺序返回迭代器中的一个值
3.迭代到最后，没有元素时，抛出Stopiteration，Python会自己处理这个异常
```python
class MyRange:
    def __init__(self, num):
        self.i = 0
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.num:
            i = self.i
            self.i += 1
            return i
        else:
            # 达到某个条件时必须抛出此异常，否则会无止境地迭代下去
            raise StopIteration() 
            
for i in MyRange(3):
    print(i)
>>>
0
1
2
```
***
#### 5.python的小整数池
例：
```python
>>> a = -6
>>> b = -6
>>> a is b
False

>>> a = -5
>>> b = -5
>>> a is b
True

>>> a = 256
>>> b = 256
>>> a is b
True

>>> a = 257
>>> b = 257
>>> a is b
False

>>> a = 257; b = 257
>>> a is b
True

```
为了避免整数频繁的申请和销毁内存空间，python定义了一个小整数池[-5,256]这些整数对象是提前建好的，不会被垃圾回收
注意：以上代码请在Python终端下测试，如果是在IDE中，并不是这样的效果

对最后一个为True的解释：当在同一行里，同时给两个变量赋同一个值，解释器知道这个对象已经生成，那么它就会引用到同一个对象。如果分成两行的话，解释器并不知道这个对象那个已经生成了，会重新申请内存存放这个对象

#### [你可能不知道的Python（三）](https://blog.csdn.net/qq_42874994/article/details/89433399)