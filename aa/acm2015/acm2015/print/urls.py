#!/usr/bin/env python
#coding:utf-8
#author:dongchen
from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url(r'^/?$', 'print.views.login'),
    url(r'^result/?$', 'print.views.submit_code'),
    # url(r'^2ol5aCm/360916/PFxt3V/admIn/', include('admin.urls')),
)
