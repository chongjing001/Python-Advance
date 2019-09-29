from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        pass