# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test
from django.shortcuts import render


# 数据库操作
def add(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 数据库操作
def chaxun(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # list = Test.objects.filter(id=1)
    # response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "

    '''原来返回的结果
    response = {}
    response['hello'] = response1
    return HttpResponse("<p>" + response + "</p>")
    '''
    # response['hello'] = 'Hello World!'
    # response['hello'] = [1,2,3,4]
    response['hello'] = {'name':'java','pwd':'123'}

    # newlist = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    return render(request, "look.html", response)

# def hello(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'hello.html', context)



# 数据库操作
def change(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=2)
    test1.name = 'JR'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


# 数据库操作
def shanchu(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=2)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")