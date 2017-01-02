#!/usr/bin/env python
#coding=utf-8
#author:dongchen

from django.conf.urls import url
from django.views.decorators.cache import cache_page
from ranklist import views

urlpatterns = [
    url(r'^/?$', cache_page(10)(views.show_ranklist)),
    url(r'^display/?$', views.show_ranklist_display),
    url(r'^concern/?$', cache_page(10)(views.show_concerned_ranklist)),
    url(r'^set_concern/?$', views.set_concern_teams),
    url(r'^reset_concern/?$', views.reset_concern_teams),
]