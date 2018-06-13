#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 把新闻整理成一行文本.py
# @Author: 刘绪光
# @Date  : 2018/4/7
# @Desc  :

import os


def to_oneline(path, file_name):
    fp = open(path + file_name, 'r', encoding='utf-8')

    result = ''
    for line in fp:
        result += line.strip().replace('\n', '').replace('\t', '') + ' '
    fp.close()
    return result


def write_file(content):
    fp = open('D:/workspace/data/onefile.txt', 'a', encoding='utf-8')
    fp.write('经济责任审计   ' + content + '\n')
    fp.close()


if __name__ == '__main__':
    for filename in os.listdir('D:/workspace/data/zjw'):
        content = to_oneline('D:/workspace/data/zjw/', filename)
        write_file(content)
