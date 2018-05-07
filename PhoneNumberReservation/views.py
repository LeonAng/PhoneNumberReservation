# -*- coding: utf-8 -*
from django.shortcuts import render

# Create your views here.
# views.py 是Web应用后台的核心，定义了后台具体的响应动作和数据存取、操作动作的函数；
from django.http import HttpResponse

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
