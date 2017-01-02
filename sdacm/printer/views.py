#!/usr/bin/env python
#coding=utf-8
#author:dongchen
import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from config import USER_KEEP_ALIVE
from tools.Printer import Printer
from web.models import Team, Code


def login(request):
    errors = []
    if request.user.is_active and 'logintime' in request.session:
        if datetime.datetime.now() - datetime.datetime.strptime(request.session['logintime'], '%Y-%m-%d %H:%M:%S') > datetime.timedelta(USER_KEEP_ALIVE):
            del request.session['logintime']
            auth.logout(request)
            return HttpResponseRedirect('/printer')

    if request.method == 'GET':
        if request.user.is_authenticated() and not request.user.is_superuser and request.user.username != 'ballonserver':
            request.session['logintime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user = request.user
            return render_to_response('print_index.html', locals(), context_instance=RequestContext(request))

    if request.method == 'POST':
        input = request.POST.get('input1')
        valid = request.POST.get('input2')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if input != valid:
            errors.append('Incorrect verifycode')
        elif not user:
            errors.append('Incorrect username or password')
        elif user.is_superuser:
            errors.append('Permission denied')
        else:
            auth.login(request, user)
            return HttpResponseRedirect('.')

    return render_to_response('print_login.html', locals(), context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('.')


@csrf_exempt
def submit_code(request):
    if not request.user.is_authenticated():
        pass
    elif request.method == 'POST':
        team = Team.objects.get(account=request.user)
        text = request.POST.get('code')
        code = Code.objects.create(team=team, text=text, isPrint=False)
        Printer().print_code(code)
        if code.isPrint:
            return render_to_response('print_ok.html')
        else:
            return render_to_response('print_fail.html')
    return HttpResponseRedirect('/printer')

