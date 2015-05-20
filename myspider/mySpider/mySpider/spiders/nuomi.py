#!/usr/bin/env python
# coding=utf-8
# dongchen@meituan.com


from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import re


# 糯米deal详情页的抓取框架
class nuomiScrapy(CrawlSpider):
    name = 'nuomi'
    allowed_domains = ['nuomi.com']
    start_urls = [
        'http://www.nuomi.com/pcindex/main/changecity',
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'nuomi.com/deal/([\w\d]+).html')), callback='myparse'),
        Rule(SgmlLinkExtractor(allow=(r'([\w]+).nuomi.com$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'nuomi.com/([\d]+)$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'nuomi.com/([\w]+)$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'nuomi.com/([\d]+)-page\d+')), follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'dianping.com/shop/([\d]+)')), follow=True),
    ]

    def myparse(self, response):
        dealid = re.findall('nuomi.com/deal/([\w\d]+).html', response.url)
        if len(dealid) == 0:
            return
        else:
            dealid = dealid[0]
        filename = '../data/nuomi/' + str(dealid) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
