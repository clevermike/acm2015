#!/usr/bin/env python
# coding=utf-8
#author :dongchen
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from config import END_TIME, START_TIME


def display(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_time = START_TIME
    end_time = END_TIME
    return render_to_response('clock_display.html',
                              locals(),
                              context_instance=RequestContext(request))

