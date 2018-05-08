# -*- coding: utf-8 -*
from django.shortcuts import render
from ReservationManagement.models import PhoneNumber
import datetime
# Create your views here.
# views.py 是Web应用后台的核心，定义了后台具体的响应动作和数据存取、操作动作的函数；
from django.http import HttpResponse

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def reservation(request):
    list = PhoneNumber.objects.filter(is_achieved = False)
    return render(request, 'home/mainFrame/Reservation.html', {'list': list})

def reservationNumber(request):
    phone_number = request.GET['phone_number']
    phoneNumber = PhoneNumber.objects.get(phone_number=phone_number)
    phoneNumber.is_achieved = True
    phoneNumber.date = datetime.datetime.now().strftime('%Y-%m-%d')
    phoneNumber.user_name = request.session.get('username')
    phoneNumber.save()
    return render(request, 'home/mainFrame/ReservationManagement.html')
