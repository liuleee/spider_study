# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute('scrapy crawl douban_spider -o db_movie.csv'.split())