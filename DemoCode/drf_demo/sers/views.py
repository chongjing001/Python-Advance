from django.views import View
from user.models import User
from .serializers import UserSerializer
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViews1(APIView):
    """使用序列化器序列化转换单个模型数据"""

    def get(self, request, pk):
        # 获取单个数据
        user = User.objects.get(pk=pk)
        # 数据转换[序列化过程]
        serializer = UserSerializer(instance=user)
        print(serializer.data)
        # 响应数据
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        """在更新中调用序列化器完成数据的更新操作"""
        user_obj = User.objects.get(pk=pk)

        data_dict = self.__request_to_dict(request)
        print(data_dict)

        # 实例化序列化器
        serializer = UserSerializer(instance=user_obj, data=data_dict)

        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        print(f'update {instance}')

        return JsonResponse({'code': 200, 'msg': 'update success'})

    def delete(self, request, pk):
        """在更新中调用序列化器完成数据的删除操作"""
        user = User.objects.filter(id=pk).first()
        user.delete()
        print(f'删除{user}用户成功')
        return JsonResponse({'code': 200, 'msg': 'del success'})

    @staticmethod
    def __request_to_dict(request):
        req_data = request.data
        data_dict = {
            'name': req_data.get('name', ''),
            'age': req_data.get('age', ''),
            'sex': req_data.get('sex', ''),
            'phone': req_data.get('phone', ''),
            'addr': req_data.get('addr', ''),
        }

        return data_dict


class UserViews2(View):
    """使用序列化器序列化转换多个模型数据"""

    def get(self, request):
        # 获取数据
        user_list = User.objects.all()

        # 转换数据[序列化过程]
        # 如果转换多个模型对象数据，则需要加上many=True
        serializer = UserSerializer(instance=user_list, many=True)
        print(serializer.data)  # 序列化器转换后的数据

        # 响应数据给客户端
        # 返回的json数据，如果是列表，则需要声明safe=False
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data_dict = self.__request_to_dict(request)
        """在客户端提交数据的时，对数据进行验证"""
        serializer = UserSerializer(data=data_dict)

        result = serializer.is_valid(raise_exception=True)
        print(f"验证的结果： {result}")
        # 获取验证的错误信息
        if not result:
            print("错误信息： %s" % serializer.error_messages)

        # save表示让序列化器开始执行反序列化代码 create和update的代码
        user = serializer.save()

        print(f'新建用户：{user}')

        return JsonResponse({'code': 200, 'msg': 'add success'})

    @staticmethod
    def __request_to_dict(request):
        req_data = request.POST
        data_dict = {
            'name': req_data.get('name', ''),
            'age': req_data.get('age', ''),
            'sex': req_data.get('sex', ''),
            'phone': req_data.get('phone', ''),
            'addr': req_data.get('addr', ''),
        }

        return data_dict
