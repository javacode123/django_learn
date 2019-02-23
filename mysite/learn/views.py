# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def get_model(request):
    name = request.GET.get('name', 'zjl')  # 设置默认值
    print name
    return HttpResponse(name)


def index(request):
    # 自动查找 app 下的 templates 中的文件
    msg = u'我在学习 django!'  # 字符渲染
    for_msg = ['java', 'python', 'c++']
    return render(request, 'home.html', {'msg': msg, 'for_msg': for_msg})


# ?a=9&b=9
def add(request):
    # 接收参数
    a = request.GET.get('a', 0)  # 设置默认值
    b = request.GET.get('b', 0)  # 设置默认值
    return HttpResponse(str(int(a) + int(b)))


# 使用 /3/4/
def add2(request, a, b):
    return HttpResponse(str(int(a) + int(b)))
