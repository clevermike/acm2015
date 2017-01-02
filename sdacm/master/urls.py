#!/usr/bin/env python
#coding=utf-8
#author:dongchen

from django.conf.urls import url

from django.contrib import admin

from master import views

admin.autodiscover()

urlpatterns = [
    url(r'^/?$', views.login),
    url(r'^logout/?$', views.logout),
    url(r'^import/?$', views.reload_team),
    url(r'^export/?$', views.export),
]
