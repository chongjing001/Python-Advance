#### Flask异常处理使用记录



> 初识Flask异常处理，是使用`@app.teardown_request`钩子函数错处理

```python
# 遇到错误就执行
@app.teardown_request
def teardown_request(e):
     print('error:', e)
```

>我想搭配日志记录和错误状态返回
>
>[感谢该博主的文章](https://www.cnblogs.com/luyuze95/p/12937704.html)  厉害厉害

> 我再改吧改吧， 哈哈

##### 异常自定义

```python
import json

from flask import request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = None
    msg = None
    

    def __init__(self, msg=None):
        self.msg = msg or self.__class__.__name__
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            error_msg=self.msg,
            error_code=self.code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        return json.dumps(body)


    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

# 使用type原类封装一个类的工厂
def gen_error(name: str, err_code: int) -> APIException:
    base_cls = (APIException,)
    cls_attr = {'code': err_code}
    return type(name, base_cls, cls_attr)


# 通用错误，自定义，状态码和描述
NotFoundError = gen_error('NotFoundError', 404)
InternalError = gen_error('InternalError', 500)  # 服务器内部错误
ParamsError = gen_error('ParamsError', 1001)  # 参数错误
DataError = gen_error('DataError', 1002)  # 数据错误
DoseNotExist = gen_error('DoseNotExist', 1003)  # 不存在
ReachUpperLimit = gen_error('ReachUpperLimit', 1004)  # 达到上限
PermissionDenied = gen_error('PermissionDenied', 1005)  # 没有权限
Timeout = gen_error('Timeout', 1006)  # 超时
Expired = gen_error('Expired', 1007)  # 已过期
NotAllowRequestType = gen_error('NotAllowRequestType', 1008)  # 不允许的请求方式
RestrictOperation = gen_error('RestrictOperation', 1009)  # 限制操作

UnKnownError = gen_error('UnKnownError', 1020) # 未知错误


```



##### Flask全局处理

```python


# 全局错误AOP处理
@app.errorhandler(Exception)
def framework_error(e): 
    my_error_log.logger.error(e)  # 对错误进行日志记录，文件/控制台 输出
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        return UnKnownError()
    	# return UnKnownError('要提示的信息，为空的话，默认提示创建时的类名哦')
    else:
        return InternalError()
        
```

> `UnKnownError()`和`InternalError()`是上面自定义的异常

