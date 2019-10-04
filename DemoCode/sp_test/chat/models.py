from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.


class chatTest(models.Model):
    pass

    class Meta:
        verbose_name = "chat"
        verbose_name_plural = "chat"


class MyUser(AbstractUser):
    avatar = models.CharField(max_length=512)
