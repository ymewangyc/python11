#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

'''
def hello(request):
    return HttpResponse("Hello world ! ")
'''

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
