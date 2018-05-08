from django.db import models
from django.contrib import admin

# Create your models here.
"""
以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，
数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
"""


class User(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    pass_word = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)  # 是否是管理员，默认不是
    phone_number = models.IntegerField(default=0)  # 手中号码个数


admin.site.register(User)  # 注册该数据模型到 admin

