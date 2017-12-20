# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test,Contact,Tag

# Register your models here.
# admin.site.register(Test)
# admin.site.register([Test, Contact, Tag])
'''

class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
'''

'''
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])

'''
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