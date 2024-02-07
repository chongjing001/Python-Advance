#### `flask_sqlalchemy`  filter函数封装记录
> 实现类似DRF中filter类的效果

#### 

```python
"""
 基于flask_sqlalchemy filter函数封装
 author: chongjing001
 date: 2024/02/06
 version: 1.0
"""
from typing import List, Dict
from enum import Enum
from app_core.utils.exceptions.app_exception import FilterError # 自定义的异常


class FilterBy(Enum):

    GT = 'gt'
    GTE = 'gte'
    LT = 'lt'
    LTE = 'lte'
    IN = 'in'
    LIKE = 'like'
    ISNULL = 'isnull'


class FilterSetOptions:
    def __init__(self, options=None):
        self.model = getattr(options, "model", None)
        # self.fields = getattr(options, "fields", None)
        # self.exclude = getattr(options, "exclude", None)


class FilterSetMetaclass(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._meta = FilterSetOptions(getattr(new_class, "Meta", None))
        return new_class


class BaseFilterSet:
    filter_by_fields: List = []
    filter_fields: Dict[str, FilterBy] = {}
    to_int_fields: List = []

    @classmethod
    def get_filter_params(cls, key: str, con: FilterBy, value: str):
        model = cls._meta.model
        attr = getattr(model,key)
        match con:
            case FilterBy.GT:
                return attr > value
            case FilterBy.GTE:
                return attr >= value
            case FilterBy.LT:
                return attr < value
            case FilterBy.LTE:
                return attr <= value
            case FilterBy.LIKE:
                return attr.like(f'%{value}%')

    @classmethod
    def get_query(cls, **kwargs):
        filter_by_kwargs = dict()
        filter_kwargs = set()
        for key in kwargs:
            value = kwargs[key]
            if not value:
                continue
            if key not in cls.filter_fields.keys() and key not in cls.filter_by_fields and key not in ['page', 'size']:
                raise FilterError(f'不支持筛选的字段:{key}')
            if key in cls.to_int_fields:
                kwargs[key] = int(kwargs[key])
            if key in cls.filter_fields:
                filter_kwargs.add(cls.get_filter_params(key, cls.filter_fields[key], value))
            if key in cls.filter_by_fields:
                filter_by_kwargs[key] = value
        model = cls._meta.model
        records = model.query
        if filter_by_kwargs:
            records = records.filter_by(**filter_by_kwargs)
        if filter_kwargs:
            records = records.filter(*filter_kwargs)
        return records

    @classmethod
    def get_result(cls, **kwargs):
        records = cls.get_query(**kwargs)
        return records.all()

    @classmethod
    def get_result_pagination(cls, **kwargs):
        """
        分页获取
        :param kwargs: query参数
        """
        records = cls.get_query(**kwargs)
        total = records.count()
        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 10))
        model = cls._meta.model
        return records.order_by(model.create_time.desc()).paginate(page=page, per_page=size,
                                                                  error_out=False).items, page, size, total


class FilterSet(BaseFilterSet, metaclass=FilterSetMetaclass):
    """
        说明：
            基于flask_sqlalchemy filter函数封装
            继承该类，实现filter_fields、filter_by_fields、to_int_fields属性
       示例：
       过滤定义：
       class TaskFilter(FilterSet):
           filter_by_fields = ['task_guid', 'task_status', 'task_type', 'creator_name', 'creator_code', 'application_step']
           filter_fields = {'name': FilterBy.LIKE, 'begin': FilterBy.GTE, 'end': FilterBy.LTE}
           to_int_fields = ['task_status']
           class Meta:
               model = Task
       使用：
       kwargs = dict(request.args)
       不分页：
           data = TaskFilter.get_result(**kwargs)
       分页：
           data, page, size, total = TaskFilter.get_result_pagination(**kwargs)

       """
    pass

```

