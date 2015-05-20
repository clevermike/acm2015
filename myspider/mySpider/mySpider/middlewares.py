#!/usr/bin/env python
# coding=utf-8
# dongchen@meituan.com

from mySpider.settings import USER_AGENT_LIST, USER_PASS_LIST, PROXY_LIST
import random
import base64


class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)


class ProxyMiddleware(object):

    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = random.choice(PROXY_LIST)

        # Use the following lines if your proxy requires authentication
        proxy_user_pass = random.choice(USER_PASS_LIST)
        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
