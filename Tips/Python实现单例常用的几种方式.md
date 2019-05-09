### 1.最简单的，日常都在用
**import 模式，Python天然的单例模式**
```python
# mysingleton.py 中定义
class My_singleton(object):
	a = 1111
	def foo(self):
		pass
my_singleton = My_singleton()

# 在另一个py文件中导入对象my_singleton
from mysingleton import my_singleton

print(my_singleton.a)
>>>>
1111
```
***
### 2.装饰器版本
```python
def singleton(cls,*args,**kwargs):
	instance = {}
	def getinstance():
		if cls not in instance:
			instance[cls] = cls(*args,**kwargs)
		return instance[cls]
	return getinstance

@singleton
class Myclass(object):
	pass
```
***
### 3.共享属性
**创建时把所有实例的__dict__指向同一个字典，这样它们具有相同的属性和方法**
```python3
class Borg(object):
	_state = {}
	def __new__(cls,*args,**kwargs):
		ob = supper(Borg,cls).__new__(cls,*args,**kwargs)
		ob.__dict__ = cls._state
		return ob

class Myclass(Borg):
	pass

```
***
### 4.使用__new__
- **无线程安全锁**
```python3
class Singleton(object):
	def __new__(cls,*args,**kwargs):
		if not hasattr(cls,'_instance'):
			orig = super(Singleton,cls)
			cls._instance = orig.__new__(cls,*args,**kwargs)
		return cls._instance
```

***
- **有线程安全锁**
```python3
import threading
class Singleton(object):
	_instance_lock = threading.Lock()
	def __init__(self):
		pass
	def __new__(cls,*args,**kwargs):
		if not hasattr(Singleton,'_instance'):
			with Singleton._instance_lock:
				if not hasattr(Singleton,'_instance'):
					Singleton._instance = object.__new__(cls)
		return Singleton._instance

```