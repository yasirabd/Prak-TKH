import scrapy
from tripadvisor.items import TripadvisorItem

#TODO use loaders
class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    start_urls = ["https://www.tripadvisor.co.id/Hotels-g297712-Semarang_Central_Java_Java-Hotels.html"]

    def parse(self, response):
        # untuk masuk ke dalam url dari setiap item hotel dengan mengambil dari class="listing_title" kemudian mengambil link dari atribut href
        for href in response.xpath('//div[@class="listing_title"]/a/@href'):
            url = response.urljoin(href.extract())

            # menjalankan fungsi parse_hotel
            yield scrapy.Request(url, callback=self.parse_hotel)

        # untuk melakukan crawling pada page berikutnya
        next_page = response.xpath('//div[@class="unified pagination standard_pagination"]/child::*[2][self::a]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_hotel(self, response):
        # masuk ke dalam url dari setiap item review yang diawali dengan class="quote" kemudian mengambil link dari atribut href
        for href in response.xpath('//div[starts-with(@class,"quote")]/a/@href'):
            url = response.urljoin(href.extract())

            # menjalankan fungsi parse_review
            yield scrapy.Request(url, callback=self.parse_review)

        # untuk melakukan crawling pada page berikutnya
        next_page = response.xpath('//div[@class="unified pagination "]/child::*[2][self::a]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_hotel)


    #to get the full review content I open its page, because I don't get the full content on the main page
    #there's probably a better way to do it, requires investigation
    def parse_review(self, response):
        item = TripadvisorItem()

        item['title'] = response.xpath('//div[@class="quote"]/text()').extract()[0][1:-1]   # strip the quotes (first and last char)
                                                                                            # menghilangkan karakter pertama dan terakhir yaitu tanda ""
        item['content'] = response.xpath('//div[@class="entry"]/p/text()').extract()[0]

        item['stars'] = response.xpath('//span[@class="rate sprite-rating_s rating_s"]/img/@alt').extract()[0]  # mendapatkan data pada atribut alt
                                                                                                                # yang terdapat pada tag <img>
        return item
