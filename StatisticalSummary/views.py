from django.shortcuts import render

# Create your views here.

def analysis(request):
    return render(request, 'home/mainFrame/Analysis.html')
