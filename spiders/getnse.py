import scrapy
from scrapy_splash import SplashRequest
# from scrapy.crawler import CrawlerProcess


class GpSpider(scrapy.Spider):
    name = 'gp'

    def start_requests(self):
        url = 'https://www.nseindia.com/get-quotes/equity?symbol=PSUBNKBEES'
        yield SplashRequest(url)

    def parse(self, response):
        yield {
            # 'name': response.css('td:nth-child(2) ::text()').get(),
            'title': response.css('title ::text').get(),
            'ltp': response.css('#quoteLtp ::text').get()
        }


# process = CrawlerProcess()
# process.crawl(GpSpider)
# process.start()
