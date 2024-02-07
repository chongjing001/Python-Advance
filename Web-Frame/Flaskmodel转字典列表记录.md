#### `Flask-sqlalchemy`  query_set结果转字典或列表记录

#### 代码

```python
import json
from datetime import datetime as cdatetime
from datetime import date, time
from flask_sqlalchemy.model import Model
from sqlalchemy import DateTime, Numeric, Date, Time, Text, Enum


def query_to_dict(models, deep_convert=False) -> list | dict:
    """
    将查询结果转换为字典/列表
    :param models: 查询结果
    :param deep_convert: json字符串转换
    """
    if not models:
        return models
    if isinstance(models, list):
        if isinstance(models[0], Model):
            lst = []
            for model in models:
                gen = model_to_dict(model, deep_convert)
                dit = dict((g[0], g[1]) for g in gen)
                lst.append(dit)
            return lst
        else:
            res = result_to_dict(models)
            return res
    else:
        if isinstance(models, Model):
            gen = model_to_dict(models, deep_convert)
            dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def model_to_dict(model, deep_convert=False):
    """
    将模型对象转换为字典
    """
    for col in model.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            # value = float(getattr(model, col.name))
            value = getattr(model, col.name)
        elif isinstance(col.type, Enum):
            value = getattr(model, col.name).value
        else:
            value = getattr(model, col.name)
            if deep_convert and isinstance(col.type, Text):
                try:
                    if value:
                        value = json.loads(value)
                except:
                    pass
        yield col.name, value


def find_datetime(value):
    for v in value:
        if isinstance(value[v], cdatetime):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    if value:
        if isinstance(value, (cdatetime, DateTime)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(value, (date, Date)):
            return value.strftime("%Y-%m-%d")
        elif isinstance(value, (Time, time)):
            return value.strftime("%H:%M:%S")
    else:
        return ""

```

