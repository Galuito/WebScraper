import scrapy
from willywonka.items import WillywonkaItem
from willywonka.itemloaders import WillywonkaItemLoader

class WillyspiderSpider(scrapy.Spider):
    name = "willyspider"
    allowed_domains = ["chocolate.co.uk"] #This is for avoiding an accident with scraping
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    #css selector = 'product-item'
    #css selector use = response.css('product-item')
    def parse(self, response):
        products = response.css('product-item')

        # product_item = WillywonkaItem()
        for product in products:
            # yield {
            #     'name': product.css('a.product-item-meta__title::text').get(),
            #     'price': product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>', '').replace('</span>', ''),
            #     'url': product.css('a.product-item-meta__title').attrib['href']
            # }

            # product_item['name'] = product.css('a.product-item-meta__title::text').get()
            # product_item['price'] = product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>', '').replace('</span>', '')
            # product_item['url'] = product.css('a.product-item-meta__title').attrib['href']
            # yield product_item

            chocolate = WillywonkaItemLoader(item = WillywonkaItem(), selector = product)
            chocolate.add_css('name', "a.product-item-meta__title::text")
            chocolate.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()
        
        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)
            chocolate.add_css('name', "a.product-item-meta__title::text")
            chocolate.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()
