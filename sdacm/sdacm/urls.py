#!/usr/bin/env python
# coding=utf-8
# author:dongchen
import datetime
import logging
import os
import shutil

from apscheduler.scheduler import Scheduler
from django.conf.urls import include, url

from django.contrib import admin

from config import RESULT_PATH, RESULT_PATH_COPY, BOARD_OFF_TIME
from web import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', views.index),
    url(r'^ranklist/', include('ranklist.urls')),
    url(r'^print/', include('printer.urls')),
    url(r'^ballon/', include('ballon.urls')),
    url(r'^master/', include('master.urls')),
    url(r'^clock/', include('clock.urls')),
]

logging.basicConfig()
sched = Scheduler()


@sched.interval_schedule(seconds=2)
def cron():

    END_TIME = datetime.datetime.strptime(BOARD_OFF_TIME, '%Y-%m-%d %H:%M:%S')
    logging.basicConfig()
    if datetime.datetime.now() < END_TIME:
        try:
            if os.path.exists(RESULT_PATH):
                shutil.copyfile(RESULT_PATH, RESULT_PATH_COPY)
        except Exception:
            logging.error('fuck', Exception)


sched.start()
