from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from ReservationManagement.models import PhoneNumber, MobileCode4Day


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def reservationManagement(request):
    if request.session.get('is_admin'):
        list = PhoneNumber.objects.all()
    else:
        list = PhoneNumber.objects.filter(user_name = request.session.get('username'))
    return render(request, 'home/mainFrame/ReservationManagement.html', {'list': list})


def phoneNumberPutting(request):
    list = MobileCode4Day.objects.all()
    return render(request, 'home/mainFrame/PhoneNumberPutting.html',{'list': list})

def deleteNumber(request):
    phone_number = request.GET['phone_number']
    #print(phone_number)
    phoneNumber = PhoneNumber.objects.get(phone_number = phone_number)
    phoneNumber.is_achieved = False
    phoneNumber.date = None
    phoneNumber.user_name = None
    phoneNumber.save()
    return render(request, 'home/mainFrame/ReservationManagement.html')
