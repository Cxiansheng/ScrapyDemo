# -*- coding:utf-8 -*-
"""

Created on 2019/6/22
@author:Ray Li

"""

import scrapy
from Douban import items


class MyDouban(scrapy.Spider):
    name = "Douban"
    start_urls = ["https://movie.douban.com/top250"]

    url = "https://movie.douban.com/top250"

    def parse(self, response):
        item = items.DoubanItem()
        movies = response.xpath('//div[@class="info"]')

        for movie in movies:
            title = movie.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
            # print(title)
            full_title = ''
            for each in title:
                full_title += each

            movie_info = movie.xpath('div[@class="bd"]/p/text()').extract()[0]

            score = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]

            quote = movie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()[0]

            # print("######################################")
            # print(movie_info)
            # print(score)
            # print(quote)
            # print(title)
            # print("######################################")

            item['title'] = full_title
            item['movie_info'] = movie_info
            item['quote'] = quote
            item['score'] = score

            yield item

        nextPage = response.xpath('//span[@class="next"]/a/@href').extract()

        if nextPage:
            nextPage = nextPage[0]
            yield scrapy.Request(self.url + nextPage, callback=self.parse)