#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : baidu_spider.py
# @Author: 刘绪光
# @Date  : 2018/6/14
# @Desc  :

from scrapy.spider import Spider
from scrapy.spider import Request
from bs4 import BeautifulSoup
from baidu.items import BaiduItem


class BaiduSpider(Spider):
    # 爬虫启动命令
    name = 'baidu'
    base_url = 'https://baike.baidu.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://baike.baidu.com/item/李娜'
        yield Request(url, headers=self.headers)

    # 初始爬取列表
    start_urls = ['https://baike.baidu.com/item/经济责任审计']

    def parse(self, response):
        item = BaiduItem()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.select('.lemmaWgt-lemmaTitle-title h1')[0].text
        subhead = soup.select('.lemmaWgt-lemmaTitle-title h2')
        if len(subhead) is not 0:
            # print(subhead[0].text)
            title = title + subhead[0].text
        item['title'] = title

        info_list = soup.select('.lemma-summary div')
        info = ''
        for temp in info_list:
            # 截取其中文字信息
            info += temp.text
            # 如果有超链接，则继续爬取
            a_list = temp.select('a')
            if len(a_list) is not 0:
                for a in a_list:
                    if a.has_attr('href'):
                        yield Request(self.base_url + a['href'], headers=self.headers)
        item['info'] = info

        properties_list = soup.select('.basicInfo-block dt')
        properties = ''
        for pro in properties_list:
            properties += '###' + pro.text.strip().replace('\n', '')
            # 如果有超链接，则继续爬取
            a_list = pro.select('a')
            if len(a_list) is not 0:
                for a in a_list:
                    if a.has_attr('href'):
                        yield Request(self.base_url + a['href'], headers=self.headers)
        item['properties'] = properties

        values_list = soup.select('.basicInfo-block dd')
        values = ''
        for val in values_list:
            values += '###' + val.text.strip().replace('\n', '')
            # 如果有超链接，则继续爬取
            a_list = val.select('a')
            if len(a_list) is not 0:
                for a in a_list:
                    if a.has_attr('href'):
                        yield Request(self.base_url + a['href'], headers=self.headers)
        item['values'] = values

        if len(soup.select('.summary-pic img')) is not 0:
            item['img'] = soup.select('.summary-pic img')[0]['src']

        print(item['title'])

        yield item
