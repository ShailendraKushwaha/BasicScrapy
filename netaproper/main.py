import scrapy

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'https://www.net-a-porter.com/en-in/shop/clothing/tops'
    ]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)