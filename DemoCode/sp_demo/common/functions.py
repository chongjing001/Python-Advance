from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def is_login(func):
    def check(request):
        try:
            # 获取session中已保存的user
            request.session['user']
        except:
            # 调转到登录
            return render(request,'user/login.html')
        return func(request)

    return check
