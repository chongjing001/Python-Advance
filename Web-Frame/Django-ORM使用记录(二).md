##### ORM查询

- queryset和objects对象
  - 1.queryset是查询集，就是传到服务器上的url里面的内容。Django会对查询返回的结果集QerySet进行缓存，这里是为了提高查询效率，也就是说，在你创建一个QuerySet对象的时候，Django并不会立即向数据库发出查询命令，只有在你需要用到这个QuerySet的时候才回去数据库查询
  - 2.Objects是django实现的mvc框架中的数据层(model)m，django中的模型类都有一个objects对象，它是一个django中定义的QuerySet类型的对象它包含了模型对象的实例。简单的说，objects是单个对象，queryset是许多对象
  - 3.QuerySet 可以被构造，过滤，切片，做为参数传递，这些行为都不会对数据库进行操作。只要你查询的时候才真正的操作数据库

| 管理器方法             | 返回类型                            | 说明                                                                                       |
| ----------------- | ------------------------------- | ---------------------------------------------------------------------------------------- |
| 模型类.objects.all() | QuerySet                        | 返回表中所有数据                                                                                 |
| filter()          | QuerySet                        | 返回符合条件的数据                                                                                |
| values()          | ValuesQuerySet(QuerySet的子类)     | 返回一个列表 每个元素为一个字典                                                                         |
| values_list()     | ValuesListQuerySet(QuerySet的子类) | 返回一个列表，不过它的元素不是字典，而是元组                                                                   |
| get()             | 模型对象                            | 返回一个满足条件的对象； 如果没有找到符合条件的对象，会引发模型类.DoesNotExist异常;  如果找到多个，会引发模型类.MultiObjectsReturned 异常 |
| first()           | 模型对象                            | 返回第一条数据                                                                                  |
| last()            | 模型对象                            | 返回最后一条数据                                                                                 |
| exclude()         | QuerySet                        | 返回不符合条件的数据                                                                               |
| order_by()        | QuerySet                        | 对查询结果集进行排序                                                                               |
| reverse()         | QuerySet                        | 对排序的结果反转                                                                                 |
| count()           | int                             | 返回查询集中对象的数目                                                                              |
| exists()          | bool                            | 判断查询的数据是否存在                                                                              |

- 1.len()与count()
  
  - 计算QuerySet元素的数量，并不推荐使用len()，除非QuerySet是求过值的（即evaluated），否则，用QuerySet.count()获取元素数量，这个效率要高很多，特别在数据量大(上万)的时候

- 2.if QuerySet: 与 if QuerySet.exists()
  
  - 同样不建议`if QuerySet`这种方法判断是否为空，而应该使用QuerySet.exists()，查询效率高

- 3.F类
  
  ```python
  from django.db import models
  from django.db.models import F
  ```

class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    both = models.CharField(max_length=20)

```

**不使用F()**
```python
s = User.objects.get(name='xxx')
s.age += 1
s.save()
```

将对象从数据库中查出来放到内存中，然后计数，再存入到数据库中

**使用F()**

```python
s = User.objects.get(name='xxx')
s.age = F('age') + 1
s.save()
```

直接在数据库中查出数据，计数后更改数据库

- 4. Q类 - 对应(and/or/not)
     - 如果有or等逻辑关系呢，那就用Q类
     - filter中的条件可以是Q对象与非Q查询混和使用，但不建议这样做，因为混和查询时Q对象要放前面，这样就有难免忘记顺序而出错，所以如果使用Q对象，那就全部用Q对象
     - Q对象也很简单，就是把原来filter中的各个条件分别放在一个Q()即可，不过我们还可以使用或与非，分别对应符号为”|”和”&”和”~”，而且这些逻辑操作返回的还是一个Q对象，另外，逗号是各组条件的基本连接符，也是与的关系，其实可以用&代替（在python manage.py shell测试过，&代替逗号，执行的SQL是一样的），不过那样的话可读性会很差，这与我们直接写SQL时，各组条件and时用换行一样，逻辑清晰
       
       ```shell
       >>> python manage.py shell
       >>> from django.db.models import Q
       >>> Poll.objects.get( Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
       question__startswith='Who')   # 正确，但不要这样混用
       >>> Poll.objects.get( Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
       Q(question__startswith='Who'))  # 推荐，全部是Q对象
       >>> Poll.objects.get( (Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))&
       Q(question__startswith='Who'))  # 与上面语句同意，&代替”,”，可读性差
       ```
       
       Q类中时应该可以使用F类吗?? 有兴趣的可以试一下

- annotate（无对应SQL关键字）
  - 函数`annotate(*args, **kwargs)`:返回QuerySet
  - 往每个QuerySet的model instance中加入一个或多个字段，字段值只能是聚合函数，因为使用annotate时，会用group by，所以只能用聚合函数。聚合函数可以像filter那样关联表，即在聚合函数中，Django对OneToOne、OneToMany、ManyToMany关联查询及其反向关联提供了相同的方式

示例：

```python
from django.db.models import Count
s = User.objects.all().annotate(n=Count('age'))
```

- 5.order_by()
  
  - 如果直接用字段名，那就是升序asc排列；如果字段名前加-，就是降序desc
  - 返回QuerySet

- 6.distinct()
  
  - 一般与values()、values_list()连用，这时它返回ValuesQuerySet、ValuesListQuerySet这个类跟列表很相似，它的每个元素是一个字典
  - 它没有参数（其实是有参数的，不过，参数只在PostgreSQL上起作用）
    
    示例：
    
    ```python
    s = User.objects.values('name').distinct()
    ```

- 7.aggregate
  
  - `aggregate(*args,**kwargs)`:参数为聚合函数，最好用`**kwargs`的形式，每个参数起一个名字
  - annotate相当于aggregate()和group_by的结合，对每个group执行aggregate()函数。而单独的aggregate()并没有group_by
    
    ```python
    from django.db.models import Count
    # 这是用*args的形式，最好不要这样用
    s = User.objects.aggregate(Count('name'))
    # 这是用**kwargs的形式
    s = User.objects.aggregate(n=Count('name'))
    ```

- 8.模糊查询
  
  - `gt/gte/lt/lte`对应`>,>=,<,<=`:字段名加双下划线 
    - `age__gt=18`:年龄大于18
  - `in`对应in:字段名加双下划线
  - `contains/startswith/endswith`对应like:字段名加双下划线
  - `range`对应`between and`:字段名加双下划线，range后面值是列表

- 9. extra()
     - `extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)`
     - 实现复杂的where字句,在 extra 可以指定一个或多个 params 参数，如 select，where 或 tables。所有参数都是可选的，但你至少要使用一个
       
       简单示例：
       
       ```python
       s = User.objects.extra(select={'is_recent':"both>'2000-01-01'"})
       ```
