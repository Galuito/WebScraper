from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class CurrencyLoader(ItemLoader):
    default_output_processor = TakeFirst()
    # currency_to_bss_in = MapCompose(lambda x: float(x))
