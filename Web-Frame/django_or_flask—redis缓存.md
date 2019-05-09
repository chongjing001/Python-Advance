
### django-redis

setting 文件
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },

    # 接口数据缓存
    'api': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://localhost:6379/2',
        ],
        'KEY_PREFIX': 'oa:api',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 500,
            },
        }
    },

    # 会话缓存
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://localhost:6379/3',
        ],
        'KEY_PREFIX': 'oa:session',
        'TIMEOUT': 1209600,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 2000,
            },
        }
    },    
}

# session使用的存储方式
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指明使用哪一个库保存session数据
SESSION_CACHE_ALIAS = "session"


```
views.py文件
```python
#导入缓存库
from django.core.cache import cache
#导入页面缓存
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# 接口
@cache_page(timeout=60, cache='api')
def foo(request):
	pass


# 渲染
@cache_page(20)
def foo(request):
	pass
```


### flask-redis
安装flask缓存插件Flask-Cache
pip install flask_cache

- manage.py文件
```python
app = Flask(__name__)

config = {
  'CACHE_TYPE': 'redis',
  'CACHE_REDIS_HOST': '127.0.0.1',
  'CACHE_REDIS_PORT': 6379,
  'CACHE_REDIS_DB': '',
  'CACHE_REDIS_PASSWORD': ''
}

app.config.from_object(config)
cache.init_app(app,config)
```
views.py 文件  例：
```python
@app.route('/')
@cache.cached(timeout=60*2)
def index():
  name = 'mink'
  return name
 
if __name__ == '__main__':
  app.run()
```
