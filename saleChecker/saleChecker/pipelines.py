# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import psycopg2

#I did the pipeline job in the itemloaders
class PriceCleanerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
            adapter['price'] = float(adapter['price'])

            return item
        else:
            raise DropItem(f"Missing price in {item}")

class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = psycopg2.connect(
            host = "localhost",
            database = "steamgames",
            user = "postgres",
            password = "160527"
        )
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        try:
            #ESTO DE ACA ABAJO TIENE QUE SER UN TUPLE OBLIGADO POR LO TANTO LA ',' TIENE QUE IR
            self.curr.execute("SELECT * FROM juegos WHERE name = %s", (item["name"],))
            existing_row = self.curr.fetchone()

            # if the row exists, update it
            if existing_row:
                self.curr.execute("UPDATE juegos SET onsale = %s, currency = %s, price = %s WHERE name = %s", (item['onSale'], item['currency'], item['price'], item['name']))
            # otherwise, insert a new row
            else:
                self.curr.execute("INSERT INTO juegos (name, onsale, currency, price, url) VALUES (%s, %s, %s, %s, %s)", (item["name"], item["onSale"], item["currency"], item["price"], item["url"]))
            #########################

            self.connection.commit()
        except BaseException as e:
            print(e)
            self.connection.rollback()