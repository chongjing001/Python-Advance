from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=20)
    pwd = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    avatar = models.CharField(max_length=512)
    ctime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
