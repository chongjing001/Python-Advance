#### **Flask**工厂函数

> 

[官网](http://docs.jinkan.org/docs/flask/patterns/appfactories.html)

##### 我的目录结构

```
flask_project

	-- config
		-- __init__.py
		-- config.py
		-- settings.py
		
	-- other_app
		...
		
	-- manage.py
	
```



##### 基本示例

- config.py

> 定义工厂函数

```python
from flask import Flask
from config.settings import config
from api.views import api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 日志
    register_logging(app)
    # 注册蓝图
    register_blueprints(app)
    # 数据库
    register_database(app)
    # 异常处理
    register_errors(app)
    # 注册自定义命令
    register_commands(app)

    return app


def register_logging(app):
    pass


def register_blueprints(app):
    app.register_blueprint(api, url_prefix='/api')


def register_database(app):
    pass


def register_errors(app):
    pass


def register_commands(app):
    pass

```



- settings.py

> 不同环境的配置(测试/生产/正式)

```python
class BaseConfig:
    TEST = True
    NUM = 10


config = {

    'default': BaseConfig
}
```



- manage.py

> 总入口

```python
from config.config import create_app


if __name__ == '__main__':

    app = create_app('default') # 默认环境
    print(app.config['NUM']) # 获取定义变量NUM
    
    app.run()
```

