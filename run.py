# _*_ encoding:utf-8 _*_
"""
运行主函数
"""

from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'mooc'])
