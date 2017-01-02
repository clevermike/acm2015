#!/usr/bin/env python
# coding=utf-8
#author :dongchen

from django.conf.urls import url

from clock import views

urlpatterns = [
    url(r'display/?$', views.display),
]