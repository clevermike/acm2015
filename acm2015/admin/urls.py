#!/usr/bin/env python
#coding:utf-8
#author:dongchen

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('admin.views',
    url(r'^/?$', 'login'),
    url(r'^logout/?$', 'logout'),
    url(r'^team/reload?$', 'reload_team'),
    url(r'^team/?$', 'show_team_list'),
)
