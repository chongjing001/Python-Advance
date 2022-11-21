#### Python项目日志使用记录(loguru)



*封装如下*

- 实现多文件记录

```python
import os
import datetime
from loguru import logger
from config import BASE_DIR


class Logings:

    __logger = dict()


    def __init__(self, file_name='info'):

        if Logings.__logger.__contains__(file_name):
            self.logger = Logings.__logger[file_name]
            return
        self.file_name = file_name
        # 文件名称，按天创建
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        # 项目路径下创建log目录保存日志文件
        logpath = f'{BASE_DIR}/logs/{date}'  # 拼接指定路径
        # 判断目录是否存在，不存在则创建新的目录
        if not os.path.isdir(logpath): os.makedirs(logpath)

        logger.add(f'{logpath}/{self.file_name}.log',  # 指定文件
                   format="{time}  | {level}| {message}",
                   encoding='utf-8',
                   retention='1 days',  # 设置历史保留时长
                   backtrace=True,  # 回溯
                   diagnose=True,  # 诊断
                   enqueue=True,  # 异步写入
                   # rotation="5kb",  # 切割，设置文件大小，rotation="12:00"，rotation="1                         week"
                   filter=lambda record: record["extra"].get("name") == self.file_name 
                   # 过滤模块
                   # compression="zip"   # 文件压缩
                   )

        self.logger = logger.bind(name=self.file_name)
        self.logger.__setattr__('name', file_name)
        if not Logings.__logger.__contains__(file_name):
            Logings.__logger[file_name] = self.logger


    # def __new__(cls, *args, **kwargs):
    #     if not cls.__instance:
    #         cls.__instance = super(Logings, cls).__new__(cls, *args, **kwargs)
    #     return cls.__instance

    def info(self, msg, *args, **kwargs):
        return logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        return logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        return logger.exception(msg, *args, exc_info=True, **kwargs)

# 基本日志 info error request
info_log = Logings().logger
error_log = Logings('error').logger
req_log = Logings('request').logger
```



##### 指定模块记录

- 实例化Logings
  - *示例：*

```python
class TaskDispatch(object):

    sc_type = None
    req_data = dict()
    req_header = None
	logger = None


    def __init__(self, **kwargs):
        self.logger = Logings(self.__class__.__name__).logger
```

