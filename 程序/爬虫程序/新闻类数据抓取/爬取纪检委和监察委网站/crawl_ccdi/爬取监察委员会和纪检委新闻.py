#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 爬取监察委员会和纪检委新闻.py
# @Author: 刘绪光
# @Date  : 2018/4/2
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

# 监察委员会网站主页
start_url = 'http://www.ccdi.gov.cn/'


# 进入审计署主页，然后进行搜索，搜索成功后
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
        a_list = soup.select('.s_0603_list li em b a')
        it_url_list(a_list)
        # print(a_list)
        print('第', page, '页....................')

        next_page = driver.find_elements_by_css_selector('.next-page')
        next_page[0].click()
        page += 1


def it_url_list(a_list):
    for a in a_list:
        print(a.text)
        if a['href'] != '#':
            title, content = get_html(a['href'])
            write_file('D:/workspace/ccdinews/', title, content)
        time.sleep(random.uniform(0, 3))


def get_html(url):
    html = requests.get(url)
    if html.status_code == 200:
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, 'html.parser')

        title = soup.select('.tit')
        content = soup.select('.TRS_Editor p')
        return title, content
    else:
        print(url, '404')
        return None, None


def write_file(path, title, content):
    if title is None or len(title) == 0:
        print('未获取到页面...................')
    else:
        rel_title = title[0].text
        rel_title = str(rel_title).replace('\t', '').replace('\n', '').strip()
        if not os.path.exists(path + rel_title + '.txt'):
            try:
                fp = open(path + rel_title + '.txt', 'a', encoding='utf-8')
                fp.write(rel_title + '\n')

                for p in content:
                    fp.write(p.text + '\n')

                fp.close()
            except Exception as e:
                print(e, '文件名不合法...........')
        else:
            print('已经存在......')


if __name__ == '__main__':
    start(start_url)

    # 关闭浏览器
    driver.quit()
