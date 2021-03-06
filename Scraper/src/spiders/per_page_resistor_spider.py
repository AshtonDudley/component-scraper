import re
import scrapy 


class AvResistorSpider(scrapy.Spider):
    name = "av_resistor"
    
    start_urls = ['https://www.taydaelectronics.com/resistors/1-4w-metal-film-resistors.html']
        

    def parse(self, response):   
    
        resistor_page_links = response.css('a.product-item-link')
        yield from response.follow_all(resistor_page_links, self.parse_resistor)


        pagination_links = response.css('a.action.next::attr(href)')
        yield from response.follow_all(pagination_links, callback=self.parse)

    def parse_resistor(self, response):
        yield {
            'Part Name' : response.css("span.base::text").get(),
            'Description' : response.css("span.base::text").get(),
            'Manufacturer Part' : AvResistorSpider.parse_info(self, response)[0],
            'Resistance' : AvResistorSpider.parse_info(self, response)[2] + "R", 
            'Manufacturer' : 'Royal OHM',
            'Supplier 1' : 'Tayda Electronics',
            'Supplier Part Number 1' : response.css("td.col.data::text").get(),
            'Length': '52mm', 
            'Voltage Rating (DC)': '0.25W',
            'Tolerance' : '1%',
            'Resistor Type' : 'Metal Film',
            'Case/Package' : 'Axial',
            'Category' : 'Through-Hole Resistor',
            'Library Ref' : 'Resistor',
            'Library Path' : 'Symbols\Resistors.SchLib',
            'Footprint Path' : 'Footprints\Resistors.PcbLib',
            'Footprint Ref' : '6.8MM.9',
            'Comment' : AvResistorSpider.parse_info(self, response)[2],
            
        }

    def parse_info(self, response):
        info = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[4]/div/div[2]/center//text()').extract()
        rep =[]
        out = ["NULL","NULL","NULL",]

        for i in info:
            rep.append(i.strip())

        for i in rep:
            if re.search("MF............*", i):
                out[0] = re.search("MF............",i).group()
            elif i == 'Manufacturer: Royal OHM':
                out[1] = "Royal OHM"
            elif re.search("^Resistan", i):
                out[2] =re.search("[.?\d]+[K|M]?", i).group()
        return(out)


            



