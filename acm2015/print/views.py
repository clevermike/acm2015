#!/usr/bin/env python
#coding:utf-8
#author:dongchen
import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from settings import USER_KEEP_ALIVE
from tools.Printer import Printer
from web.models import Team, Code


def login(request):
    errors = []
    if request.user.is_active and 'logintime' in request.session:
        # print request.session['logintime']
        # print datetime.datetime.now()
        # print datetime.datetime.now() - datetime.datetime.strptime(request.session['logintime'], '%Y-%m-%d %H:%M:%S')
        if datetime.datetime.now() - datetime.datetime.strptime(request.session['logintime'], '%Y-%m-%d %H:%M:%S') > USER_KEEP_ALIVE:
            del request.session['logintime']
            auth.logout(request)
            return HttpResponseRedirect('/print')

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
    if request.user.is_authenticated() and not request.user.is_superuser:
        request.session['logintime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return render_to_response('print_index.html')
    return render_to_response('print_login.html',
                              locals(),
                              context_instance=RequestContext(request))

@csrf_exempt
def submit_code(request):
    if not request.user.is_authenticated():
        pass
    elif request.method == 'POST':
        team = Team.objects.get(account=request.user)
        text = request.POST.get('code')
        valid = request.POST.get('print')
        code = Code.objects.create(team=team, text=text, is_print=False)
        Printer().print_code(code)
        if valid != 'acm1234+-*/':
            pass
        elif code.is_print:
            return render_to_response('print_ok.html')
        else:
            return render_to_response('print_fail.html')
    return HttpResponseRedirect('/print')