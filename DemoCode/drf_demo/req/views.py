from django.views import View
from django.http import HttpResponse, JsonResponse


class UserViews(View):
    """用户View类"""

    def get(self, request):
        print(request)
        print(request.GET)
        """打印效果：
        <WSGIRequest: GET '/req/users/'>  # 这是django原生提供的HttpRequest类
        """

        return HttpResponse('ok')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from sers.serializers import UserModelSerializer
from user.models import User


class UserApiviews1(APIView):
    """用户APIView类,用于查询单个、更新、删除"""

    def get(self, request, pk):
        # 获取单个数据
        user = User.objects.get(pk=pk)
        # 数据转换[序列化过程]
        serializer = UserModelSerializer(instance=user)
        # 响应数据
        return Response(serializer.data, HTTP_200_OK)

    def put(self, request, pk):
        """在更新中调用序列化器完成数据的更新操作"""
        user_obj = User.objects.get(pk=pk)
        # 实例化序列化器
        serializer = UserModelSerializer(instance=user_obj, data=request.data)

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


class UserApiviews2(APIView):
    """用户APIView类,用于新增、查询全部"""

    def get(self, request):
        """新增用户"""
        print(request)
        """
        控制台：<rest_framework.request.Request object at 0x7efc8a7f7128>
        """
        data_list = User.objects.all()
        serializer = UserModelSerializer(instance=data_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        """添加数据"""
        # 接受post请求数据
        data_dict = request.data
        # 调用序列化器
        serializer = UserModelSerializer(data=data_dict)
        # 验证
        serializer.is_valid(raise_exception=True)
        # 反序列化，保存数据
        serializer.save()
        # 响应数据
        return Response(serializer.data, HTTP_200_OK)


from rest_framework.generics import GenericAPIView


class UserGenericAPIView2(GenericAPIView):
    queryset = User.objects.all()  # 当前视图类中操作的公共数据，先从数据库查询出来
    serializer_class = UserModelSerializer  # 设置类视图中所有方法共有调用的视图类

    def get(self, request):
        """获取所有数据"""
        # 获取模型数据
        user_list = self.get_queryset()
        # 调用序列化器
        serializer = self.get_serializer(instance=user_list, many=True)

        return Response(serializer.data, HTTP_200_OK)

    def post(self, request):
        """添加数据"""
        # 获取客户端提交的数据
        serializer = self.get_serializer(data=request.data)
        # 使用序列化器进行验证
        serializer.is_valid(raise_exception=True)
        # 反序列化
        serializer.save()
        # 返回结果
        return JsonResponse({'code': 200, 'msg': 'add success'})


class UserGenericAPIView1(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get(self, request, pk):  # 这里的参数名必须叫pk，否则要配置另一个名称如果不配置，则报错!
        # 报错信息：  get() got an unexpected keyword argument 'pk'
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object()
        # 获取客户端提交数据
        data = request.data
        # 实例化序列化器期
        serializer = self.get_serializer(instance=instance, data=data)
        # 验证
        serializer.is_valid(raise_exception=True)
        # 反序列化
        serializer.save()
        # 返回响应
        return Response(serializer.data)

    def delete(self, request, pk):
        user = User.objects.filter(id=pk).first()
        user.delete()
        print(f'删除{user}用户成功')
        return JsonResponse({'code': 200, 'msg': 'del success'})


"""GenericAPIView结合视图扩展类实现api接口"""
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# 声明分页的配置类
from rest_framework.pagination import PageNumberPagination


class UserPageNumberPagination(PageNumberPagination):
    # 默认每一页显示的数据量
    page_size = 2
    # 允许客户端通过get参数来控制每一页的数据量
    page_size_query_param = "size"
    max_page_size = 10
    # 自定义页码的参数名
    page_query_param = "page"


class UserMiXinGenericAPIView2(GenericAPIView, ListModelMixin, CreateModelMixin):
    # 本次视图类中要操作的数据   [必填]
    queryset = User.objects.all()
    # 本次视图类中要调用的默认序列化器  [必填]
    serializer_class = UserModelSerializer
    # 分页器
    pagination_class = UserPageNumberPagination

    def get(self, request):
        """获取多个用户信息"""
        return self.list(request)

    def post(self, request):
        """添加用户信息"""
        return self.create(request)


from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class UserMiXinGenericAPIView1(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()

    serializer_class = UserModelSerializer

    # 在使用GenericAPIView视图获取或操作单个数据时,视图方法中的代表主键的参数最好是pk
    def get(self, request, pk):
        """获取一条数据"""
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """更新一条数据"""
        return self.update(request, pk)

    def delete(self, request, pk):
        """删除一条数据"""
        return self.destroy(request, pk)


# ListAPIView    获取所有数据
# CreateAPIView 添加数据
from rest_framework.generics import ListAPIView, CreateAPIView


class LCUserGenericAPIView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# RetrieveAPIView   获取一条数据
# UpdateAPIView     更新一条数据
# DestorAPIView     删除一条数据
# RetrieveUpdateDestoryAPIView  上面三个的缩写
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class UserModelViewSet1(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                        DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


from rest_framework.viewsets import ModelViewSet


class UserModelViewSet2(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
