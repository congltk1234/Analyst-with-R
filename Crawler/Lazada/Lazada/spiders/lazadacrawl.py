import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LazadaItem


class LazadacrawlSpider(CrawlSpider):
    name = 'lazadacrawl'
    allowed_domains = ['lazada.vn']
    #start_urls = ['http://lazada.vn/']

    rules = (
        Rule(LinkExtractor(allow=r'products/',restrict_xpaths='//*[@id="root"]/div/div[3]/div[1]/div/div[1]', tags='a', attrs='href'), callback='parse_item', follow=True),
    )

    order_number = 1

    

    def start_requests(self):
        url = "https://www.lazada.vn/"
        yield scrapy.Request(url)

    def start_requests(self):
        base_url = "https://www.lazada.vn/laptop/?page="
        for i in range(1,3):
            yield scrapy.Request(url = base_url+str(i), callback=self.parse_link)
    def parse_link(self, response):
        for products in response.css("div._8JShU"):
            link = "https://www.lazada.vn/" + products.css("div a::attr(href)").get()
            yield scrapy.Request(url = link, callback=self.parse_item)    

    def parse_item(self, response):
            product_name = response.xpath('//*[@id="module_product_title_1"]/div/div/h1/text()').get()
            price = response.xpath('//*[@id="module_product_price_1"]/div/div/span/text()').get()
            shop = response.xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a/text()').get()
            category = response.xpath('//*[@id="J_breadcrumb"]/li[3]/span/a/span/text()').get()
            label = response.xpath('//*[@id="module_product_detail"]/div/div/div[1]/div[4]/div[1]/ul/li[1]/div/text()')

            item=LazadaItem()
            item['price']=price
            item['product_name']=product_name
            item['shop']=shop
            item['category'] = category
            item['label']=label
            yield item