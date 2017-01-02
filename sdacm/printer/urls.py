#!/usr/bin/env python
#coding=utf-8
#author:dongchen
from django.conf.urls import url

from printer import views

urlpatterns = [
    url(r'^/?$', views.login),
    url(r'^logout/?$', views.logout),
    url(r'^result/?$', views.submit_code),
    # url(r'^2ol5aCm/360916/PFxt3V/admIn/', include('admin.urls')),
]
