#!/usr/bin/env python
#coding=utf-8
#author:dongchen

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    '''
    id:队伍编号
    account:队伍账户，包含帐号密码等信息
    name:队伍英文名称（默认为官方队名）
    chName:队伍中文名称（默认为中文队名）
    school:学校
    isStar:是否打星
    isGirl:是否女队
    seatId:座位号，比赛座位标识
    coach:教练姓名
    player1:队员1
    player2:队员2
    player3:队员3
    '''
    id = models.SmallIntegerField(primary_key=True, unique=True)
    account = models.OneToOneField(User, unique=True)
    name = models.CharField(max_length=50, default='', blank=True)
    chName = models.CharField(max_length=50, default='', blank=True)
    school = models.CharField(max_length=50, default='', blank=True)
    isStar = models.BooleanField(default=False, blank=False)
    isGirl = models.BooleanField(default=False, blank=False)
    seatId = models.CharField(max_length=10, default='', blank=True)
    coach = models.CharField(max_length=20, default='', blank=True)
    player1 = models.CharField(max_length=20, default='', blank=True)
    player2 = models.CharField(max_length=20, default='', blank=True)
    player3 = models.CharField(max_length=20, default='', blank=True)


class Code(models.Model):
    '''
    id:唯一标识
    team:队伍
    text:代码
    submitTime:提交时间
    isPrint:是否已打印
    '''
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team)
    text = models.TextField(max_length=30000, blank=False)
    submitTime = models.DateTimeField(auto_now_add=True)
    isPrint = models.BooleanField(default=False)


class Ballon(models.Model):
    '''
    id:唯一标识
    team:队伍
    problem:题目号
    isPlaced:是否已放置
    '''
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team)
    problem = models.CharField(max_length=5, null=False)
    isPlaced = models.BooleanField(default=False)