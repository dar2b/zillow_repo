from scrapy import zillow
from zillow.items import ZillowItem

class BestBuySpider(Spider):
    name = 'zillow_spider'
    allowed_urls = ['https://www.zillow.com/']
    start_urls = ['https://www.zillow.com/homes/for_sale/Gloucester-County-NJ/38765394_zpid/2929_rid/globalrelevanceex_sort/39.969227,-74.555283,39.430359,-75.748672_rect/9_zm/']
    def parse(self, response):
        pass