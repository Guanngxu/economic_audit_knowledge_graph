#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hudong_spider.py
# @Author: 刘绪光
# @Date  : 2018/6/14
# @Desc  :

from scrapy.spider import Spider
from bs4 import BeautifulSoup
from scrapy.spider import Request
from hudong.items import HudongItem


class HudongSpider(Spider):

    # 爬虫启动命令
    name = 'hudong'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://www.baike.com/wiki/经济责任审计'
        yield Request(url, headers=self.headers)

    def parse(self, response):

        item = HudongItem()

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.select('.content-h1 h1')[0].text
        item['title'] = title

        open_type_list = soup.select('#openCatp a')
        open_type = ''
        for a in open_type_list:
            open_type += '##' + a.text
        item['open_type'] = open_type

        info_list = soup.select('#anchor p')
        info = ''
        for p in info_list:
            info += p.text
        item['info'] = info

        properties_list = soup.select('.module table tbody tr td strong')
        properties = ''
        for pro in properties_list:
            properties += '##' + pro.text
        item['properties'] = properties

        values_list = soup.select('.module table tbody tr td span')
        values = ''
        for val in values_list:
            values += '##' + val.text
        item['values'] = values

        yield item


