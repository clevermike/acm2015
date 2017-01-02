#!/usr/bin/env python
# coding=utf-8
#author:dongchen

import random
import os
import sys
from config import PRINTER


class Printer:

    def __init__(self):
        self.major_printer = PRINTER['major']
        self.minor_printers = PRINTER['group']

    def print_code(self, code):
        # 此段代码使用os.popen,不能得到失败的提示信息，也无法获得成功失败的状态;看网上建议使用subprocess模块,欢迎大牛一起研究
        try:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            printer = self.minor_printers[int(random.randint) % len(self.minor_printers)]
            op = os.popen('lp -d ' + printer + ' -t ' + code.team.account.username + '-' + code.team.seatId +
                      ' -o prettyprint -o Page-left=36 -o Page-right=36 -o Page-top=36 -o Page-bottom=36', 'wb')
            op.write(code.text.encode('utf-8'))
            if op:
                code.isPrint = True
                code.save()
                op.close()
        except Exception:
            pass

