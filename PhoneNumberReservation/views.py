# -*- coding: utf-8 -*
from django.shortcuts import render
from ReservationManagement.models import PhoneNumber
import datetime
import math
# Create your views here.
# views.py 是Web应用后台的核心，定义了后台具体的响应动作和数据存取、操作动作的函数；
from django.http import HttpResponse

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def reservation(request):
    list1 = PhoneNumber.objects.filter(is_achieved = False)

    # 每页显示10条数据
    per_page_count = 8
    # current-page 当有页

    current_page = request.GET.get('p')

    # 数字运算要转成int类型
    current_page = int(current_page)
    # 如果是第1页，索引0-9，就是1-10的数
    # p=1
    # 0,10   0-9  取索引
    # p=2
    # 大于等于10，小于20就是10-19
    # 10,20 10-19
    # start 开始页数  end=结束页数

    # 如果p=1-1=0
    start = (current_page - 1) * per_page_count
    # 1 * 10=10
    end = current_page * per_page_count
    # 数据切片，每次显示10页
    list = list1[start:end]

    # 上一页
    if current_page >= 2:
        prev_pager = current_page - 1
    else:
        prev_pager = 1
    # 下一页
    if current_page < math.ceil(list1.count()/per_page_count):
        next_pager = current_page + 1
    else:
        next_pager = math.ceil(list1.count()/per_page_count)

    return render(request, 'home/mainFrame/Reservation.html', {'list': list,'prev_pager':prev_pager,'next_pager':next_pager})

def reservationNumber(request):
    phone_number = request.GET['phone_number']
    phoneNumber = PhoneNumber.objects.get(phone_number=phone_number)
    phoneNumber.is_achieved = True
    phoneNumber.date = datetime.datetime.now().strftime('%Y-%m-%d')
    phoneNumber.user_name = request.session.get('username')
    phoneNumber.save()
    return render(request, 'home/mainFrame/ReservationManagement.html')
