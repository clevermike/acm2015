#!/usr/bin/env python
#coding:utf-8
#author:dongchen
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from tools.BoardGenerator import BoardGenerator
from tools.TabReader import TabReader
from web.models import Team


def login(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user:
            errors.append('Incorrect username or password')
        elif not user.is_superuser:
            errors.append('Permission denied')
        else:
            auth.login(request, user)
    if request.user.is_authenticated() and request.user.is_superuser:
        return render_to_response('admin_index.html')

    return render_to_response('admin_login.html',
                              locals(),
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('.')


def reload_team(request, show=False):
    if not request.user.is_active:
        return HttpResponseRedirect('.')
    errors = []
    if request.method == 'POST':
        if 'file' not in request.FILES.keys():
            errors.append('Empty file')
        else:
            Team.objects.all().delete()
            User.objects.filter(username__contains='team').delete()
            tab_file = request.FILES['file'].read()
            teams = TabReader.get_item_list(tab_file, 'team.csv')
            for t in teams:
                if User.objects.filter(username=t['account']):
                    errors.append(t['account']+' has already exist')
                else:
                    account = User.objects.create_user(username=t['account'],
                                                       password=t['password'])
                    account.save()
                    team = Team.objects.create(id=t['id'],
                                           account=account,
                                           team_name=t['displayname'],
                                           school=t['school'],
                                           is_friend=(t['isfriend'] == '1'),
                                           is_girl=(t['isgirl'] == '1'),
                                           seat_id=t['seatid'])
                    errors.append(t['account']+' load OK')

    return render_to_response('admin_team_reload.html',
                              locals(),
                              context_instance=RequestContext(request))


def show_team_list(request):
    team_list = Team.objects.all()
    return render_to_response('admin_team_show.html',
                              locals(),
                              context_instance=RequestContext(request))

def contest_setting(request):
    return
