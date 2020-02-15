# -*- coding: utf-8 -*-
import scrapy
from image_spider.items import ImageSpiderItem
import json

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        if len(data_list)==0:
            return
        
        for data in data_list:
            item = ImageSpiderItem()
            item['nickname'] = data['nickname']
            item['imagelink'] = data['vertical_src']
            item['roomid'] = data['room_id']
            item['roomname'] = data['room_name']
            yield item
            
            
        self.offset += 20
        yield scrapy.Request(self.base_url + str(self.offset),callback = self.parse)
