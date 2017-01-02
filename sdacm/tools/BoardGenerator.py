#!/usr/bin/env python
# coding=utf-8
#author:dongchen
from xml.dom import minidom
from tools.XmlReader import XmlReader
from config import *
from web.models import Team, Ballon


class BoardGenerator:

    def __init__(self):
        self.__openXmlNode = minidom.parse(RESULT_PATH_COPY).documentElement
        self.__realXmlNode = minidom.parse(RESULT_PATH).documentElement
        self.__header = None
        self.__problems = None
        self.__real_problems = None
        self.__openStanding = None
        self.__realStanding = None
        self.__realStandingDict = dict()

    def get_header(self):
        if self.__header is None:
            self.__header = XmlReader.get_item(self.__realXmlNode,
                                               'standingsHeader',
                                               KEYS['header_keys'])
        return self.__header

    def get_problems(self):
        if self.__problems is None:
            self.__problems = XmlReader.get_item_list(self.__openXmlNode,
                                                      'problem',
                                                      KEYS['problem_keys'])
            self.__real_problems = XmlReader.get_item_list(self.__realXmlNode,
                                                           'problem',
                                                           KEYS['problem_keys'])
            for p, rp in zip(self.__problems, self.__real_problems):
                p['attempts'] = rp['attempts']
        return self.__problems

    def make_board(self):
        self.get_standing()
        self.get_real_standing()
        self.get_real_standing_dict()
        self.complete(self.__openStanding)
        self.complete_pending()
        return self.__openStanding

    def make_real_board(self):
        self.get_real_standing()
        self.complete(self.__realStanding)
        return self.__realStanding

    def complete(self, standing):
        self.complete_team_info(standing)
        self.complete_first_solved(standing)
        self.complete_rank(standing)
        self.complete_medal(standing)

    def get_ballon_list(self):
        self.get_problems()
        self.get_real_standing()
        result = []
        for rst in self.__realStanding:
            for index, rsts in enumerate(rst['status']):
                obj = {}
                if rsts['isSolved']:
                    obj['isFirst'] = True if rsts['solutionTime'] == self.__real_problems[rsts['index']-1]['bestSolutionTime'] else False
                    obj['team'] = Team.objects.get(id=rst['teamId'])
                    obj['problem'] = chr(ord('A')+index)
                    obj['time'] = rsts['solutionTime']
                    result.append(obj)
        result = sorted(result, key=lambda s: s['time'], reverse=True)
        for res in result:
            if not Ballon.objects.filter(team=res['team'], problem=res['problem']):
                Ballon.objects.create(team=res['team'], problem=res['problem'])
        return result

    def get_standing(self):
        if self.__openStanding is None:
            self.__openStanding = XmlReader.get_item_list(self.__openXmlNode,
                                                          'teamStanding',
                                                          KEYS['team_keys'])

    def get_real_standing(self):
        if self.__realStanding is None:
            self.__realStanding = XmlReader.get_item_list(self.__realXmlNode,
                                                          'teamStanding',
                                                          KEYS['team_keys'])

    def get_real_standing_dict(self):
        for rst in self.__realStanding:
            self.__realStandingDict[rst['teamId']] = rst

    def complete_team_info(self, standing):
        for st in standing:
            if not Team.objects.filter(id=st['teamId']):
                st['school'] = ''
                st['isStar'] = False
		st['isGirl'] = False
                st['name'] = ''
                st['chName'] = ''
                st['coach'] = ''
                st['player1'] = ''
                st['player2'] = ''
                st['player3'] = ''
                st['seatId'] = ''
            else:
                team = Team.objects.get(id=st['teamId'])
                st['school'] = team.school
                st['isStar'] = team.isStar
		st['isGirl'] = team.isGirl
                st['name'] = team.name
                st['chName'] = team.chName
                st['coach'] = team.coach
                st['player1'] = team.player1
                st['player2'] = team.player2
                st['player3'] = team.player3
                st['seatId'] = team.seatId

    def complete_first_solved(self, standing):
        for st in standing:
            for sts in st['status']:
                if sts['isSolved'] and sts['solutionTime'] == self.__problems[sts['index']-1]['bestSolutionTime']:
                    sts['isFirstSolved'] = True

    def complete_rank(self, standing):
        team_num = 1
        school_list = []
        for st in standing:
            if st['isStar']:
                st['teamRank'] = ''
                st['schoolRank'] = ''
            else:
                st['teamRank'] = team_num
                team_num += 1
                if st['school'] not in school_list:
                    st['schoolRank'] = len(school_list) + 1
                    school_list.append(st['school'])

    def complete_medal(self, standing):
        gold = NUM_GOLD
        silver = gold + NUM_SILVER
        bronze = silver + NUM_BRONZE
        for st in standing:
            st['isWinner'] = False
            st['isGold'] = False
            st['isSilver'] = False
            st['isBronze'] = False
            st['isIron'] = False
            st['prize'] = u''
            if st['teamRank'] == '' or st['solved'] == 0:
                continue
            if st['teamRank'] == 1:
                st['isWinner'] = True
                st['prize'] = u'冠军'
            elif 1 < st['teamRank'] <= gold:
                st['isGold'] = True
                st['prize'] = u'金牌'
            elif gold < st['teamRank'] <= silver:
                st['isSilver'] = True
                st['prize'] = u'银牌'
            elif silver < st['teamRank'] <= bronze:
                st['isBronze'] = True
                st['prize'] = u'铜牌'
            elif bronze < st['teamRank'] and st['solved'] > 0:
                st['isIron'] = True
                st['prize'] = u'铁牌'

    def complete_pending(self):
        for st in self.__openStanding:
            rst = self.__realStandingDict[st['teamId']]
            for sts, rsts in zip(st['status'], rst['status']):
                if rsts['attempts'] > sts['attempts']:
                    sts['isPending'] = True
                    sts['attempts'] = rsts['attempts']

