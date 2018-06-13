#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 获取实体之间的关系.py
# @Author: 刘绪光
# @Date  : 2018/4/6
# @Desc  :

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.wikidata.org/wiki/'


# 获取关系列表
def get_html(entity, entity_id, entity_en):
    res = requests.get('https://www.wikidata.org/wiki/' + entity_id)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    list_view = soup.select('.wikibase-listview')
    print(entity, '       ', entity_en)
    if len(list_view) is not 0:
        rel_list = list_view[0].select('.wikibase-statementgroupview')
        for rel in rel_list:
            # 关系和属性混在一起，第一个一定是关系，后面不一定
            a_list = rel.select('a')
            # print(a_list)
            process_a_list(entity, entity_id, entity_en, a_list)


# 选择关系
def process_a_list(entity, entity_id, entity_en, a_list):
    if len(a_list) is not 0:
        # 关系名称
        rel_name = a_list[0].text
        # 关系id
        rel_url = a_list[0]['href']

        if rel_name != 'Commons category' and rel_name != "topic's main category":
            head_str = '"' + entity + '","' + entity_id + '","' + entity_en + '","' + rel_name + '","' + rel_url + '",'
            process_relation(head_str, a_list)


# 处理关系
def process_relation(head_str, a_list):
    end = len(a_list)
    i = 1
    while i < end:
        try:
            # 如果长度为1，说明是实体
            write_str = ''
            if len(a_list[i]['title'].split(':')) == 1:
                write_str += head_str + '"' + a_list[i].text + '","' + a_list[i]['title'] + '"'
            else:
                write_str += '"' + a_list[i - 1].text + '","' + a_list[i - 1]['title'] + '","' \
                             + a_list[i].text + '","' + a_list[i]['href'] + '",' \
                             + '"' + a_list[i + 1].text + '","' + a_list[i + 1]['title'] + '"'
                i += 1
            write_file('实体关系', write_str)
            i += 1
        except Exception as e:
            i += 1
            # print(e, ',无title......')


# 写入文件
def write_file(file_name, content):
    fp = open(file_name + '.txt', 'a', encoding='utf-8')
    try:
        fp.write(content + '\n')
    finally:
        fp.close()


# 从文件中读取数据，对每一行进行处理
def read_file(file_name):
    fp = open(file_name + '.json', 'r', encoding='utf-8')
    try:
        for line in fp:
            dic = eval(line)
            get_html(dic['name'], dic['id'], dic['en_name'])
    finally:
        fp.close()


if __name__ == '__main__':
    # res = requests.get('https://www.wikidata.org/wiki/Q124291')
    # res.encoding = 'utf-8'
    # soup = BeautifulSoup(res.text, 'html.parser')
    # list_view = soup.select('.wikibase-listview')
    #
    # if len(list_view) is not 0:
    #     rel_list = list_view[0].select('.wikibase-statementgroupview')
    #     print(len(rel_list))
    #     # for rel in relation:
    #     print(rel_list[0].select('a'))
    #
    # print(len('Q26717101'.split(':')))
    read_file('实体简要信息')
