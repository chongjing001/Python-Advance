import json

from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
from user.models import User


@api_view(['GET'])
def login(request):
    return render(request, 'user/login.html')


@api_view(['POST'])
def user_register(request):

    
    print(request.data)
    print(request.POST)

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if User.objects.filter(username=username).exists():
        return JsonResponse({'code': -1, 'msg': '用户名已存在'})
    user = User()
    user.username = username
    user.pwd = make_password(password)
    user.save()

    return JsonResponse({'code': 200, 'msg': 'success'})


# @api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_obj = User.objects.filter(username=username).first()
        if check_password(password, user_obj.pwd):
            request.session['user_id'] = user_obj.id
            return JsonResponse({'code': 200, 'msg': 'success'})



def get_csrf(request):
    x = csrf(request)
    csrf_token = x['csrf_token']
    return JsonResponse({'code': 200, 'msg': 'success', 'data': str(csrf_token)})
