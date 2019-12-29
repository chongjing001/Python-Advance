from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def is_login(func):
    def check(request):
        try:
            # 获取session中已保存的user
            request.session['user_id']
        except:
            # 调转到登录
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)

    return check
