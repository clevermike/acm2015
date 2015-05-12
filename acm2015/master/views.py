#!/usr/bin/env python
#coding=utf-8
#author:dongchen
import os
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from settings import FILE_PATH, EXPORT
from tools.BoardGenerator import BoardGenerator
from tools.CsvReader import CsvReader
from tools.CsvWriter import CsvWriter
from web.models import Team


def login(request):
    errors = []

    if request.method == 'GET':
        if request.user.is_authenticated() and request.user.is_superuser:
            return render_to_response('admin_index.html',
                                      locals(),
                                      context_instance=RequestContext(request))

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
            return HttpResponseRedirect('.')

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
            teams = CsvReader.get_item_list(tab_file, 'team.csv')
            for t in teams:
                if User.objects.filter(username=t['account']):
                    errors.append(t['account']+' has already exist')
                else:
                    account = User.objects.create_user(username=t['account'], password=t['password'])
                    account.save()
                    team = Team(id=t['id'], account=account)
                    if 'displayname' in t:
                        team.name = t['displayname']
                    if 'nickname' in t:
                        team.chName = t['nickname']
                    if 'school' in t:
                        team.school = t['school']
                    if 'isstar' in t:
                        team.isStar = (t['isstar'] == '1')
                    if 'isgirl' in t:
                        team.isGirl = (t['isgirl'] == '1')
                    if 'seatid' in t:
                        team.seatId = t['seatid']
                    if 'coach' in t:
                        team.coach = t['coach']
                    if 'player1' in t:
                        team.player1 = t['player1']
                    if 'player2' in t:
                        team.player2 = t['player2']
                    if 'player3' in t:
                        team.player3 = t['player3']
                    team.save()
                    errors.append(t['account']+' load OK')

    return render_to_response('admin_import.html',
                              locals(),
                              context_instance=RequestContext(request))


def export(request):
    if request.method == 'POST':
        no = request.POST.get('no')
        return export_file(no)
    else:
        return render_to_response('admin_export.html',
                              locals(),
                              context_instance=RequestContext(request))


def export_file(no):
    generator = BoardGenerator()
    problems = generator.get_problems()
    board = generator.make_real_board()
    file_name = EXPORT['name'][no]
    file_path = (FILE_PATH + file_name).encode('utf-8')
    if no == '4':
        board = filter2(board)
        CsvWriter.set_item_list(board, file_name, EXPORT['keys2'], EXPORT['header2'])
    else:
        board = filter(no, board)
        CsvWriter.set_item_list(board, file_name, EXPORT['keys'], EXPORT['header'])
    response = HttpResponse(open(file_path, 'r'), content_type='APPLICATION/OCTET-STREAM') #设定文件头，这种设定可以让任意文件都能正确下载，而且已知文本文件不是本地打开
    response['Content-Disposition'] = 'attachment; filename='+file_name.encode('utf-8')  #设定传输给客户端的文件名称
    response['Content-Length'] = os.path.getsize(file_path)#传输给客户端的文件大小
    return response

def filter(no, board):
    result = []
    for b in board:
        if b['isWinner'] or b['isGold']:
	    if b['isGirl']:
	        b['isGirl'] = u'女队'
	    else:
		b['isGirl'] = u''
	    b['medal'] = u'金奖'
            result.append(b)
        elif b['isSilver']:
	    if b['isGirl']:
	        b['isGirl'] = u'女队'
	    else:
		b['isGirl'] = u''
	    b['medal'] = u'银奖'
            result.append(b)
        elif b['isBronze']:
	    if b['isGirl']:
	        b['isGirl'] = u'女队'
	    else:
		b['isGirl'] = u''
	    b['medal'] = u'铜奖'
            result.append(b)
    return result

def filter2(board):
    result = []
    for b in board:
        if not b['isStar']:
            pos = findpos(result, 'school', b['school'])
            if pos == -1:
                node = {
                    'school' : b['school'],
                    'goldNum' : 0,
                    'silverNum' : 0,
                    'bronzeNum' : 0,
                }
                result.append(node)
            if b['isGold'] or b['isWinner']:
                result[pos]['goldNum'] += 1
            if b['isSilver']:
                result[pos]['silverNum'] += 1
            if b['isBronze']:
                result[pos]['bronzeNum'] += 1
    return result

def findpos(list, key, value):
    for index, item in enumerate(list):
        if item[key] == value:
            return index
    return -1
