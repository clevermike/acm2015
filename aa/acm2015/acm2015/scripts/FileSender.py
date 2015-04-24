#!/usr/bin/env python
# coding:utf-8
#author:dongchen
import sys
sys.path.append("..")
import logging
import settings
import shutil
import time
import datetime

XML_PATH = settings.XML_PATH
XML_PATH_COPY = settings.XML_PATH_COPY
print datetime.datetime.now()
while datetime.datetime.now() < settings.BOARD_OFF_TIME:
    try:
        shutil.copyfile(XML_PATH, XML_PATH_COPY)
    except Exception:
        logging.error('fuck', Exception)
    time.sleep(3)
