# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

#I did the pipeline job in the itemloaders
class PriceCleanerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
            # adapter['price'] = adapter['price'].replace('\n\t\t\t\t\t\t\t$', '')
            # adapter['price'] = float(adapter['price'])

            return item
        else:
            raise DropItem(f"Missing price in {item}")
