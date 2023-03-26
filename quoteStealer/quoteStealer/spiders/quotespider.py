import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            yield{
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'url': quote.css('a').attrib['href'],
                'tags': quote.css('a.tag::text').extract()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://quotes.toscrape.com' + next_page
            yield response.follow(next_page_url, self.parse)
