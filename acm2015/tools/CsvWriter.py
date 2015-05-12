#!/usr/bin/env python
#coding=utf-8
#author:dongchen

import csv
from settings import FILE_PATH
from tools.BoardGenerator import BoardGenerator


class CsvWriter:

    def __init__(self):
        pass

    @staticmethod
    def set_item_list(content, file_name, keys, header):
        csv_path = (FILE_PATH + file_name).encode('utf-8')
        file = csv.writer(open(csv_path, 'w'), delimiter='\t')
        result = []
        for item in header:
            result.append(item.encode('utf-8'))
        file.writerow(result)
        for line in content:
            result = []
            for key in keys:
                result.append(unicode(line[key]).encode('utf-8'))
            file.writerow(result)


