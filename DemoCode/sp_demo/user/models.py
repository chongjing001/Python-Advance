from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=20, null=True)
    pwd = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)
    avatar = models.CharField(max_length=512, null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=False,verbose_name="是否在线")

    class Meta:
        db_table = 'user'


class UserFriends(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    friend = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE, verbose_name='好友id')

    class Meta:
        db_table = 'user_friends'
