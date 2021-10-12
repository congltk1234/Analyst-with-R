# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LazadaItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    category = scrapy.Field()
    label = scrapy.Field()
