from re import S
import scrapy 


class AvResistorSpider(scrapy.Spider):
    name = "av_resistor"

    
    start_urls = ['https://www.taydaelectronics.com/resistors/1-4w-metal-film-resistors.html']
        

    def parse(self, response):   
    
        resistor_page_links = response.css('a.product-item-link')
        yield from response.follow_all(resistor_page_links, self.parse_resistor)


        pagination_links = response.css('a.action.next::attr(href)').get()
        yield from response.follow_all(pagination_links, callback=self.parse)

    def parse_resistor(self, response):
        yield {
            'Part Name' : response.css("span.base::text").get(),
        }


        
        # for resistor in response.css("div.product-item-info"):
        #     yield {
        #         'Part Name' : resistor.css("a.product-item-link::text").get().strip(),
        #         'Price' : resistor.css("span.price::text").get(),
        #         'Supplier Link' : resistor.css("a.product-item-link::attr(href)").get(),
        #         'Supplier Part Number' : resistor.css("div.product.sku-qty.product-item-sku-qty::text").get().strip().replace(" ","").replace("\n","").replace("|",":").split(':')[1],
        #         'Resistance' : resistor.css("a.product-item-link::text").get().strip().split(' ')[0],
        #     }
        # next_page = response.css('a.action.next::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)