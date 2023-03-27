import scrapy


class SalespiderSpider(scrapy.Spider):
    name = "salespider"
    allowed_domains = ["store.steampowered.com"]
    gameDomains = ["311690/Enter_the_Gungeon/",
                   "400/Portal/",
                   "108600/Project_Zomboid/",
                   "1369630/ENDER_LILIES_Quietus_of_the_Knights/",
                   "588650/Dead_Cells/",
                   "367520/Hollow_Knight/",
                   "391540/Undertale/"
                   ]
    
    url = "https://store.steampowered.com/app/"

    start_urls = []
    for x in gameDomains:
        start_urls.append(url + x)

    def parse(self, response):
        yield{
            'name': response.css('div.apphub_AppName::text').get(),
            'price': response.css('div.game_purchase_price.price::text').get().replace("\r\n\t\t\t\t\t\t\t", '').replace("\t\t\t\t\t\t", '')
        }
