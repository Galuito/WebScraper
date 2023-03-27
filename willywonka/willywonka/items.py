# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
"""In here I defined the items which I will be using to run my spider, it is very easy, you just have to 
give every field a name and then define it as a Scrapy Field"""
class WillywonkaItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
