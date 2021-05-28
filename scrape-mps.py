import scrapy


class OurCommonsSpider(scrapy.Spider):
    name = "ourcommons_spider"
    start_urls = ['https://www.ourcommons.ca/Members/en/search']

    def parse(self, response):
        for mp in response.css(".ce-mip-mp-tile"):
            mp_name = mp.css(".ce-mip-mp-name::text").get()
            mp_party = mp.css(".ce-mip-mp-party::text").get()

            data = {
                'name': mp_name,
                'party': mp_party,
            }

            details_address = mp.attrib['href']
            details_url = response.urljoin(details_address)
            request = scrapy.Request(details_url,
                                     callback=self.parse_details,
                                     cb_kwargs=dict(data=data))

            yield request

    def parse_details(self, response, data):
        a = response.css("#contact div.container p a")[0]
        mailto_link = a.attrib["href"]
        email = mailto_link.removeprefix("mailto:")
        data['email'] = email
        yield data
