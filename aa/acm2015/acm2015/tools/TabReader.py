#!/usr/bin/env python
#coding:utf-8
#author:dongchen
import csv

class TabReader:

    @staticmethod
    def get_item_list(content, file_name):
        csv_path = '/var/www/acm2015/static/files/' + file_name
        open(csv_path, 'w').write(content.replace('\t', ','))
        file_content = csv.reader(open(csv_path, 'r'))
        header = file_content.next()
        result = []
        for line in file_content:
            obj = {}
            for index, key in enumerate(header):
                obj[key] = line[index]
            result.append(obj)
        return result
