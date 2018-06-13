#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : wikidata数据去重.py
# @Author: 刘绪光
# @Date  : 2018/4/14
# @Desc  :


def re_dup():

    dup = set()
    fp = open('wikidata获取的实体.json', 'r', encoding='utf-8')

    for line in fp:
        dup.add(line)

    fp.close()

    write = open('wikidata获取的实体去重.json', 'a', encoding='utf-8')
    for data in dup:
        write.write(data)

    write.close()


if __name__ == '__main__':
    re_dup()
