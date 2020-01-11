from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from user.filter import UserFilter

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name', 'age')
    filter_class = UserFilter
