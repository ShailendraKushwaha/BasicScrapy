import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'MySpider'
    start_urls = ['https://www.net-a-porter.com/en-in/shop/clothing/tops']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
       
        for container in response.css("div.ProductListWithLoadMore52__listingGrid").css("a"):
         yield {
              'name':container.css("span.ProductItem24__name::text").get(),
              'brand':container.css("span.ProductItem24__designer::text").get(),
              'sale_price': float(container.css("span.PriceWithSchema9__value").css("span::text").get().replace("$","").replace(",","")),
              'original_price': float(container.css("span.PriceWithSchema9__value").css("span::text").get().replace("$","").replace(",","")),
              'image_url': container.css("img.Image18__image::attr(src)").get(),
              'product_page_url': container.attrib['href'],
              'product_category':"topwear"
            }

        next_page =  response.css("a.Pagination7__next").attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)