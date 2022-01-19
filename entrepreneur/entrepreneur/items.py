# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EntrepreneurItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    category = scrapy.Field()
    initial_investment = scrapy.Field()
    industry = scrapy.Field()
    # founded = scrapy.Field()
    # parent_company = scrapy.Field()
    # leadership = scrapy.Field()
    # ticker_symbol = scrapy.Field()
    # related_category = scrapy.Field()
    # franchising_since = scrapy.Field()
    # employees_at_hq = scrapy.Field()
    # number_of_unit = scrapy.Field()
    # as_of = scrapy.Field()
    # growth = scrapy.Field()
    # initial_franchise_fee = scrapy.Field()
    # initial_franchise_fee_2 = scrapy.Field()
    # net_worth_requirement = scrapy.Field()
    # cash_requirement = scrapy.Field()
    # royalty_fee = scrapy.Field()
    # ad_royalty_fee = scrapy.Field()
    # term_of_agreement = scrapy.Field()
    # franchise_renewable = scrapy.Field()
    # financing_options = scrapy.Field()
    # onthejob_training = scrapy.Field()
    # classroom_training = scrapy.Field()
    # additional_training = scrapy.Field()
    # ongoing_support = scrapy.Field()
    # marketing_support = scrapy.Field()
    # is_absentee_ownership_allowed = scrapy.Field()
    # run_from_home = scrapy.Field()
    # run_part_time = scrapy.Field()
    # exclusive_territories_available = scrapy.Field()
    page_url = scrapy.Field()
    # pass
