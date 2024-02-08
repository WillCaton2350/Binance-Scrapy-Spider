from psycopg2.errors import ConnectionFailure
from psycopg2.errors import DataError
import psycopg2
import logging

class WebScraperPipeline:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                user='user',
                password='password',
                database='database',
                port = '0000'
            )
        except ConnectionFailure as err:
            logging.error(f'{err}')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS binance_tb 
            (
                url character(1000),
                pair_name character(1000),
                pair_price character(1000),
                daily_change character(1000),
                daily_high character(1000),
                daily_low character(1000),
                volume character(1000),
                market_cap character(1000)
            )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        try:    
            self.cur.execute(
                """INSERT INTO binance_tb (
                url, 
                pair_name,
                pair_price, 
                daily_change, 
                daily_high, 
                daily_low, 
                volume, 
                market_cap
                ) 
                VALUES (%s, %s, %s, %s, 
                %s, %s, %s, %s)
                """, 
            (
                item['url'],
                item['pair_name'],
                item['pair_price'],
                item['daily_change'],
                item['daily_high'],
                item['daily_low'],
                item['volume'],
                item['market_cap']
            ))
        except DataError as err:
            logging.error(f'{err}')
        self.conn.commit()
        
    def close_spider(self, spider):
        self.conn.close()
        self.cur.close()
