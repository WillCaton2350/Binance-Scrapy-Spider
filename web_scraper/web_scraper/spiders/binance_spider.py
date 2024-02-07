from scrapy import Spider
from web_scraper.items import WebScraperItem

class BinanceSpiderSpider(Spider):
    name = "binance_spider"
    allowed_domains = ["binance.us"]
    start_urls = ["https://www.binance.us/price"]

    def parse(self, response):
        web_item = WebScraperItem()
        web_item['url'] = response.url
        web_item['pair_name'] = None
        web_item['pair_price'] = None
        web_item['daily_change'] = None
        web_item['daily_high'] = None
        web_item['daily_low'] = None
        web_item['volume'] = None
        web_item['market_cap'] = None
    
        if response.url == "https://www.binance.us/price":
            web_item['pair_name'] = response.css('h4.sc-aXZVg.dKubqp.asset::text').getall()
            web_item['pair_price'] = response.css('div.sc-guJBdh.bGIose::text').getall()
            web_item['daily_change'] = response.css('span.sc-hwdzOV.cMnvhL::text').getall()
            web_item['daily_high'] = response.css('div.sc-krNlru.czmfVu::text').getall()
            web_item['daily_low'] = response.css('div.sc-isRoRg.dlnfsM::text').getall()
            web_item['volume'] = response.css('div.sc-isRoRg.dlnfsM::text').getall()
            web_item['market_cap'] = response.css('div.sc-isRoRg.dlnfsM::text').getall()
            yield web_item
