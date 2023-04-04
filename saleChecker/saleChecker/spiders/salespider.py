import scrapy
#Importing the SteamGame class from items.py, this is a simple class containing the Fields of my elements
from saleChecker.items import SteamGame
#In here we import the Item Loader, which works as a small way to pre process the item inside the Spider
from saleChecker.itemloaders import SteamGameLoader



#This is still not working properly, I have to fix it someway and somehow, also, I need to find a way to scrape even
#harder to get links out of steam and then scrape those links, ALSO, I need to handle when there is a sale and when
#there isn't so that I can get the correct value for the correct field

class SalespiderSpider(scrapy.Spider):
    name = "salespider"
    allowed_domains = ["store.steampowered.com"]
    #This are all the domains that I am interested in scraping

    gameDomains = ["311690/Enter_the_Gungeon/",
                   "400/Portal/",
                   "108600/Project_Zomboid/",
                   "1369630/ENDER_LILIES_Quietus_of_the_Knights/",
                   "588650/Dead_Cells/",
                   "367520/Hollow_Knight/",
                   "391540/Undertale/",
                   "504230/Celeste/",
                   "1736550/Deflector/",
                   "2050650/Resident_Evil_4/",
                   "105600/Terraria/",
                   "211820/Starbound/",
                   "413150/Stardew_Valley/",
                   "599140/Graveyard_Keeper/",
                   "247080/Crypt_of_the_NecroDancer/"
                   ]

    #Base URL which I'll be appending the specific games to
    url = "https://store.steampowered.com/app/"
    start_urls = []
    for x in gameDomains:
        #Filling the start urls list with said URLs that are going to be scraped
        start_urls.append(url + x)

    def start_requests(self):
        cookies = {'birthtime': '1008392401', 'lastagecheckage':'15-2-2002'}
        for eachURL in self.start_urls:
            yield scrapy.Request(url = eachURL, cookies = cookies, callback = self.parse)
        
        # return super().start_requests()

    def parse(self, response):
        #We define the Item Loader, with its own item (SteamGame) and from where it'll be getting its contents (response)
        # if(False):

        buyBox = response.css('div.game_area_purchase_game_wrapper')
        # if(response.css('div.discount_final_price::text')):
        if(buyBox[0].css('div.discount_final_price::text')):
            steamGame = SteamGameLoader(item = SteamGame(), selector = buyBox)
            # steamGame.add_css('name', 'div.apphub_AppName::text')
            steamGame.add_value('name', ' '.join(buyBox.css('h1::text').get().split(' ')[1:]))
            steamGame.add_value('onSale', 'YES')
            steamGame.add_value('currency', buyBox.css('div.discount_final_price::text').get())
            steamGame.add_css('price', 'div.discount_final_price::text')
            steamGame.add_value('url', response.url)
            yield steamGame.load_item()
        
        else:
            steamGame = SteamGameLoader(item = SteamGame(), selector = buyBox)
            # steamGame.add_css('name', 'div.apphub_AppName::text')
            steamGame.add_value('name', ' '.join(buyBox.css('h1::text').get().split(' ')[1:]))
            steamGame.add_value('onSale', 'NO')
            steamGame.add_value('currency', buyBox.css('div.game_purchase_price.price::text').get())
            steamGame.add_css('price', 'div.game_purchase_price.price::text')
            steamGame.add_value('url', response.url)
            yield steamGame.load_item()
        #I didn't have to use pipelines for now because I could fix the price format in the Item Loader with a cheap trick


"""Below all of this will be my deprecated spider code which I find annoying being above"""

        #No scrapy.Item application
        # yield{
        #     'name': response.css('div.apphub_AppName::text').get(),
        #     'price': response.css('div.game_purchase_price.price::text').get().replace("\r\n\t\t\t\t\t\t\t", '').replace("\t\t\t\t\t\t", ''),
        #     'url': response.url
        # }

        #scrapy.Item application
        # steamGame = SteamGame()
        # steamGame['name'] = response.css('div.apphub_AppName::text').get()
        # steamGame['price'] = response.css('div.game_purchase_price.price::text').get().replace("\r\n\t\t\t\t\t\t\t", '').replace("\t\t\t\t\t\t", '')
        # steamGame['url'] = response.url
        # yield steamGame