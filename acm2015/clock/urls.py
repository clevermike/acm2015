#!/usr/bin/env python
# coding=utf-8
#author :dongchen

from django.conf.urls import patterns, include, url

urlpatterns = patterns('clock.views',
    url(r'display/?$', 'display'),
)