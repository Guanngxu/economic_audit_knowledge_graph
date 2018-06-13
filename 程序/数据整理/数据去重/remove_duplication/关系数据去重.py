#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 关系数据去重.py
# @Author: 刘绪光
# @Date  : 2018/4/14
# @Desc  :


def re_dup():

    dup = set()
    fp = open('实体关系.txt', 'r', encoding='utf-8')

    for line in fp:
        dup.add(line)

    fp.close()

    write = open('实体关系去重.txt', 'a', encoding='utf-8')
    for data in dup:
        write.write(data)

    write.close()


if __name__ == '__main__':
    re_dup()