#!/usr/bin/env python
# coding:utf-8
#author:dongchen

import types
import datetime

#pc2的路径
#PC2_PATH = '/home/dongchen/pc2-9.2.4/bin/'
PC2_PATH = '/home/acm/pc2-9.2.4/bin/'

#results.xml的路径
XML_PATH = PC2_PATH + 'results.xml'

#results.xml的副本的路径，副本在比赛结束前一小时不会更新（解析的是这个副本）
XML_PATH_COPY = PC2_PATH + 'results_copy.xml'

#比赛发奖的总队伍数标准
TEAM_NUM_AWARDED = 10

#封榜时间
BOARD_OFF_TIME = datetime.datetime(year=2015,month=4,day=19,hour=13,minute=06)

#保持会话时间
USER_KEEP_ALIVE = datetime.timedelta(minutes=30)

#气球的颜色
BALLON_COLOR = {
    'A': '',
    'B': '',
    'C': '',
    'D': '',
    'E': '',
    'F': '',
    'G': '',
    'H': '',
    'I': '',
    'J': '',
    'K': '',
    'L': ''
}

#pc^2解析需要的字段
key_list = {
    'problem_keys': [
        'id',
        'title',
        'attempts',
        'numberSolved',
        'bestSolutionTime'
    ],
    'team_keys': [
        'rank',
        'solved',
        'teamId',
        'teamName',
        'points'
    ],
    'status_keys': [
        'index',
        'isPending',
        'isSolved',
        'attempts',
        'solutionTime',
    ],
    'header_keys': [
        'currentDate',
        'problemCount',
        'totalAttempts',
        'totalSolved',
    ]
}


type_list = {
    'id': types.IntType,
    'title': types.StringType,
    'attempts': types.IntType,
    'numberSolved': types.IntType,
    'bestSolutionTime': lambda x: -1 if x == '' else int(x),
    'rank': types.IntType,
    'solved': types.IntType,
    'teamId': types.IntType,
    'teamName': types.UnicodeType,
    'points': types.IntType,
    'index': types.IntType,
    'isPending': lambda x: x == 'true',
    'isSolved': lambda x: x == 'true',
    'solutionTime': types.IntType,
    'currentDate': types.StringType,
    'problemCount': types.IntType,
    'totalAttempts': types.IntType,
    'totalSolved': types.IntType,
}
