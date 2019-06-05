##### ORM简介

- ORM概念
  
  对象关系映射（Object Relational Mapping，简称ORM）模式是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术。
  
  简单的说，ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系数据库中。
  
  ORM在业务逻辑层和数据库层之间充当了桥梁的作用

- ORM由来
  
  让我们从O/R开始。字母O起源于"对象"(Object),而R则来自于"关系"(Relational)。
  
  几乎所有的软件开发过程中都会涉及到对象和关系数据库。在用户层面和业务逻辑层面，我们是面向对象的。当对象的信息发生变化的时候，我们就需要把对象的信息保存在关系数据库中。
  
  按照之前的方式来进行开发就会出现程序员会在自己的业务逻辑代码中夹杂很多SQL语句用来增加、读取、修改、删除相关数据，而这些代码通常都是重复的。

- ORM的优势
  
  ORM解决的主要问题是对象和关系的映射。它通常把一个类和一个表一一对应，类的每个实例对应表中的一条记录，类的每个属性对应表中的每个字段。 
  
  ORM提供了对数据库的映射，不用直接编写SQL代码，只需像操作对象一样从数据库操作数据。
  
  让软件开发人员专注于业务逻辑的处理，提高了开发效率

- ORM的劣势
  
  ORM的缺点是会在一定程度上牺牲程序的执行效率。
  
  ORM用多了SQL语句就不会写了，关系数据库相关技能退化...

- ORM总结
  
  ORM只是一种工具，工具确实能解决一些重复，简单的劳动。这是不可否认的。
  
  但我们不能指望某个工具能一劳永逸地解决所有问题，一些特殊问题还是需要特殊处理的。
  
  但是在整个软件开发过程中需要特殊处理的情况应该都是很少的，否则所谓的工具也就失去了它存在的意义

##### ORM中的Model

**在Django中model是你数据的单一、明确的信息来源。它包含了你存储的数据的重要字段和行为。通常，一个模型（model）映射到一个数据库表**
每个模型都是一个Python类，它是django.db.models.Model的子类。
模型的每个属性都代表一个数据库字段

![5cf787fc5212844626](https://i.loli.net/2019/06/05/5cf787fc5212844626.png)

**1.字段类型**

```python
from django.db import models

class Person(models.Model):
    # Django会在数据库中自动创建一个列名为id且自增的整数列
    # 也可以自定义
    # z_id = models.AutoField(primary_key=True)  # 此处为自定义
    name = models.CharField(max_length=10)
    age = models.IntegerField()
```

- 主外键
  
  - `AutoField(Field)`:int自增列，必须填入参数 primary_key=True
  
  - `BigAutoField(AutoField)`:bigint自增列，必须填入参数 primary_key=True
  
  - `ForeignKey()`:定义外键
  
  - `OneToOneField()`:一对一字段
  
  - `ManyToManyField()`:多对多字段

- 数字
  
  - `IntegerField(Field)`:整数列(有符号的) -2147483648 ～ 2147483647
  - `SmallIntegerField(IntegerField)`:小整数 -32768 ～ 32767
  - `PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)`: 正整数 0 ～ 2147483647
  - `PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)`:正小整数 0 ～ 32767
  - ` BigIntegerField(IntegerField)`:长整型(有符号的) -9223372036854775808 ～ 9223372036854775807
  - `DurationField(Field)`:长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型
  - `FloatField(Field)`:浮点型
  - `DecimalField(Field)`:
    - 10进制小数
    - 参数：
      - max_digits，小数总长度
      - decimal_places，小数位长度
  - `BinaryField(Field)`:二进制类型

- 布尔
  
  - `BooleanField(Field)`:布尔值类型
  - `NullBooleanField(Field)`:可以为空的布尔值

- 字符串
  
  - `CharField(Field)`
    - 字符类型
    - 必须提供max_length参数， max_length表示字符长度
  - `TextField(Field)`:文本类型
  - `EmailField(CharField)`:字符串类型，Django Admin以及ModelForm中提供验证机制
  - `IPAddressField(Field)`:字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制
  - `GenericIPAddressField(Field)`
    - 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
    - 参数：
      - protocol，用于指定Ipv4或Ipv6， 'both',"ipv4","ipv6"
      - unpack_ipv4， 如果指定为True，则输入::ffff:192.0.2.1时候，可解析为192.0.2.1，开启刺功能，需要protocol="both"
  - `URLField(CharField)`:字符串类型，Django Admin以及ModelForm中提供验证 URL
  - `SlugField(CharField)`:字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）
  - `CommaSeparatedIntegerField(CharField)`:字符串类型，格式必须为逗号分割的数字
  - `UUIDField(Field)`:字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证
  - `FilePathField(Field)`
    - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
    - 参数：
      - path,                      文件夹路径
      - match=None,                正则匹配
      - recursive=False,           递归下面的文件夹
      - allow_files=True,          允许文件
      - allow_folders=False,       允许文件夹
  - `FileField(Field)`:
    - 字符串，路径保存在数据库，文件上传到指定目录
    - 参数：
      - upload_to = ""      上传文件的保存路径
      - storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
  - `ImageField(FileField)`:
    - 字符串，路径保存在数据库，文件上传到指定目录
    - 参数
      - upload_to = ""      上传文件的保存路径
      - storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
      - width_field=None,   上传图片的高度保存的数据库字段名（字符串）
      - height_field=None   上传图片的宽度保存的数据库字段名（字符串）

- 日期和时间
  
  - `DateTimeField(DateField)`:日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
  - `DateField(DateTimeCheckMixin, Field)`:日期格式      YYYY-MM-DD
  - `TimeField(DateTimeCheckMixin, Field)`:时间格式      HH:MM[:ss[.uuuuuu]]

**2.字段参数**

- `null`:数据库中字段是否可以为空

- `db_column`:数据库中字段的列名

- `db_tablespace`:自定义数据库表空间的名字。默认值是工程的DEFAULT_TABLESPACE设置

- `default`:数据库中字段的默认值

- `primary_key`:数据库中字段是否为主键

- `db_index`:数据库中字段是否可以建立索引

- `unique`:数据库中字段是否可以建立唯一索引

- 时间字段独有
  
  - `auto_now_add`:配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库
  - `auto_now`:配置上auto_now=True，每次更新数据记录的时候会更新该字段

- ForeignKey
  
  - `to`:设置要关联的表
  - `to_field`:设置要关联的字段
  - `related_name`:反向操作时，使用的字段名，用于代替原反向查询时的'表名_set'
  - `related_query_name`:反向查询操作时，使用的连接前缀，用于替换表名
  - `on_delete`:当删除关联表中的数据时，当前表与其关联的行的行为
    - `models.CASCADE`:删除关联数据，与之关联也删除
    - `models.DO_NOTHING`:删除关联数据，引发错误IntegrityError
    - `models.PROTECT`:删除关联数据，引发错误ProtectedError
    - `models.SET_NULL`:删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）
    - `models.SET_DEFAULT`:删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）
    - `models.SET`:删除关联数据
      - 与之关联的值设置为指定值，设置：models.SET(值)
      - 与之关联的值设置为可执行对象的返回值，设置：models.SET(可执行对象)
  - `db_constraint`:是否在数据库中创建外键约束，默认为True
