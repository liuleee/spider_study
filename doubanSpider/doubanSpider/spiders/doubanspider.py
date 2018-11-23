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
#默认的解析方法
    def parse(self, response):
        #循环与电影的条目
        moive_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in moive_list:
            #导入item文件
            doubanSpider_item = DoubanspiderItem()
            #详细的数据解析
            doubanSpider_item['serial_num'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            doubanSpider_item['movie_name'] = i_item.xpath(".//div[@class='info']//div[@class='hd']//a/span[1]/text()").extract_first()
            #多行时，进行数据处理
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']//p[1]/text()").extract()
            for i_content in content:
                content_item = "".join(i_content.split())
                doubanSpider_item['introduce'] = content_item
            doubanSpider_item['star'] = i_item.xpath(".//div[@class='bd']//div[@class='star']/span[2]/text()").extract_first()
            doubanSpider_item['evaluate'] = i_item.xpath(".//div[@class='bd']//div[@class='star']/span[4]/text()").extract_first()
            doubanSpider_item['describe'] = i_item.xpath(".//div[@class='bd']//p[@class='quote']/span[@class='inq']/text()").extract_first()
            #将数据给yeild进pipeline
            yield doubanSpider_item
            #解析下一页，取下一页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)




