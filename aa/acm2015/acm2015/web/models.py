#!/usr/bin/env python
#coding:utf-8
#author:dongchen

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    '''
    id:队伍编号
    account:队伍账户，包含帐号密码等信息
    team_name:队伍名称
    school:学校
    is_friend:是否友情参赛
    is_girl:是否女队
    seat_id:座位号，比赛座位标识
    '''
    id = models.SmallIntegerField(primary_key=True, unique=True)
    account = models.OneToOneField(User, unique=True)
    team_name = models.CharField(max_length=50, default='', blank=True)
    school = models.CharField(max_length=50, default='', blank=True)
    is_friend = models.BooleanField(default=False, blank=False)
    is_girl = models.BooleanField(default=False, blank=False)
    seat_id = models.CharField(max_length=10, default='', blank=False)


class Code(models.Model):
    '''
    id:唯一标识
    team:队伍
    text:代码
    submit_time:提交时间
    print_time:打印时间（进入打印队列）
    is_print:是否已打印
    '''
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team)
    text = models.TextField(max_length=30000, blank=False)
    submit_time = models.DateTimeField(auto_now_add=True)
    print_time = models.DateTimeField(blank=True, null=True)
    is_print = models.BooleanField(default=False)


class Ballon(models.Model):
    '''
    id:唯一标识
    team:队伍
    problem:题目号
    is_placed:是否已放置
    '''
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team)
    problem = models.CharField(max_length=5, null=False)
    is_placed = models.BooleanField(default=False)