from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path('index/', index, name='index'),
    path('init_ws_pubic_room/', init_ws_pubic_room, name='init_ws_pubic_room')
]
