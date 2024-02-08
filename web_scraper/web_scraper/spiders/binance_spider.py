from scrapy import Spider
from web_scraper.items import WebScraperItem

class BinanceSpiderSpider(Spider):
    name = "binance_spider"
    allowed_domains = ["binance.us"]
    start_urls = ["https://www.binance.us/price"]

    def parse(self, response):
        if response.url == "https://www.binance.us/price":
            pair_names = response.css('h4.sc-aXZVg.dKubqp.asset::text').getall()
            pair_prices = response.css('div.sc-kFWlue.ecuGZa::text').getall()
            daily_changes = response.xpath('//span[@class="sc-satoz jCpdXl"]/text()').getall()
            daily_highs = response.css('td.rc-table-cell > div.sc-krNlru.czmfVu::text').getall()
            daily_lows = response.xpath('//div[@class="sc-isRoRg dlnfsM"]/text()').getall()
            volumes = response.xpath('//div[@class="sc-isRoRg dlnfsM"]/text()').getall()
            market_caps = response.xpath('//div[@class="sc-isRoRg dlnfsM"]/text()').getall()

            for pair_name in pair_names:
                web_item = WebScraperItem()
                web_item['url'] = response.url
                web_item['pair_name'] = pair_name
                web_item['pair_price'] = pair_prices
                web_item['daily_change'] = daily_changes
                web_item['daily_high'] = daily_highs
                web_item['daily_low'] = daily_lows
                web_item['volume'] = volumes
                web_item['market_cap'] = market_caps  

                yield web_item
