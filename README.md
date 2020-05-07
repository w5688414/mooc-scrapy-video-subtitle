# mooc-scrapy-video-subtitle

+ 主要是修改别人的代码，我只需要带有字幕的视频，代码主要来自于https://github.com/victorlidong/moocScrapy.git
+ 原作者的代码不支持多个url，我这里拓展成支持多个url同时爬取
+ mooc爬虫，爬视频，字幕

## 依赖

+ requests                2.23.0
+ Scrapy                  2.1.0
+ m3u8                    0.6.0
+ natsort                 7.0.1
+ fake-useragent          0.1.11

## 使用方法 
获取课程链接中的课程号，例如

https://www.icourse163.org/course/SCU-1003253003 

中的SCU-1003253003 在setting.py中更改

```
COURSE_ID="SCU-1003253003"
```

然后运行run.py,运行之前确保依赖安装好了
