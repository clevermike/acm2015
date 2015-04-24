#!/usr/bin/env python
#coding:utf-8
#author:dongchen

from xml.dom import minidom
from config import type_list, key_list


class XmlReader:
    '''
    解析results.xml的类
    '''

    @staticmethod
    def get_value(node, key):
        return type_list[key](node.getAttribute(key))

    @staticmethod
    def get_item(parent_node, tag_name, keys):
        node_list = parent_node.getElementsByTagName(tag_name)
        result = {}
        for key in keys:
            result[key] = XmlReader.get_value(node_list[0], key)
        return result

    @staticmethod
    def get_item_list(parent_node, tag_name, keys):
        node_list = parent_node.getElementsByTagName(tag_name)
        result = []
        for node in node_list:
            obj = {}
            for key in keys:
                obj[key] = XmlReader.get_value(node, key)
                if tag_name == 'teamStanding':
                    obj['status'] = XmlReader.get_item_list(node,
                                                            'problemSummaryInfo',
                                                            key_list['status_keys'])
            result.append(obj)
        return result