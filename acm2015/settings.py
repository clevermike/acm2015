#!/usr/bin/env python
# coding=utf-8
#author:dongchen

import types

#pc2的路径
PC2_PATH = '/usr/local/pc2/bin/'

#存放文件到路径
FILE_PATH = '/var/www/acm2015/static/files/'

#results.xml的路径
RESULT_PATH = PC2_PATH + 'results.xml'

#results.xml的副本的路径，副本在比赛结束前一小时不会更新（解析的是这个副本）
RESULT_PATH_COPY = PC2_PATH + 'results_copy.xml'

#比赛发奖的总队伍数
NUM_GOLD = 11    #金牌
NUM_SILVER = 21  #银牌
NUM_BRONZE = 32  #铜牌

#开始时间
START_TIME = '2015-05-10 09:00:00'

#结束时间
END_TIME = '2015-05-10 14:00:00'

#封榜时间
BOARD_OFF_TIME = '2015-05-10 13:00:00'

#会话保持时间（打印服务会话，分钟）
USER_KEEP_ALIVE = 30

#气球的颜色
BALLON_COLOR = {
    'A': ['red', '红色'],
    'B': ['yellow', '黄色'],
    'C': ['green','深绿'],
    'D': ['royalblue','浅蓝'],
    'E': ['purple','深紫'],
    'F': ['darkred','酒红'],
    'G': ['plum','浅紫'],
    'H': ['blue','深蓝'],
    'I': ['palegreen','浅绿'],
    'J': ['orangered','橙色'],
    'K': ['pink','粉色'],
    'L': ['white','白色']
}

# 打印机
PRINTER = {
    'major': 'HP1',
    'group': ['HP2', 'HP3', 'HP4'],
}

#pc^2解析需要的字段
KEYS = {
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

TYPES = {
    'id': types.IntType,
    'title': types.UnicodeType,
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

# 导出信息的参数
EXPORT = {
    'keys': ['school', 'medal', 'rank', 'chName', 'name', 'coach', 'player1', 'player2', 'player3', 'isGirl'],
    'header': [u'学校', u'奖项', u'排名', u'队伍名（中文）', u'队伍名（英文）', u'教练', u'队员1', u'队员2', u'队员3', u'女队'],
    'name':{
        '1':u'获奖名单.txt',
        '4':u'获奖数量汇总.txt',
    },
    'keys2': ['school', 'goldNum', 'silverNum', 'bronzeNum'],
    'header2': [u'学校', u'金奖数', u'银奖数', u'铜奖数']
}
