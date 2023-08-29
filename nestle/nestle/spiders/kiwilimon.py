import scrapy


class KiwilimonSpider(scrapy.Spider):
    name = "kiwilimon"
    allowed_domains = ["www.kiwilimon.com"]
    start_urls = ["https://www.kiwilimon.com"]

    def parse(self, response):
        pass
