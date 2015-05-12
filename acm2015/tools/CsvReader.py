#!/usr/bin/env python
#coding=utf-8
#author:dongchen
import csv
from settings import FILE_PATH


class CsvReader:

    def __init__(self):
        pass

    @staticmethod
    def get_item_list(content, file_name):
        csv_path = FILE_PATH + file_name
        open(csv_path, 'w').write(content)
        file_content = csv.reader(open(csv_path, 'r'), delimiter='\t')
        header = file_content.next()
        result = []
        for line in file_content:
            obj = {}
            for index, key in enumerate(header):
                obj[key] = line[index]
            result.append(obj)
        return result
