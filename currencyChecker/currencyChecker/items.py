# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CurrencyItem(scrapy.Item):
    name = scrapy.Field()
    currency_to_bss = scrapy.Field()