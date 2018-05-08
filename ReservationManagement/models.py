from django.db import models
from django.contrib import admin
from User.models import User
# Create your models here.
"""
以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，
数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
"""


class MobileCode4Day(models.Model):  # 每日开放的号段
    date = models.DateField(auto_now_add=True)
    mobile_code_start = models.BigIntegerField(default=0)  # 起始号段
    mobile_code_end = models.BigIntegerField(default=0)  # 终止号段
    reservation_strategy_666 = models.BooleanField(default=False)  # 带666
    reservation_strategy_888 = models.BooleanField(default=False)  # 带888
    reservation_number = models.CharField(max_length=200, null=True,blank=True)  # 手动输入的预留号码


class PhoneNumber(models.Model):  # 开放的号码
    phone_number = models.BigIntegerField(default=0, primary_key=True)  # 号码
    is_achieved = models.BooleanField(default=False)  # 是否被预约
    id_reserved = models.BooleanField(default=False)  # 是否被预留
    user_name = models.CharField(max_length=20,null=True,blank=True)  # 预约人
    date = models.DateField(null=True,blank=True)


admin.site.register(MobileCode4Day)
admin.site.register(PhoneNumber)

