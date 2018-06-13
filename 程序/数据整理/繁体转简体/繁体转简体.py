#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 繁体转简体.py
# @Author: 刘绪光
# @Date  : 2018/4/23
# @Desc  :
from 整理最终的关系数据.langconv import *


# 繁体转换为简体
def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line)
    return line


def start():
    reations = open('relations.json', 'r', encoding='utf-8')

    zh = dict()

    for line in reations:
        dic = eval(line)
        zh[dic['rmention'].strip()] = tradition2simple(dic['chrmention'].strip())
    reations.close()

    # 记录没有中文表述的关系
    count = set()

    fp = open('relation.csv', 'r', encoding='utf-8')
    write = open('result.csv', 'a', encoding='utf-8')
    fail = open('fail.csv', 'a', encoding='utf-8')

    for line in fp:
        words = line.strip().split(',')
        if words[1] in zh.keys():
            write.write(str(words[0] + ',' + zh[words[1]] + ',' + words[2] + '\n'))
        else:
            fail.write(line.strip() + '\n')
            count.add(words[1])

    fp.close()
    write.close()
    fail.close()

    print(count)


def read():
    fp = open('realtionlast.csv', 'r', encoding='utf-8')
    write = open('writerelation.csv', 'a', encoding='utf-8')
    for line in fp:
        write.write(tradition2simple(line))

    write.flush()
    fp.close()
    write.close()


if __name__ == '__main__':
    read()
