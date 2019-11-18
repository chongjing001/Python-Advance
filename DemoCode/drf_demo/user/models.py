from django.db import models


# Create your models here.

class User(models.Model):
    # 模型字段
    name = models.CharField(max_length=10, verbose_name="姓名")
    sex = models.BooleanField(default=1, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    phone = models.CharField(max_length=20, null=True, verbose_name="电话")
    addr = models.CharField(max_length=100,null=True,verbose_name="地址")

    class Meta:
        db_table = "tb_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
