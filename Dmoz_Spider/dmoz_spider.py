import scrapy

from tutor.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['http://www.dmoztools.net']
    start_urls=[
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
        ]

    def parse(self,response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div/div/div/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div[@class="site-title"]/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract()
            items.append(item)
        return items
