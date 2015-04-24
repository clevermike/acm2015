#!/usr/bin/env python
#coding:utf-8
#author:dongchen

'''
新的省赛排行榜的改进如下：
1、使用regional风格展示成绩，以“提交数/通过时间”为格式
2、增加显示各个题目的提交数和通过数
3、封榜之后提交的特殊颜色显示
4、增加show concerned teams（第四届、第五届未使用）


排行榜展示相关的数据格式：

"problemInfo": {
    "problemId": ,
    "attempts": ,
    "solved": ,
}

"teamStanding": {
    "teamId": ,
    "prize": ,
    "schoolRank": ,
    "school": ,
    "teamName": ,
    "teamRank": ,
    "solved": ,
    "penalty": ,
    "problem": [{
        "problemId": ,
        "isSolved": ,
        "isPending": ,
        "attempts": ,
        "points": ,
    }...]
}

关注指定队伍相关的数据格式：
"setConcernTeams": {
    "teamName": ,
    "teamAlias": ,
}
'''
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response,render
from django.template import RequestContext
from tools.BoardGenerator import BoardGenerator


def show_ranklist(request, is_concern=False, is_display=False):

    generator = BoardGenerator()
    header = generator.get_header()
    problems = generator.get_problems()
    for pb in problems:
        pb['id'] = chr(pb['id']+ord('A')-1)
    print problems
    board = generator.make_board()
    if is_concern:
        standing = []
        for bd in board:
            if unicode(bd['teamId']) in request.session['concern']:
                standing.append(bd)
    else:
        standing = board
    if is_display:
        return render_to_response('ranklist_display.html', locals(),
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('ranklist_show.html', locals(),
                                  context_instance=RequestContext(request))

def show_ranklist_display(request):
    return show_ranklist(request, is_display=True)


def show_concerned_ranklist(request):
    if 'concern' not in request.session:
        request.session['concern'] = []
    return show_ranklist(request, True)

def set_concern_teams(request):
    generator = BoardGenerator()
    problems = generator.get_problems()
    standing = generator.make_board()
    if request.method == 'POST':
        request.session['concern'] = request.POST.getlist('concern_list')
        return show_concerned_ranklist(request)
    if 'concern' not in request.session:
        request.session['concern'] = []
    for st in standing:
        if unicode(st['teamId']) in request.session['concern']:
            st['concern'] = True
    return render_to_response('ranklist_concern.html', locals(),
                              context_instance=RequestContext(request))

def reset_concern_teams(request):
    request.session['concern'] = []
    return HttpResponseRedirect('/ranklist/set_concern')


