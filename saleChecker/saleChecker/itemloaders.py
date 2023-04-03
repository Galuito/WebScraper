from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import re

class SteamGameLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: re.findall("([0-9]*\.[0-9][0-9]?)", x))
    currency_in = MapCompose(lambda x: re.findall("(USD|EUR|ARS)", x))