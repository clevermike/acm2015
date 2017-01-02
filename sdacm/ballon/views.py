#!/usr/bin/env python
# coding :utf-8
#author :dongchen
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from config import BALLON_COLOR
from tools.BoardGenerator import BoardGenerator
from web.models import Ballon


def login(request):
    errors = []

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user:
            errors.append('Incorrect username or password')
        elif user.username != 'ballonserver':
            errors.append('Permission denied')
        else:
            auth.login(request, user)
    if request.user.is_authenticated() and request.user.username == 'ballonserver':
        return show(request)

    return render_to_response('ballon_login.html',
                              locals(),
                              context_instance=RequestContext(request))

def show(request):
    generator = BoardGenerator()
    ballon_list = generator.get_ballon_list()
    if request.method == 'POST':
        if request.POST.has_key('password'):
            pass
        else:
            bid = request.POST.get('id')
            ballon = Ballon.objects.get(id=int(bid))
            ballon.isPlaced ^= 1
            ballon.save()
        return HttpResponseRedirect('.')

    for bl in ballon_list:
        ballon = Ballon.objects.get(team=bl['team'], problem=bl['problem'])
        bl['id'] = ballon.id
        bl['isPlaced'] = ballon.isPlaced
        bl['color'] = BALLON_COLOR[bl['problem']]

    return render_to_response('ballon_show.html',
                              locals(),
                              context_instance=RequestContext(request))
