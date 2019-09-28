from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('init_ws_pubic_room/', views.init_ws_pubic_room, name='init_ws_pubic_room')

]
