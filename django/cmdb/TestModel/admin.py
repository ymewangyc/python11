# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test,Contact,Tag

'''
为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin。
比如，我们之前在 TestModel 中已经创建了模型 Test 。修改 TestModel/admin.py:
'''
# Register your models here.
admin.site.register(Test)
