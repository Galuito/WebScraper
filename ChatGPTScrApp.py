'''
This was an scrapy example use provided by ChatGPT, I'll use it the moment I understand it because, even though
the code is there and it probably works I don't know how to get it running, therefore, I'll first learn with a 
different example given to my by other source, if I get this code running then I'll consider myself triumphant

Still, I'd like to do more than 1 web scraper and maybe I can do a class which handles scraping for me and can be
imported as a module.

After googling most of my questions in the internet now I can understand how it all works, basically what I'm doing
is specifying which parts of the HTML code I need to get from the page, specifying by the CSS attributes of the class
'''

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
