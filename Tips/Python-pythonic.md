### 数据算法和结构



#### 通过公共键对字典列表排序

- 根据一个或多个字典中的值来对列表排序

```python
users = [
    {'name':'jack','age':25,'height':180},
    {'name':'amor','age':23,'height':177},
    {'name':'niko','age':45,'height':169},
    {'name':'lops','age':20,'height':168},
    {'name':'fdop','age':33,'height':189},
    {'name':'bon','age':22,'height':168},
    {'name':'rom','age':26,'height':166},
    {'name':'gogo','age':18,'height':177},
]
```



```python
# 通过公共列age排序，反序的话添加reversed=True
sort_by_age = sorted(users,key=lambda x:x['age'])
print(sort_by_age)

# 输出
[{'name': 'gogo', 'age': 18, 'height': 177},
 {'name': 'lops', 'age': 20, 'height': 168},
 {'name': 'bon', 'age': 22, 'height': 168},
 {'name': 'amor', 'age': 23, 'height': 177},
 {'name': 'jack', 'age': 25, 'height': 180},
 {'name': 'rom', 'age': 26, 'height': 166},
 {'name': 'fdop', 'age': 33, 'height': 189},
 {'name': 'niko', 'age': 45, 'height': 169}]
```



> `operator`模块中的`itemgetter`
>
> `itemgetter()`通常要比`lambda`要快一些

```python
from operator import itemgetter
sort_by_age = sorted(users,key=itemgetter('age'))
# 结果和上面完全一样

# 接受多个
by_height_age = sorted(users,key=itemgetter('height','age'))
print(by_height_age)
# 输出
[{'name': 'rom', 'age': 26, 'height': 166},
 {'name': 'lops', 'age': 20, 'height': 168},  # height相同再通过age排序
 {'name': 'bon', 'age': 22, 'height': 168},
 {'name': 'niko', 'age': 45, 'height': 169},
 {'name': 'gogo', 'age': 18, 'height': 177}, 
 {'name': 'amor', 'age': 23, 'height': 177}, 
 {'name': 'jack', 'age': 25, 'height': 180}, 
 {'name': 'fdop', 'age': 33, 'height': 189}]
```



- 同样也支持`max`和`min`函数

```python
# 获取height最大的
max(users,key=itemgetter('age'))
```



- 取出序列中的前几个或后几个

> `heapq`模块中的`nlargest`和`nsmallest`

```python
from heapq import nlargest,nsmallest
from operator import itemgetter

# 简单序列
nums = [21,1,546,6,269,236,344,56,3]

# 最大三个
print(nlargest(3,nums))

# 最小三个
print(nsmallest(3,nums))

# 输出
[546, 344, 269]
[1, 3, 6]


# 复杂序列，就用上面的users

# 年龄最大三人
# sort_age = nlargest(3,users, key=lambda a: a['age'])
sort_age = nlargest(3,users, key=itemgetter('age'))
print(sort_age)

# 最矮三人
sort_height = nsmallest(3, users, key=itemgetter('height'))
print(sort_height)

# 输出
[{'name': 'niko', 'age': 45, 'height': 169},
 {'name': 'fdop', 'age': 33, 'height': 189},
 {'name': 'rom', 'age': 26, 'height': 166}]

[{'name': 'rom', 'age': 26, 'height': 166},
 {'name': 'lops', 'age': 20, 'height': 168},
 {'name': 'bon', 'age': 22, 'height': 168}]

```

