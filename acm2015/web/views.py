#!/usr/bin/env python
#coding:utf-8
#author:dongchen

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')