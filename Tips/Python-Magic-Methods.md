## Python 中的**魔术方法（Magic Methods）**

> 也称为**特殊方法（Special Methods）\**或\**双下方法（Dunder Methods）**，是以双下划线（`__`）开头和结尾的方法。它们用于定义类的行为，例如对象的创建、操作、比较、字符串表示等



## 1. **对象创建与初始化**

### （1）`__new__`

- 用于创建类的实例（对象）。
- 在 `__init__` 之前调用。
- 通常用于不可变类型或单例模式。

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        instance = super().__new__(cls)
        return instance
```



### （2）`__init__`

- 用于初始化对象的属性。
- 在对象创建后调用。

```python
class MyClass:
    def __init__(self, value):
        self.value = value
```



## 2. **对象的字符串表示**

### （1）`__str__`

- 定义对象的“非正式”字符串表示，通常用于用户友好的输出。
- 由 `str()` 和 `print()` 调用。

```python
class MyClass:
    def __str__(self):
        return "MyClass instance"
```

### （2）`__repr__`

- 定义对象的“正式”字符串表示，通常用于调试和开发。
- 由 `repr()` 调用，如果没有定义 `__str__`，`print()` 也会调用 `__repr__`。

```python
class MyClass:
    def __repr__(self):
        return "MyClass()"
```



## 3. **对象的比较**

### （1）`__eq__`

- 定义 `==` 操作符的行为。

```python
class MyClass:
    def __eq__(self, other):
        return isinstance(other, MyClass)
```

### （2）`__lt__`

- 定义 `<` 操作符的行为。

```python
class MyClass:
    def __lt__(self, other):
        return self.value < other.value
```

### （3）`__gt__`、`__le__`、`__ge__`、`__ne__`

- 分别定义 `>`、`<=`、`>=`、`!=` 操作符的行为。



## 4. **对象的数学运算**

### （1）`__add__`

- 定义 `+` 操作符的行为。

```python
class MyClass:
    def __add__(self, other):
        return self.value + other.value
```

### （2）`__sub__`、`__mul__`、`__truediv__`、`__floordiv__`、`__mod__`

- 分别定义 `-`、`*`、`/`、`//`、`%` 操作符的行为。

### （3）`__iadd__`、`__isub__`、`__imul__` 等

- 定义 `+=`、`-=`、`*=` 等增量赋值操作符的行为。



## 5. **对象的容器行为**

### （1）`__len__`

- 定义 `len()` 函数的行为。

```python
class MyList:
    def __len__(self):
        return 10
```

### （2）`__getitem__`

- 定义通过索引访问元素的行为（如 `obj[key]`）。

```python
class MyList:
    def __getitem__(self, index):
        return index * 2
```

### （3）`__setitem__`

- 定义通过索引设置元素的行为（如 `obj[key] = value`）。

```python
class MyList:
    def __setitem__(self, index, value):
        print(f"Setting {index} to {value}")
```

### （4）`__contains__`

- 定义 `in` 操作符的行为。

```python
class MyList:
    def __contains__(self, item):
        return item in [1, 2, 3]
```



## 6. **对象的上下文管理**

### （1）`__enter__`

- 定义 `with` 语句进入时的行为。

```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
```

### （2）`__exit__`

- 定义 `with` 语句退出时的行为。

```python
class MyContext:
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
```



## 7. **对象的调用行为**

### （1）`__call__`

- 定义对象被调用时的行为（如 `obj()`）。

```python
class MyCallable:
    def __call__(self):
        print("Called!")
```



## 8. **对象的属性访问**

### （1）`__getattr__`

- 定义访问不存在的属性时的行为。

```python
class MyClass:
    def __getattr__(self, name):
        return f"Attribute {name} not found"
```

### （2）`__setattr__`

- 定义设置属性时的行为。

```python
class MyClass:
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)
```

### （3）`__delattr__`

- 定义删除属性时的行为。

```python
class MyClass:
    def __delattr__(self, name):
        print(f"Deleting {name}")
        super().__delattr__(name)
```



## 9. **对象的迭代行为**

### （1）`__iter__`

- 定义对象的迭代行为。

```python
class MyIterable:
    def __iter__(self):
        return iter([1, 2, 3])
```

### （2）`__next__`

- 定义迭代器的下一个值。

```python
class MyIterator:
    def __next__(self):
        if not hasattr(self, "count"):
            self.count = 0
        self.count += 1
        if self.count > 3:
            raise StopIteration
        return self.count
```