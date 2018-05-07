from django.db import models
from django.contrib import admin
# Create your models here.
# models.py 是Web应用数据库的定义文件，以Python类的形式定义数据库中的各个表；
"""
以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，
数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
"""


# 测试用：
class Test(models.Model):
    name = models.CharField(max_length=20)


admin.site.register(Test)  # 注册该数据模型到 admin
