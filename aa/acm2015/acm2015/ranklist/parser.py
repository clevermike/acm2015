#!/usr/bin/env python
#coding:utf-8
#author:dongchen

from xml.dom import minidom
from config import key_list, type_list
from settings import XML_PATH, XML_PATH_IN


class Parser:
    '''
    解析results.xml的类
    '''

    def __init__(self):
        self.__filePath = XML_PATH
        self.__filePathBak = XML_PATH_IN
        self.__docElement = minidom.parse(XML_PATH_IN).documentElement
        self.__docElementComp = minidom.parse(XML_PATH).documentElement

    def get_problem_list(self):
        return Parser.get_parse_result(self.__docElement, 'problem', 'problem_keys')

    def get_team_standing(self):
        return Parser.get_parse_result(self.__docElement, 'teamStanding', 'team_keys')

    def get_global_info(self):
        return Parser.get_parse_result(self.__docElement, 'standingsHeader', 'header_keys')[0]

    @staticmethod
    def get_value(node, key):
        return type_list[key](node.getAttribute(key))

    @staticmethod
    def get_parse_result(node, tag_name, key_type):
        node_list = node.getElementsByTagName(tag_name)
        result = []
        for node in node_list:
            obj = {}
            for key in key_list[key_type]:
                obj[key] = Parser.get_value(node, key)
            if tag_name == 'teamStanding':
                obj['submissions'] = Parser.get_parse_result(node, 'problemSummaryInfo', 'submission_keys')
            result.append(obj)
        return result


# a = Parser()
# print a.get_problem_list()
# print a.get_team_standing()