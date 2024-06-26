from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import scrapy

# item models
from craigslist.items import CraigslistItem, CraigslistItemDetail

class CraigslistSpider(CrawlSpider):

    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        #"http://sfbay.craigslist.org/search/sfc/apa"
        "http://sfbay.craigslist.org/search/sss?query=rv"
    ]

    rules = (
            Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_search", follow = True),
            #Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="hdrlnk"]',)), callback="parse_page", follow = True),
     )


    def parse_search(self, response):
        """
                We will be retiring our parse_search method
        """

        for sel in response.xpath("//p[@class='row']"):

            item = CraigslistItem()
            #item['title'] =  sel.xpath("//span/a[@class='hdrlnk']/text()").extract()[0]
            #item['link']  =  sel.xpath("span/span/a/@href").extract()[0]
            item['price'] =  sel.xpath("//span[@class='price']/text()").extract()[0]
            yield item
