# import scrapy


# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     allowed_domains = ["example.com"]
#     start_urls = ["https://quotes.toscrape.com/page/1/"]

#     def parse(self, response):
#         title = response.css('title::text').extract()
#         yield {'titletext':title}
        
from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')