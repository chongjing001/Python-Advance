from rest_framework import serializers
from user.models import User


# 创建序列化器类，视图中被调用
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
