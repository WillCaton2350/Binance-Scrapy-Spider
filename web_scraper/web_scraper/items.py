from scrapy import Item, Field

class WebScraperItem(Item):
    url = Field()
    pair_name = Field()
    pair_price = Field()
    daily_change = Field()
    daily_high = Field()
    daily_low = Field()
    volume = Field()
    market_cap = Field()