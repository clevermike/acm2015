#!/usr/bin/env python
#coding:utf-8
#author:dongchen

from web.models import Team
from settings import TEAM_NUM_AWARDED

class Completion:

    def __init__(self):
        return

    @staticmethod
    def complete(problems, team_standing):
        Completion.complete_first_solved(problems, team_standing)
        Completion.complete_rank(team_standing)
        Completion.complete_medal(team_standing)
        return

    @staticmethod
    def complete_first_solved(problems, team_standing):
        for ts in team_standing:
            for tss in ts['submissions']:
                if tss['isSolved'] and tss['solutionTime'] == problems[tss['index']-1]['bestSolutionTime']:
                    tss['isFirstSolved'] = True

    @staticmethod
    def complete_rank(team_standing):
        friend_team_num = 0
        for ts in team_standing:
            if ts['teamName'][0] != '*':
                ts['rank'] -= friend_team_num
            else:
                if ts['solved'] > 0:
                    friend_team_num += 1
                ts['rank'] = ''

    @staticmethod
    def complete_medal(team_standing):
        gold = int(0.1 * TEAM_NUM_AWARDED + 0.5)
        silver = int(0.3 * TEAM_NUM_AWARDED + 0.5)
        bronze = int(0.6 * TEAM_NUM_AWARDED + 0.5)
        for ts in team_standing:
            if ts['rank'] == '':
                continue
            if ts['rank'] == 1:
                ts['isWinner'] = True
            if 1 < ts['rank'] <= gold:
                ts['isGold'] = True
            if gold < ts['rank'] <= silver:
                ts['isSilver'] = True
            if silver < ts['rank'] <= bronze:
                ts['isBronze'] = True
            if bronze < ts['rank'] and ts['solved'] > 0:
                ts['isIron'] = True

    @staticmethod
    def complete_school_info(team_standing):
        return

    @staticmethod
    def get_last_hour_standing(team_standing, team_standing_bak):
        return
