#!/usr/bin/env python
#coding:utf-8
#author:dongchen

import types

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

