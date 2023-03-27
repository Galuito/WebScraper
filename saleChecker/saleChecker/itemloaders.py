from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class SteamGameLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: x[1:].split("USD")[0])
    # url_in = TakeFirst()