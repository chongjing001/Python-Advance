#### 1.Python关键字
```python
import keyword
print(keyword.kwlist)
>>>>
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
***
#### 2.有趣的import
```python
>>> import __hello__
Hello world!
```
***
- Python之禅
```python
In [1]: import this 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
***
```python
>>> import antigravity
```
会自动打开一个网页
![](https://img-blog.csdnimg.cn/20190421141733513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyODc0OTk0,size_16,color_FFFFFF,t_70)
***
#### 3.万物皆对象
```python
# 省略号(...)也是
In [2]: ...                                                              
Out[2]: Ellipsi
In [3]: type(...)                                                        
Out[3]: ellipsis
# 转布尔为True
In [4]: bool(...)                                                     
Out[4]: True
```
**可以使用...代替pass**
***
#### 4. and与or
如果or表达式中所有的值都为真，Python会选择第一个值
and的话，会选择最后一个
```python
>>> 5 or 6
5
>>> (True and 9)
9
```
***
#### 5.解释器提示符（>>>和...）
```python
>>> for i in range(2):
...     print(i)
... 
0
1
# 有没有想过为什么是>>>和...  ， 可不可以修改呢
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps3
>>> sys.ps1="--hello python>>> "
--hello python>>> sys.ps2 = '0**0'
--hello python>>> for i in range(2):
0**0                    print(i)
0**0
0
1
```
#### [你可能不知道的Python（二）](https://blog.csdn.net/qq_42874994/article/details/89430966)