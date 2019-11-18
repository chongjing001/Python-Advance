from django.urls import path, re_path

from sers import views

urlpatterns = [
    re_path("users/(?P<pk>\d)/", views.UserViews1.as_view()),
    path("users/", views.UserViews2.as_view()),
]
