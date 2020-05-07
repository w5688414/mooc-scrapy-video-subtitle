# -*- coding: utf-8 -*-
"""
MoocScrapy项目的Scrapy设置
"""

import datetime
import os
import pandas as pd

# DOWNLOAD_URL = input("请输入保存路径：")
# course_url = input("输入你想爬取的课程链接：")
print("输入下载的视频质量（1-3）：")
DOWNLOAD_URL='download'
# course_url='https://www.icourse163.org/course/SCU-1003253003'
# course_url='https://www.icourse163.org/course/BIT-268001'
course_url='https://www.icourse163.org/course/WHU-1001716008'
# VIDEO_TYPE = input()
VIDEO_TYPE=1
print("VIDEO_TYPE = ", VIDEO_TYPE)

data=pd.read_csv('data.csv')
list_data=data['url'].tolist()


class DownloadUrls():
     
    def __init__(self):
        self.urls={}

    def getDownloadUrl(self,i):
        if(i not in self.urls):
            return DOWNLOAD_URL
        return self.urls[i]

    def setDownloadUrl(self,i,downloadurl):
        # global DOWNLOAD_URL
        self.urls[i] = downloadurl


downloadUrls=DownloadUrls()

def get_course_id(course_url):
    COURSE_ID = ''
    for i in range(len(course_url)):
        if course_url[len(course_url) - i - 1] == '/':
            COURSE_ID = course_url[-i:]
            break
    print("COURSE_ID =", COURSE_ID)
    return COURSE_ID

COURSE_IDs=[]
for item in list_data:
    COURSE_ID=get_course_id(item)
    COURSE_IDs.append(COURSE_ID)


DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 10
COOKIES_ENABLED = False

BOT_NAME = 'moocScrapy'
SPIDER_MODULES = ['moocScrapy.spiders']
NEWSPIDER_MODULE = 'moocScrapy.spiders'

ROBOTSTXT_OBEY = False
# URL不去重
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

Today = datetime.datetime.now()
# 则在目标下增加log文件夹项目下  和scrapy.cfg同级
Log_file_path = 'log/scrapy_{}_{}_{}.log'.format(Today.year, Today.month, Today.day)
if not os.path.exists('log'):
    os.mkdir('log')

# 级别，则高于或者等于该等级的信息就能输出到我的日志中，低于该级别的信息则输出不到我的日志信息中
# Log_file_path='scrapy_{}_{}_{}.log'.format(Today.year,Today.month,Today.day)#时间为名字
LOG_LEVEL = "WARNING"
LOG_FILE = Log_file_path

DOWNLOADER_MIDDLEWARES = {
    'moocScrapy.middlewares.RandomUserAgent': 543,
}

ITEM_PIPELINES = {
    'moocScrapy.pipelines.MoocscrapyPipeline': 400,
}
