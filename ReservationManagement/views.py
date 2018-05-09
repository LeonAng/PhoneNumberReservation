from django.shortcuts import render
import datetime
# Create your views here.
from django.template.loader import get_template

from ReservationManagement.models import PhoneNumber, MobileCode4Day


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def reservationManagement(request):
    if request.session.get('is_admin'):
        list = PhoneNumber.objects.filter(is_achieved = True)
    else:
        list = PhoneNumber.objects.filter(user_name = request.session.get('username'))
    return render(request, 'home/mainFrame/ReservationManagement.html', {'list': list})


def phoneNumberPutting(request):
    list = MobileCode4Day.objects.all()
    return render(request, 'home/mainFrame/PhoneNumberPutting.html',{'list': list})


def deleteNumber(request):
    phone_number = request.GET['phone_number']
    phoneNumber = PhoneNumber.objects.get(phone_number = phone_number)
    phoneNumber.is_achieved = False
    phoneNumber.date = None
    phoneNumber.user_name = None
    phoneNumber.save()
    return render(request, 'home/mainFrame/ReservationManagement.html')


def setMobileCode(request):
    mobile_code_start = int(request.POST['mobile_code_start'])
    mobile_code_end = int(request.POST['mobile_code_end'])

    if request.POST['reservation_strategy_666'] =='1':
        reservation_strategy_666 = True
    else:
        reservation_strategy_666 = False
    if request.POST['reservation_strategy_888'] =='1':
        reservation_strategy_888 = True
    else:
        reservation_strategy_888 = False
    reservation_number = request.POST['reservation_number']
    mobileCode4Day = MobileCode4Day(date=datetime.datetime.now().strftime('%Y-%m-%d'),
                                    mobile_code_start=mobile_code_start,
                                    mobile_code_end=mobile_code_end,
                                    reservation_strategy_666=reservation_strategy_666,
                                    reservation_strategy_888=reservation_strategy_888,
                                    reservation_number=reservation_number)
    mobileCode4Day.save()

    reservation_number_list = reservation_number.split(',')
    for i in range(mobile_code_start,mobile_code_end+1):
        phoneNumber = PhoneNumber(phone_number = i)
        # 处理预留号码
        if str(i) in reservation_number_list:
            phoneNumber.id_reserved=True
        if reservation_strategy_666 and str(666) in str(i):
            phoneNumber.id_reserved = True
        if reservation_strategy_666 and str(888) in str(i):
            phoneNumber.id_reserved = True

        phoneNumber.save()
    return render(request, 'home/mainFrame/ReservationManagement.html')