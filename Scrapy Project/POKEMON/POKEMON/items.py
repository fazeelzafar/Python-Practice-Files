# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    total = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    sp_atk = scrapy.Field()
    sp_def = scrapy.Field()
    speed = scrapy.Field()
    icon_url = scrapy.Field()
    
    pass
