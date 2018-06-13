#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 爬取新浪网新闻.py
# @Author: 刘绪光
# @Date  : 2018/4/7
# @Desc  :

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# 网页解析器
from bs4 import BeautifulSoup
import requests
import time
# 产生随机数
import random
import os


# driver相当于一个浏览器，以后要在网页上面做的操作，都是通过driver进行的
driver = webdriver.Chrome(executable_path="D:/workspace/tools/chromedriver/chromedriver.exe")

# 新浪网首页
start_url = 'http://www.sina.com.cn/'


# 进入新浪主页，然后进行搜索，搜索成功后
def start(url):
    driver.get(url)

    # 显示等待
    WebDriverWait(driver, 200).until_not(
        ec.url_to_be(start_url)
    )

    # 获取窗口句柄
    handles = driver.window_handles

    # 关闭当前页
    driver.close()

    # 跳转到指定句柄窗口
    driver.switch_to_window(handles[1])

    get_news()


def get_news():
    page = 1
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        a_list = soup.select('#result a')
        a_list = a_list[0:10]
        # print(a_list)
        # print(len(a_list))
        it_url_list(a_list)

        print('第', page, '页....................')

        time.sleep(5)

        next_page = driver.find_elements_by_css_selector('#result a[title="下一页"]')

        if len(next_page) is 0:
            driver.refresh()
        else:
            next_page[0].click()
            page += 1


def it_url_list(a_list):
    for a in a_list:
        print(a.text)
        if a['href'] != '#':
            title, content, source = get_html(a['href'])
            write_file('D:/workspace/cursinanews/', title, content, source)
        time.sleep(random.uniform(0, 2))


def get_html(url):
    html = requests.get(url)
    if html.status_code == 200:
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'html.parser')

        title = soup.select('.main-title')
        if len(title) is 0:
            title = soup.select('#artibodyTitle')

        source = soup.select('.date-source')
        if len(source) is 0:
            source = soup.select('#navtimeSource')
        if len(source) is 0:
            source = soup.select('.time-source')

        content = soup.select('#article')
        if len(content) is 0:
            content = soup.select('#artibody')
        return title, content, source
    else:
        print(url, '404')
        return None, None


def write_file(path, title, content, source):
    if title is None or len(title) == 0:
        print('未获取到页面...................')
    else:
        rel_title = title[0].text
        rel_title = str(rel_title).replace('\t', '').replace('\n', '')
        if not os.path.exists(path + rel_title + '.txt'):
            try:
                # print(title)
                # print(source)
                # print(content)
                print('=================================================================')
                print(len(title), len(source), len(content))
                fp = open(path + rel_title + '.txt', 'a', encoding='utf-8')
                fp.write(rel_title + '\n')
                fp.write(source[0].text)
                fp.write(content[0].text + '\n')

                fp.close()
            except Exception as e:
                print(e, '文件名不合法...........')
        else:
            print('已经存在......')


if __name__ == '__main__':
    start(start_url)

    # 关闭浏览器
    driver.quit()
