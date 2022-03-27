import scrapy 


class ResistorSpider(scrapy.Spider):
    name = "resistor"
    start_urls = [
        'https://www.taydaelectronics.com/resistors/1-4w-metal-film-resistors.html',
    ]

    def parse(self, response):
        for resistor in response.css("div.product-item-info"):
            yield {
                'Part Name' : resistor.css("a.product-item-link::text").get().strip(),
                'Price' : resistor.css("span.price::text").get(),
                'Supplier Link' : resistor.css("a.product-item-link::attr(href)").get(),
            }