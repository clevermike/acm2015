#!/usr/bin/env python
# coding :utf-8
#author :dongchen

from django.conf.urls import url

from ballon import views

urlpatterns = [
    url(r'^/?$', views.login),
]