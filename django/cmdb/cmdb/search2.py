# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {'na':'ceshi',}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)