# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test,Contact,Tag

'''
为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin。
比如，我们之前在 TestModel 中已经创建了模型 Test 。修改 TestModel/admin.py:
'''
# Register your models here.
# admin.site.register(Test)
# admin.site.register([Test, Contact, Tag])

'''
# 不显示age
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Tag])
'''
'''
# age 属性隐藏
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'fields': ('age',),
            'classes': ('collapse',),
        }]
    )
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
'''

'''
# tag 内联contact
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
'''

'''
# 显示多个栏目，list_display
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
'''

# 增加搜索栏
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])