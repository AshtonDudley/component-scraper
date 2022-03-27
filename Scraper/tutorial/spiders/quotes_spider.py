import scrapy 


class ResistorSpider(scrapy.Spider):
    name = "resistorOrginal"
    start_urls = [
        'https://www.taydaelectronics.com/resistors/1-4w-metal-film-resistors/test-group-2.html',
    ]

    def parse(self, response):
        for resistor in response.css("tr"):
            yield {
                'price' : resistor.css("span.price::text").get(), 
                'text' : resistor.css("strong.product-item-name::text").get(),
            }



