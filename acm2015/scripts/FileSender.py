#!/usr/bin/env python
# coding=utf-8
#author:dongchen
import sys
sys.path.append("..")
import logging
import settings
import shutil
import time
import datetime

XML_PATH = settings.RESULT_PATH
XML_PATH_COPY = settings.RESULT_PATH_COPY

END_TIME = datetime.datetime.strptime(settings.BOARD_OFF_TIME, '%Y-%m-%d %H:%M:%S')
while datetime.datetime.now() < END_TIME:
    try:
        shutil.copyfile(XML_PATH, XML_PATH_COPY)
    except Exception:
        logging.error('fuck', Exception)
    time.sleep(3)
