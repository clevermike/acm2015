#!/usr/bin/env python
# coding=utf-8
# dongchen@meituan.com


from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import re


# 拉手deal详情页的抓取框架
class lashouScrapy(CrawlSpider):
    name = 'lashou'
    allowed_domains = ['lashou.com']
    start_urls = [
        'http://www.lashou.com/changecity',
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'lashou.com/deal/([\d]+).html')), callback='myparse'),
        Rule(SgmlLinkExtractor(allow=(r'([\w]+).lashou.com$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'lashou.com/cate/([\w]+)$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'lashou.com/cate/([\w]+)/page([\d]+)$')), follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'dianping.com/shop/([\d]+)')), follow=True),
    ]

    def myparse(self, response):
        dealid = re.findall('lashou.com/deal/([\d]+).html', response.url)
        if len(dealid) == 0:
            return
        else:
            dealid = dealid[0]
        filename = '../data/lashou/' + str(dealid) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)