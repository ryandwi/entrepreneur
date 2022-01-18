from urllib.parse import urljoin
import scrapy
from entrepreneur.items import EntrepreneurItem


class EntSpider(scrapy.Spider):
    name = 'ent'
    allowed_domains = ['entrepreneur.com']
    start_urls = ['https://www.entrepreneur.com/franchise500']

    def parse(self, response):
        firstRow = response.css(
            '#list > div > ul > li:not(:first-child) > div > div >div > a:first-child::attr(href)').getall()
        secondRow = response.css(
            '#childContainerDom > div:nth-child(7) > div > ul > li > div >div > div > a:first-child::attr(href)').getall()
        thirdRow = response.css(
            '#childContainerDom > div:nth-child(9) > div > ul > li > div >div > div > a:first-child::attr(href)').getall()
        fourRow = response.css(
            '#childContainerDom > div:nth-child(11) > div > ul > li > div >div > div > a:first-child::attr(href)').getall()
        fifthRow = response.css(
            '#childContainerDom > div:nth-child(13) > div > ul > li > div >div > div > a:first-child::attr(href)').getall()

        urls = firstRow + secondRow + thirdRow + fourRow + fifthRow

        for url in urls:
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_details)

        pagination = response.css(
            '#childContainerDom > div:nth-child(13) > div > div > div:nth-child(2) > div:nth-child(2) > nav > a:last-child::attr(href)').get()
        if pagination:
            yield scrapy.Request(url=response.urljoin(pagination), callback=self.parse)

    def parse_details(self, response):

        item = EntrepreneurItem()

        item['name'] = response.css('h1::text').get().strip()
        item['category'] = response.css(
            '#mainDom > div > div  > div > div > div:nth-child(2) > a::text').get().strip()
        item['initial_investment'] = response.css(
            '#childContainerDom > div > div  > div  > div  > div > div > dl > dd > div > span::text').get().strip()
        item['industry'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > dl > dd > a::text').get().strip()
        item['founded'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(3) > dl > dd::text').get().strip()
        item['parent_company'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(4) > dl > dd::text').get().strip()
        item['leadership'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(5) > dl > dd::text').get().strip()
        item['ticker_symbol'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(6) > dl > dd::text').get().strip()
        item['related_category'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(2) > dl > dd> a::text').get()
        item['franchising_since'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(4) > div:nth-child(2) > div > div > dl > dd::text').get().strip()
            
        item['growth'] = response.css('#childContainerDom > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(2) > div > div > dl > dd > div > span:nth-child(2)::text').extract()[
            1].strip().replace('over 3 years', '').strip()
        item['initial_franchise_fee'] = response.css(
            '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(7) > div:nth-child(2) > div > div > dl >dd::text').get().strip()
        # print(title)
        # print(growth)
        # print('*'*100)
        yield item
       

 