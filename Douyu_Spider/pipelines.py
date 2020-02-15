# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import re
import os
from image_spider.settings import IMAGES_STORE as store
from scrapy.pipelines.images import ImagesPipeline
from pathlib import Path,PureWindowsPath
store = Path("C:/Users/hp/Desktop/image_spider/image_spider/IMAGES/")

class ImageSpiderPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    def item_completed(self,results,item,info):
        image_path = [x["path"] for ok, x in results if ok]
        image_path[0]=Path(image_path[0])
        store_before = store / image_path[0]
        item["nickname"]="【"+item["nickname"]+"】" + " _ "+"【"+item['roomid']+"】"+" _ "+"【"+item['roomname']+"】"+".jpg"
        item["nickname"]=Path(item["nickname"])

        store_after = store / item["nickname"]
        #while store_before.find("\\")!=-1:
        #    sb = list(store_before)
        #    sb.pop(store_before.find("\\"))
        #    store_before = "".join(sb)
        #while store_after.find("\\")!=-1:
        #    sa = list(store_after)
        #    sa.pop(store_after.find("\\"))
        #    store_after = "".join(sa)
        
        #store_before.replace('\\',r'
        
        os.rename(store_before , store_after)
        return item
    
