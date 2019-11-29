from django.urls import path
from .views import index,init_ws_pubic_room,user_off_line

app_name = 'chat'

urlpatterns = [
    path('index/', index, name='index'),
    path('init_ws_pubic_room/', init_ws_pubic_room, name='init_ws_pubic_room'),
    path('user_off_line/', user_off_line, name='user_off_line'),
]
