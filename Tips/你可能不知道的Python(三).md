#### 1.交互式操作符"_"
对于_,都这样用过吧
1.变量取名好难，用_
2.长长的变量，用_
3.无用的垃圾变量，用_

说一下他在交互式中的使用
```python
>>> 1 + 2
3
>>> _
3
>>> name = 'abc'
>>> name
'abc'
>>> _
'abc'
```
>他可以返回上一次的运行结果
但如果是print打印出来的就不行
```python
>>> print(100)
100
>>> _
'abc'
```
#### 2.
```python
# __repr__和 __str__
>>> class Test(object):
...     def __str__(self):
...             return 'hello str'
...     def __repr__(self):
...             return 'hello repr'
... 
>>> t = Test()
>>> t
hello repr
>>> print(t)
hello str
>>> _
hello repr

```
***
#### 3. 一行代码搭建FTP服务器
搭建FTP，或者搭建网络文件系统，实现Linux目录共享。
但FTP和网络文件系统的功能都过于强大，因此都有一些不够方便的地方
如何快速搭建共享目录呢？
Python2使用SimpleHTTPServer，SimpleHTTPServer是Python2自带的一个模块，是Python的web服务器。它在python3中已经合并到http.server模块中
若不指定端口，默认为8000端口
```python
# python2
python -m SimpleHTTPServer 9000
# python3
(base) tj001@t-Ubuntu:~$ python3.6 -m http.server 9000
Serving HTTP on 0.0.0.0 port 9000 (http://0.0.0.0:9000/) ...

```
![](https://img-blog.csdnimg.cn/20190421144813989.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyODc0OTk0,size_16,color_FFFFFF,t_70)
#### 4.else（for else  和 try else）
>for else
```python
def test(list1,item):
    for i in list1:
        if i == item:
            print('Break')
            break
    else:
        print('Dose not exist')
test([1,2,3],2)
test([1,2,3],4)
>>>>
Break
Dose not exist	
```
**循环正常结束(没有经过break)才会走else**
>try  else
```python
def test_try(a=None):
    try:
        if a:
            pass
        else:
            raise
    except:
        print('Exception')
    else:
        print('No Exception')

# 不传参时        
test_try()
# 传参
test_try(100)
>>>>
Exception
No Exception
```
#### 5.负负得正
正如以毒攻毒一样
>python作为一门高级语言，他的编写符合人类的思维逻辑，这其中也包括了
>负负得正这个思想
```pyhton
>>> 8--4
12
>>> 5+-4
1
>>> 5++4
9
>>> 5---4
1
>>> 

```
