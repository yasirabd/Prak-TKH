# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BukalapakItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_category = scrapy.Field()
    product_currency_price = scrapy.Field()
    product_price = scrapy.Field()
