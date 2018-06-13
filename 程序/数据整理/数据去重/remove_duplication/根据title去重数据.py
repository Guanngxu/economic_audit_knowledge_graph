#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 根据title去重数据.py
# @Author: 刘绪光
# @Date  : 2018/4/16
# @Desc  :


def re_dup():

    dup = set()
    fp = open('互动百科数据去重.json', 'r', encoding='utf-8')

    dic = {}

    for line in fp:
        json = eval(line)

        keys = dic.keys()

        if json['title'].strip() not in keys:
            dic[json['title']] = line
        else:
            if len(dic[json['title'].strip()]) < len(line):
                dic[json['title'].strip()] = line

    print(len(dic))

    keys = dic.keys()

    for data in keys:
        dup.add(dic[data])

    fp.close()

    write = open('互动百科数据再去重.json', 'a', encoding='utf-8')
    for data in dup:
        write.write(data)

    write.close()


if __name__ == '__main__':
    re_dup()
