"""GraduationProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from PhoneNumberReservation import testdb
from PhoneNumberReservation import views as reservation_views  # 导入views.py文件中的函数
from ReservationManagement import views as reservation_management_views
from StatisticalSummary import views as statistical_summary_views
from User import views as user_views

# url映射关系。
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', user_views.index),
    path('index/login', user_views.login),
    path('index/homeTitle', user_views.homeTitle),
    path('index/homeLeft', user_views.homeLeft),

    path('registePage/', user_views.registePage),
    path('registePage/registe', user_views.registe),
    path('logout',user_views.logout),


    path('hello/',reservation_views.hello),  # 测试
    path('testdbInsert/',testdb.testdbInsert),  # 测试
    path('testdbGet/', testdb.testdbGet),  # 测试
    path('testdbUpdate/', testdb.testdbUpdate),  # 测试
    path('testdbDetele/', testdb.testdbDetele),  # 测试
]
