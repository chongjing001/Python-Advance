from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
from user.models import User


@api_view(['GET'])
def login(request):
    return render(request, 'user/login.html')


@api_view(['GET', 'POST'])
def user_page(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        user_obj = User.objects.filter(username=username).first()
        if check_password(password, user_obj.pwd):
            request.session.user = user_obj
            return redirect('/chat/index/')
    elif request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'code': -1, 'msg': '用户名已存在'})
        user = User()
        user.username = username
        user.pwd = make_password(password)
        user.save()

        return JsonResponse({'code': 200, 'msg': 'success'})
