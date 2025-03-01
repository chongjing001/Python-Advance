## **`__slots__` 优化内存记录**

>`__slots__` 是一个类属性，用于指定实例可以拥有的属性名称。通过使用 `__slots__`，Python 会为实例分配固定的内存空间来存储属性，而不是使用 `__dict__` 字典。



```python
class MyClass:
    __slots__ = ['x', 'y']  # 声明实例只能有 x 和 y 两个属性

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1, 2)
print(obj.x)  # 输出: 1
print(obj.y)  # 输出: 2
```

- **优点**：

  1**减少内存占用**：实例不再需要 `__dict__` 字典，节省了内存。
  2**提高访问速度**：属性访问速度更快，因为属性存储在一个固定大小的数组中，而不是字典中。

- **缺点**：

  1**灵活性降低**：不能动态添加未在 `__slots__` 中声明的属性。
  2**继承限制**：如果子类没有定义 `__slots__`，它会恢复使用 `__dict__`，从而失去内存优化效果。

  

### 比对

- **默认情况**：每个实例都有一个 `__dict__` 字典，字典本身会占用额外的内存（存储键值对、哈希表等）。
- **使用 `__slots__`**：实例的属性存储在一个固定大小的数组中，数组的每个槽位对应一个属性。这种方式避免了字典的开销。

```python
import sys

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = WithoutSlots(1, 2)
obj2 = WithSlots(1, 2)

print(sys.getsizeof(obj1))  # 输出: 56（默认情况下）
print(sys.getsizeof(obj2))  # 输出: 48（使用 __slots__ 后）
```

