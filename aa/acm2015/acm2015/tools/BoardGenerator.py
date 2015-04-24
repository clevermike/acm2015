#!/usr/bin/env python
# coding:utf-8
#author:dongchen
import logging
from xml.dom import minidom
from config import key_list
from tools.XmlReader import XmlReader
from settings import XML_PATH, XML_PATH_COPY, TEAM_NUM_AWARDED
from web.models import Team, Ballon


class BoardGenerator:

    def __init__(self):
        self.__openXmlNode = minidom.parse(XML_PATH_COPY).documentElement
        self.__realXmlNode = minidom.parse(XML_PATH).documentElement
        self.__header = None
        self.__problems = None
        self.__openStanding = None
        self.__realStanding = None
        self.__realStandingDict = dict()

    def get_header(self):
        if self.__header is None:
            self.__header = XmlReader.get_item(self.__realXmlNode,
                                               'standingsHeader',
                                               key_list['header_keys'])
        return self.__header

    def get_problems(self):
        if self.__problems is None:
            self.__problems = XmlReader.get_item_list(self.__openXmlNode,
                                                      'problem',
                                                      key_list['problem_keys'])
            self.__real_problems = XmlReader.get_item_list(self.__realXmlNode,
                                                           'problem',
                                                           key_list['problem_keys'])
            for p, rp in zip(self.__problems, self.__real_problems):
                p['attempts'] = rp['attempts']
        return self.__problems

    def make_board(self):
        self.get_standing()
        self.get_real_standing()
        self.get_real_standing_dict()
        self.complete(self.__openStanding)
        return self.__openStanding

    def complete(self, standing):
        self.complete_team_info(standing)
        self.complete_first_solved(standing)
        self.complete_rank(standing)
        self.complete_medal(standing)
        self.complete_pending()

    def get_ballon_list(self):
        self.get_real_standing()
        result = []
        for rst in self.__realStanding:
            for index, rsts in enumerate(rst['status']):
                obj = {}
                if rsts['isSolved']:
                    obj['team'] = Team.objects.get(id=rst['teamId'])
                    obj['problem'] = chr(ord('A')+index)
                    obj['time'] = rsts['solutionTime']
                    result.append(obj)
        result = sorted(result, key=lambda s: s['time'])
        for res in result:
            if not Ballon.objects.filter(team=res['team'], problem=res['problem']):
                Ballon.objects.create(team=res['team'], problem=res['problem'])
        return result

    def get_standing(self):
        if self.__openStanding is None:
            self.__openStanding = XmlReader.get_item_list(self.__openXmlNode,
                                                          'teamStanding',
                                                          key_list['team_keys'])

    def get_real_standing(self):
        if self.__realStanding is None:
            self.__realStanding = XmlReader.get_item_list(self.__realXmlNode,
                                                          'teamStanding',
                                                          key_list['team_keys'])

    def get_real_standing_dict(self):
        for rst in self.__realStanding:
            self.__realStandingDict[rst['teamId']] = rst

    def complete_team_info(self, standing):
        for st in standing:
            print st['teamId']
            if not Team.objects.filter(id=st['teamId']):
                # logging.warning('team'+st['teamId']+'is unload!')
                continue
            team = Team.objects.get(id=st['teamId'])
            st['school'] = team.school
            st['isFriend'] = team.is_friend
            st['teamName'] = team.team_name

    def complete_first_solved(self, standing):
        for st in standing:
            for sts in st['status']:
                if sts['isSolved'] and sts['solutionTime'] == self.__problems[sts['index']-1]['bestSolutionTime']:
                    sts['isFirstSolved'] = True

    def complete_rank(self, standing):
        friend_team_num = 0
        school_list = []
        for st in standing:
            if st['isFriend']:
                if st['solved'] > 0:
                    friend_team_num += 1
                st['tRank'] = ''
                st['sRank'] = ''
            else:
                st['tRank'] = st['rank'] - friend_team_num
                if st['school'] not in school_list:
                    st['sRank'] = len(school_list) + 1
                    school_list.append(st['school'])

    def complete_medal(self, standing):
        gold = int(0.1 * TEAM_NUM_AWARDED + 0.5)
        silver = int(0.3 * TEAM_NUM_AWARDED + 0.5)
        bronze = int(0.6 * TEAM_NUM_AWARDED + 0.5)
        for st in standing:
            if st['tRank'] == '' or st['solved'] == 0:
                continue
            if st['tRank'] == 1:
                st['isWinner'] = True
            if 1 < st['tRank'] <= gold:
                st['isGold'] = True
            if gold < st['tRank'] <= silver:
                st['isSilver'] = True
            if silver < st['tRank'] <= bronze:
                st['isBronze'] = True
            if bronze < st['tRank'] and st['solved'] > 0:
                st['isIron'] = True

    def complete_pending(self):
        for st in self.__openStanding:
            rst = self.__realStandingDict[st['teamId']]
            for sts, rsts in zip(st['status'], rst['status']):
                if rsts['attempts'] > sts['attempts']:
                    sts['isPending'] = True
                    sts['attempts'] = rsts['attempts']

