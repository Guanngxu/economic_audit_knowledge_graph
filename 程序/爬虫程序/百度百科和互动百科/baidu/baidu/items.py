# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field


class BaiduItem(Item):

    # 词条
    title = Field()

    # 详细信息
    info = Field()

    # 词条图片
    img = Field()

    # 属性列表
    properties = Field()

    # 属性对应的值列表
    values = Field()
