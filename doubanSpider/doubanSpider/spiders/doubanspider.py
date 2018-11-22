# -*- coding: utf-8 -*-
import scrapy


# 创建Douban类
class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名称
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url,扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.text)

