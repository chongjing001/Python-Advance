##### 这里记录使用pillow

###### 测试环境
- Python版本：python3
- 用到的三方库
	- `django`: 2.1.7
	- `pymysql`: 0.9.3
	- `pillow`: 

###### 基本工作

- **主配置文件`settings.py`**
示例：
```python
# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',  # 数据库
        'USER': 'root', # 用户名
        'HOST': '127.0.0.1', # ip地址
        'PASSWORD': '123456', # 数据库密码
        'POST': '3306',
        'AUTOCOMMIT': True,

    }
}

# 静态文件目录配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),

]

# 媒体文件目录配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
- 项目目录下(`__init__.py`)配置`mysql`驱动
```python
import pymysql

pymysql.install_as_MySQLdb()
```
- 项目目录下（`urls.py`）路由配置
```python
from django.urls import path,include,re_path
from my_file import views
from hello.settings import MEDIA_ROOT, MEDIA_URL,STATICFILES_DIRS
from django.contrib.staticfiles.urls import static
from django.views.static import serve

urlpatterns = [
    path('file/', include(('my_file.urls','file'),namespace='file')),
    path('',views.hello),
	
	# 配置路由分发
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": STATICFILES_DIRS[0]}),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),


]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
```

- 创建相关一应用`pyhton manage.py startapp 应用名`
示例：
`pyhton manage.py startapp my_file`

###### 上传图片

- `models.py`文件 - 建立django模型
```python
from django.db import models


class Img(models.Model):
	# 定义为ImageField字段类型
	# upload_to定义为 设定媒体文件/img 下存放图片
    img_url = models.ImageField(upload_to='img')
```
- 创建数据表(这里使用django中的迁移命令)
	- 生成迁移文件: `python manage.py makemigrations`
		- 可在应用目录下的migrations目录中查看
	- 迁移到数据库: `python manage.py migrate`
- 视图函数`views.py`
```python
from django.shortcuts import render
from my_file.models import Img,My_file

def upload_file(request):
    if request.method == 'GET':
        return render(request, 'up_file.html')
        
    if request.method == 'POST':
        my_file = request.FILES.get('my_file')
        if not my_file:
            return render(request, 'up_file.html', {'msg': '没有文件...请从新上传'})
        img = Img(img_url=my_file)

        # 图片缩放
        # img = img.resize((100,100))
        img.save()
        return render(request, 'up_file.html', {'msg': '上传成功'})
```
- `html`文件
示例：这里from表单上传，也可以使用ajax异步提交(略)
```html
 <form action="/file/my_file/" method="post" ENCTYPE="multipart/form-data">
 			{% csrf_token %}
            <input type="file" name="my_file">
            <br>
            <input type="submit" value="upload" id="show_tip" >
        </form>
```
- 再配置一下路由就ok（略）
###### 文件上传
- `models.py`
```python
class File(models.Model):
	# 定义为FileField字段类型
	# upload_to定义为 设定媒体文件/file 下存放文件
    file_path = models.FileField(upload_to='file')
```
- 其他 同图片上传