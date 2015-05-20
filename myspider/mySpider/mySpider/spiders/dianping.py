#!/usr/bin/env python
# coding=utf-8
# dongchen@meituan.com


from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import re


# 点评deal详情页的抓取框架
class dianpingScrapy(CrawlSpider):
    name = 'dianping'
    allowed_domains = ['dianping.com']
    start_urls = [
        'http://t.dianping.com/citylist',
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'dianping.com/deal/([\d]+)')), callback='myparse'),
        Rule(SgmlLinkExtractor(allow=(r'dianping.com/([\w]+)$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'dianping.com/list/([\w]+)-category_([\d]+)$')), follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'dianping.com/shop/([\d]+)')), follow=True),
    ]

    def myparse(self, response):
        dealid = re.findall('dianping.com/deal/([\d]+)', response.url)
        if len(dealid) == 0:
            return
        else:
            dealid = dealid[0]
        filename = '../data/dianping/' + str(dealid) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
