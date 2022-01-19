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

        # pagination = response.css(
        #     '#childContainerDom > div:nth-child(13) > div > div > div:nth-child(2) > div:nth-child(2) > nav > a:last-child::attr(href)').get()
        # if pagination:
        #     yield scrapy.Request(url=response.urljoin(pagination), callback=self.parse)

    def parse_details(self, response):

        item = EntrepreneurItem()

        item['name'] = response.css('h1::text').get().strip()
        item['category'] = response.css('#mainDom > div > div  > div > div > div:nth-child(2) > a::text').get().strip()
        item['initial_investment'] = response.css('#childContainerDom > div > div  > div  > div  > div > div > dl > dd > div > span::text').get().strip()
        item['industry'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > dl > dd > a::text').get().strip()
        # item['founded'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(3) > dl > dd::text').get().strip()
        # item['parent_company'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(4) > dl > dd::text').get().strip()
        # item['leadership'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(5) > dl > dd::text').get().strip()
        # item['ticker_symbol'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(6) > dl > dd::text').get().strip()
        # item['related_category'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(3) > div > div > div:nth-child(2) > dl > dd> a::text').get()
        # item['franchising_since'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(4) > div:nth-child(2) > div > div > dl > dd::text').get().strip()
        # item['employees_at_hq'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(2) > dl > dd: : text').get().strip()
        # item['number_of_unit'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(4) > dl > dd: : text').get().strip()
        # item['as_of'] = response.css('#childContainerDom > div:nth-child(5) > div > div > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(4) > dl > dd > span: : text').get().replace('(as of','').replace(')','').strip()
        # item['growth'] = response.css('#childContainerDom > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(2) > div > div > dl > dd > div > span:nth-child(2)::text').extract()[
        #     1].strip().replace('over 3 years', '').strip()

        # selectorFinancialReq = '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(7) > div:nth-child(2) > div';
        # item['initial_franchise_fee'] = response.css( selectorFinancialReq + ' > div > dl > dd::text').get().strip()
        # item['initial_franchise_fee_2'] = response.css( selectorFinancialReq + ' > div:nth-child(2) > dl > dd::text').get().strip()
        # item['net_worth_requirement'] = response.css( selectorFinancialReq + ' > div:nth-child(3) > dl > dd::text').get().strip()
        # item['cash_requirement '] = response.css( selectorFinancialReq + ' > div:nth-child(4) > dl > dd::text').get().strip()
        # item['royalty_fee'] = response.css( selectorFinancialReq + ' > div:nth-child(5) > dl > dd::text').get().strip()
        # item['ad_royalty_fee'] = response.css( selectorFinancialReq + ' > div:nth-child(6) > dl > dd::text').get().strip()
        # item['term_of_agreement '] = response.css( selectorFinancialReq + ' > div:nth-child(7) > dl > dd::text').get().strip()
        # item['franchise_renewable '] = response.css( selectorFinancialReq + ' > div:nth-child(8) > dl > dd::text').get().strip()
        # item['financing_options '] = response.css('#childContainerDom > div:nth-child(5) > div > div  > div:nth-child(8) > div  > div > div > dl > dd::text').get().strip()
       
        # selectorTraining = '#childContainerDom > div:nth-child(5) > div > div  > div:nth-child(9) > div  > div '
        # item['onthejob_training '] = response.css(selectorTraining + ' > div:nth-child(1) > dl > dd::text').get().strip()
        # item['classroom_training '] = response.css(selectorTraining + ' > div:nth-child(2) > dl > dd::text').get().strip()
        # item['additional_training '] = response.css(selectorTraining + ' > div:nth-child(3) > dl > dd::text').get().strip()
        # item['ongoing_support '] = ', '.join(response.css(selectorTraining + '> div:nth-child(4) > dl > dd > div > div > span::text').getall())
        # item['marketing_support '] = ', '.join(response.css(selectorTraining + '> div:nth-child(5) > dl > dd > div > div > span::text').getall())
        
        # selectorOperation = '#childContainerDom > div:nth-child(5) > div > div > div:nth-child(10) > div > div > '
        # item['is_absentee_ownership_allowed'] = response.css(selectorOperation + 'div:nth-child(1) > dl > dd::text').get().strip()
        # item['run_from_home'] = response.css(selectorOperation + 'div:nth-child(2) > dl > dd::text').get().strip()
        # item['run_part_time'] = response.css(selectorOperation + 'div:nth-child(3) > dl > dd::text').get().strip()
        # item['exclusive_territories_available'] = response.css(selectorOperation + 'div:nth-child(4) > dl > dd::text').get().strip()
        item['page_url'] = response.url

        yield item
       

 