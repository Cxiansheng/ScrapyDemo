# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class DoubanPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.create_sheet('电影TOP250')
        self.sheet.append(['电影标题', '电影信息', '电影评分', '电影金句'])

    def process_item(self, item, spider):
        print(type(item['score']))
        line = [item['title'], item['movie_info'].strip(), item['score'], item['quote']]
        self.sheet.append(line)
        self.wb.save("movie.xlsx")
        return item
