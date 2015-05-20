#!/usr/bin/env python
# coding=utf-8
# dongchen@meituan.com


from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import re


# 美团deal详情页的抓取框架
class meituanScrapy(CrawlSpider):
    name = 'meituan'
    allowed_domains = ['meituan.com']
    start_urls = [
        'http://www.meituan.com/index/changecity',
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'meituan.com/deal/([\d]+).html\??')), callback='myparse'),
        Rule(SgmlLinkExtractor(allow=(r'([\w]+).meituan.com$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'meituan.com/category/([\w_]+)$')), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'meituan.com/shop/([\d]+)')), follow=True),
    ]

    def myparse(self, response):
        dealid = re.findall('/deal/([\d]+).html\??', response.url)
        if len(dealid) == 0:
            return
        else:
            dealid = dealid[0]
        filename = '../data/meituan/' + str(dealid) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
