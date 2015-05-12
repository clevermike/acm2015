#!/usr/bin/env python
# coding=utf-8
#author:dongchen

import random
import os
import sys
from settings import PRINTER


class Printer:

    def __init__(self):
        self.major_printer = PRINTER['major']
        self.minor_printers = PRINTER['group']


    def print_code(self, code):
        try:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            printer = self.minor_printers[int(random.random()*1000) % 3]
            op = os.popen('lp -d ' + printer + ' -t ' + code.team.account.username + '-' + code.team.seatId +
                      ' -o prettyprint -o Page-left=36 -o Page-right=36 -o Page-top=36 -o Page-bottom=36', 'wb')
            op.write(code.text.encode('utf-8'))
            if op:
                code.isPrint = True
                code.save()
                op.close()
        except Exception:
            pass

