from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('user_register/', user_register, name='user_register'),
    path('user_login/', user_login, name='user_login'),
    path('get_csrf/', get_csrf, name='get_csrf'),
]
