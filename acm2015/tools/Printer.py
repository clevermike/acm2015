#!/usr/bin/env python
# coding:utf-8
#author:dongchen

import random
import os
import sys


class Printer:

    def __init__(self):
        self.major_printer = 'HP-LaserJet-M1005-MFP'
        self.minor_printers = ['HP-LaserJet-M1005-MFP', 'HP-LaserJet-M1005-MFP', 'HP-LaserJet-M1005-MFP']


    def print_code(self, code):
        try:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            printer = self.minor_printers[int(random.random()) % 3]
            op = os.popen('lp -d ' + printer + ' -t ' + code.team.account.username +
                      ' -o prettyprint -o Page-left=36 -o Page-right=36 -o Page-top=36 -o Page-bottom=36', 'wb')
            op.write(code.text.encode('utf-8'))
            if op:
                code.is_print = True
                code.save()
                op.close()
        except Exception:
            pass


    def print_file(self, file_name):
        os.system('lp -d ' + self.major_printer + ' ' + file_name)


# p = Printer()
# p.print_code('/home/mikedc/acm2015/static/tasks/team1_2015-04-11 15:02:51.352338')
# p.print_file('/home/mikedc/acm2015/static/files/team.csv')

# lp -o zh_CN.gb18030 -o nodimm -osimsun
# lp -o zh_CN.utf8 -o nodimm -osimsun