import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookItem


class BookscrapeSpider(CrawlSpider):
    name = 'bookscrape'
    allowed_domains = ['books.toscrape.com']
    #start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'catalogue/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        url='http://books.toscrape.com/'
        yield scrapy.Request(url)

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        if response.xpath('//div[@class="col-sm-6 product_main"]').get() is not None :
            title = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
            price = response.xpath('//div[@class="col-sm-6 product_main"]/p[1]/text()').get()
            type = response.xpath('//*[@id="default"]/div[1]/div/ul/li[3]/a/text()').get()
            rating = response.xpath('//div[@class="col-sm-6 product_main"]/p[3]/@class').get()

            item=BookItem()
            item['title']= title
            item['price']=price
            item['type']=type
            item['rating']=rating
            yield item

