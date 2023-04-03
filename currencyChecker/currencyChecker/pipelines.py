# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CurrencyConverterPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if(adapter.get('currency_to_bss')):
            adapter['currency_to_bss'] = adapter['currency_to_bss'].replace(',', '.')
            adapter['currency_to_bss'] = float(adapter['currency_to_bss'])
            return item
