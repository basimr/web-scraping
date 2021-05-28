import scrapy


class OurCommonsSpider(scrapy.Spider):
    name = "ourcommons_spider"
    start_urls = ['https://www.ourcommons.ca/Members/en/search']

    def parse(self, response):
        for mp in response.css(".ce-mip-mp-tile"):
            yield {
                'name': mp.css(".ce-mip-mp-name::text").get(),
                'party': mp.css(".ce-mip-mp-party::text").get(),
            }
