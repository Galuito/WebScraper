import scrapy
from currencyChecker.items import CurrencyItem
from currencyChecker.itemloaders import CurrencyLoader
class MoneyspiderSpider(scrapy.Spider):
    name = "moneyspider"
    allowed_domains = ["bcv.org.ve"]
    start_urls = ["https://bcv.org.ve/"]

    #All this spider is going to do is that it is going to return me the value of 1 USD and 1 EUR to BSF? BSS? BSSSJ?

    def parse(self, response):
        dollar = CurrencyLoader(item = CurrencyItem(), selector = response)
        dollar.add_value('name', "Dollar")
        dollar.add_css('currency_to_bss','#dolar strong::text')
        euro = CurrencyLoader(item = CurrencyItem(), selector = response)
        euro.add_value('name', "Euro")
        euro.add_css('currency_to_bss', '#euro strong::text')
        yield dollar.load_item()
        yield euro.load_item()