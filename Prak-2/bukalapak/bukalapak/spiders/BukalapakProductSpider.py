import scrapy
from bukalapak.items import BukalapakItem

class BukalapakProductSpider(scrapy.Spider):
    name = "BukalapakDeals"
    allowed_domains = ["bukalapak.com"]

    #Use working product URL below
    start_urls = [
        "https://www.bukalapak.com/p/komputer/laptop/43mglk-jual-laptop-hp-8560w-elitebook-workstation-core-i7", 
        "https://www.bukalapak.com/p/komputer/laptop/3sz46v-jual-hp-1000",
        "https://www.bukalapak.com/p/komputer/laptop/43ohlq-jual-dell-e6420-core-i5", 
        "https://www.bukalapak.com/p/komputer/laptop/45uqjz-jual-macbook-white-core-2-duo-mulus-normal-lancar"
    ]

    def parse(self, response):
        items = BukalapakItem()
        name = response.xpath('//h1[@itemprop="name"]/text()').extract()
        category = response.xpath('//dd[@itemprop="category"]/text()').extract()
        currency_price = response.xpath('//span[@itemprop="priceCurrency"]/text()').extract()
        price = response.xpath('//span[@itemprop="price"]/text()').extract()

        items['product_name'] = ''.join(name).strip()
        items['product_category'] = ''.join(category).strip()
        items['product_currency_price'] = ''.join(currency_price).strip()
        items['product_price'] = ''.join(price).strip()
        
        yield items