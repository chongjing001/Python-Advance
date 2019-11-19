from django.urls import path, re_path

from req import views

urlpatterns = [
    # path("users/", views.UserViews.as_view()),            # View

    # path("users/", views.UserApiviews2.as_view()),        # APIView
    # re_path("users/(?P<pk>\d)/", views.UserApiviews1.as_view()),

    # path("users/", views.UserGenericAPIView2.as_view()),    # GenericAPIView
    # re_path("users/(?P<pk>\d)/", views.UserGenericAPIView1.as_view()),

    # path("users/", views.UserMiXinGenericAPIView2.as_view()),  # MiXin + GenericAPIView
    # re_path("users/(?P<pk>\d)/", views.UserMiXinGenericAPIView1.as_view()),

    # path("users/", views.LCUserGenericAPIView.as_view()),  # LCUserGenericAPIView
    # re_path("users/(?P<pk>\d)/", views.UserRetrieveUpdateDestroyAPIView.as_view()),  # UserRetrieveUpdateDestroyAPIView

    path("users/", views.UserModelViewSet2.as_view({"get": "list", "post": "create"})),
    re_path("users/(?P<pk>\d+)/",
            views.UserModelViewSet2.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))
]
