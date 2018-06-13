#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 去除互动数据前面的逗号.py
# @Author: 刘绪光
# @Date  : 2018/4/14
# @Desc  :


def dup():
    fp = open('互动百科获取的词条信息带逗号.json', 'r', encoding='utf-8')
    write = open('去掉逗号.json', 'a', encoding='utf-8')

    for line in fp:
        write.write(line[1:])

    fp.write()
    write.close()


if __name__ == '__main__':
    dup()
