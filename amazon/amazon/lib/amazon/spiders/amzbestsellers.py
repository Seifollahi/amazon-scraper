import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from ..items import AmazonItem



class BestsellerSpider(CrawlSpider):
    name = "bestsellers"
    allowed_domains = ["amazon.ca"]
    start_urls = [
            "https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0",
            
        ]

    rules = [
        Rule(LinkExtractor(allow=r'Best-Sellers-.*$', restrict_xpaths = "//ul[@id='zg_browseRoot']", unique= True), callback='parse', follow=True),
    ]


    def parse(self, response):
        item = AmazonItem()

        item_response = response.xpath("//li[@class='zg-item-immersion']")
        
        selected_department = response.xpath("//ul[@id='zg_browseRoot']//span[@class='zg_selected']/text()").get()
        
        for items in item_response:
            product_title = items.xpath(".//div[1]/text()").get()
            rank = items.xpath(".//span[@class='zg-badge-text']/text()").get()
            rating = items.xpath(".//span[@class='a-icon-alt']/text()").get()
            number_of_ratings = items.xpath(".//a[@class='a-size-small a-link-normal']/text()").get()
            product_reviews_url = items.xpath(".//a[@class='a-size-small a-link-normal']/@href").get()
            price = items.xpath(".//span[@class='p13n-sc-price']/text()").get()

        
        item["selected_department"] = selected_department
        item["product_title"] = product_title
        item["rank"] = rank
        item["rating"] = rating
        item["number_of_ratings"] = number_of_ratings
        item["product_reviews_url"] = product_reviews_url
        item["price"] = price
        
        yield item