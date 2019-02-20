# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # 自动查找 app 下的 templates 中的文件
    return render(request, 'home.html')

# ?a=9&b=9
def add(request):
    # 接收参数
    a = request.GET.get('a', 0)  # 设置默认值
    b = request.GET.get('b', 0)  # 设置默认值
    return HttpResponse(str(int(a) + int(b)))


# 使用 /3/4/
def add2(request, a, b):
    return HttpResponse(str(int(a) + int(b)))
