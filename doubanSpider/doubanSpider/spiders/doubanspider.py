# -*- coding: utf-8 -*-
import scrapy
from doubanSpider.doubanSpider.items import DoubanspiderItem
# 创建Douban类
class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名称
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url,扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        moive_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in moive_list:
            doubanSpider_item = DoubanspiderItem()
            doubanSpider_item['serial_num'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            print(doubanSpider_item)
            # doubanSpider_item['movie_name'] = i_item.xpath("").extract_first()
            # doubanSpider_item['introduce'] = i_item.xpath("").extract_first()
            # doubanSpider_item['star'] = i_item.xpath("").extract_first()
            # doubanSpider_item['evaluate'] = i_item.xpath("").extract_first()
            # doubanSpider_item['describe'] = i_item.xpath("").extract_first()



