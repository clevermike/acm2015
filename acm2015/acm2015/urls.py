#!/usr/bin/env python
#coding=utf-8
#author:dongchen

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'web.views.index'),
    url(r'^ranklist/', include('ranklist.urls')),
    url(r'^print/', include('print.urls')),
    url(r'^ballon/', include('ballon.urls')),
    url(r'^master/', include('master.urls')),
    url(r'^clock/', include('clock.urls')),
)
