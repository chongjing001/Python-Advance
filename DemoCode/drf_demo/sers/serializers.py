from rest_framework import serializers

from user.models import User


def about_name(value):
    if 'drf' in value.lower():
        raise serializers.ValidationError("name不能是drf")


# 声明序列化器，所有的序列化器都要直接或者间接继承于 Serializer
# 其中，ModelSerializer是Serializer的子类，ModelSerializer在Serializer的基础上进行了代码简化
class UserSerializer(serializers.Serializer):
    """用户信息序列化器"""
    # 1. 需要进行数据转换的字段
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[about_name])  # 可以添加多个
    age = serializers.IntegerField()
    sex = serializers.BooleanField()
    phone = serializers.CharField(read_only=True)
    addr = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """新建"""
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.addr = validated_data.get('addr', instance.addr)
        instance.save()
        return instance

    def validate_name(self, value):
        if 'niko' in value.lower():
            raise serializers.ValidationError("name不能为niko")
        return value

    def validate(self, attrs):
        age = attrs['age']
        sex = attrs['sex']
        if age < sex:
            raise serializers.ValidationError('age不能比sex小')
        return attrs
