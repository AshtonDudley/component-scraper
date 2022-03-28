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
                'Supplier Part Number' : resistor.css("div.product.sku-qty.product-item-sku-qty::text").get().strip().replace(" ","").replace("\n","").replace("|",":").split(':')[1],
                'Resistance' : resistor.css("a.product-item-link::text").get().strip().split(' ')[0],
            }
        next_page = response.css('a.action.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            