# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class HindawiPipeline(object):
    def process_item(self, item, spider):
        if item['title'] and item['url'] and len(item['author_id']):
            return item
        else:
            raise DropItem("Invalid item")
