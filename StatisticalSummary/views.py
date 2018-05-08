from django.shortcuts import render
from ReservationManagement.models import PhoneNumber, MobileCode4Day
# Create your views here.

def analysis(request):
    numberAnalysis1 = PhoneNumber.objects.filter(is_achieved = True).count()
    numberAnalysis2 = PhoneNumber.objects.filter(is_achieved=False).count()
    numberAnalysis3 = PhoneNumber.objects.filter(id_reserved=True).count()


    return render(request, 'home/mainFrame/Analysis.html',
                  {'numberAnalysis1': numberAnalysis1, 'numberAnalysis2': numberAnalysis2,
                   'numberAnalysis3': numberAnalysis3})
