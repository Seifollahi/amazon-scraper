import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from ..items import AmazonItem
from ..items import AmazonItemProducts



class BestsellerProductsSpider(CrawlSpider):
    name = "bestsellersproducts"
    allowed_domains = ["amazon.ca"]
    start_urls = [
            "https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0",
            
        ]

    rules = [
        Rule(LinkExtractor(deny = r'product-reviews.*$', restrict_xpaths = "//a[@class='a-link-normal']", unique= True), callback='parse', follow=True),
        Rule(LinkExtractor(allow=r'Best-Sellers-.*$', restrict_xpaths = "//ul[@id='zg_browseRoot']", unique= True)),

    ]


    def parse(self, response):
        item = AmazonItemProducts()
        
        item["product_title"] = response.xpath("//span[@id='productTitle']/text()").get()
        item["product_main_store"] = response.xpath("//a[@id = 'bylineInfo']/text()").get()
        item["product_main_store_url"] = response.xpath("//a[@id = 'bylineInfo']/@href").get()
        item["product_rating"] = response.xpath("//span[@class='a-icon-alt']/text()").get()
        item["product_number_of_ratings"] = response.xpath("//span[@id='acrCustomerReviewText']/text()").get()
        item["product_number_of_answered_questions"] = response.xpath("//div[@id='ask_feature_div']//span[@class='a-size-base']/text()").get()
        item["product_rank"] = response.xpath("//i[@class='a-icon a-icon-addon p13n-best-seller-badge']/text()").get()
        item["product_main_department"] = response.xpath("//i[@class='a-icon a-icon-addon p13n-best-seller-badge']/text()").get()
        item["product_last_price"] = response.xpath("//span[@class='priceBlockStrikePriceString a-text-strike']/text()").get()
        item["product_price"] = response.xpath("//span[@id='priceblock_ourprice']/text()").get()
        item["prpduct_price_per_unit"] = response.xpath("//td[@class ='a-span12']/span[@class='a-size-small a-color-price']/text()").get()
        item["product_price_saving"] = response.xpath("//td[@class ='a-span12 a-color-price a-size-base priceBlockSavingsString']/text()").get()
        item["product_default_selection"] = response.xpath("//span[@class='selection']/text()").get()
        
        yield item