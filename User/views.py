from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
from User.models import User


def index(request):
    return render(request, 'user/index.html')


def login(request):
    name = request.POST['name']
    pass_word = request.POST['password']
    user = User(name,pass_word)
    list = User.objects.all()
    for i in list:
        if i.name ==user.name and i.pass_word == user.pass_word:
            request.session['username'] = i.name
            request.session['is_admin'] = i.is_admin
            request.session.set_expiry(1800)  # session过期时间：30分钟
            print("登陆成功：" + name + ' ' + pass_word)
            return render(request, 'home/fmain.html')
    print("登陆失败")
    return render(request, 'user/loginFailure.html')


def homeTitle(request):
    return render(request, 'top.html')


def homeLeft(request):
    if request.session.get('is_admin'):
        return render(request, 'home/adminLeft.html')
    else:
        return render(request, 'home/staffLeft.html')


# def homeMain(request):
#     return render(request, 'home/mainFrame/adminDocumentary.html')


def registePage(request):
    return render(request, 'user/registe.html')


def registe(request):
    name = request.POST['username']
    pass_word = request.POST['password']
    foo = request.POST['identity']
    if (foo == 'manager'):
        is_admin = True
    else:
        is_admin = False
    print("注册信息：" + name + ' ' + ' ' + pass_word + ' ' + str(is_admin))
    user = User(name, pass_word, is_admin)
    list = User.objects.all()
    if user in list:  # 神奇的默认只比较了主键orz
        return render(request, 'user/registeFailure.html')
    else:
        user.save()
        return render(request, 'user/registeSuccess.html')


def logout(request):
    if request.session.get('username', None) is not None:
        del request.session['username']
    if request.session.get('is_admin', None) is not None:
        del request.session['is_admin']
    return render(request,'user/logout.html')



