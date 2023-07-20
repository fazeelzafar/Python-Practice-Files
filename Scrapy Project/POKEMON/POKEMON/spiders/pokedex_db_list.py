import scrapy
from POKEMON.items import PokemonItem


class PokedexDbListSpider(scrapy.Spider):
    name = 'pokedex_db_list'
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net/pokedex/all"]

    def parse(self, response):
        rows = response.css('tbody > tr')

        for row in rows:
            item = PokemonItem()
            item["name"] = row.css('a.ent-name::text').get()
            item["type"] = row.css('td.cell-icon a::text').getall()
            item["total"] = row.css('td.cell-total::text').get()
            item["hp"] = row.css('td.cell-num:nth-child(3)::text').get()
            item["attack"] = row.css('td.cell-num:nth-child(4)::text').get()
            item["defense"] = row.css('td.cell-num:nth-child(5)::text').get()
            item["sp_atk"] = row.css('td.cell-num:nth-child(6)::text').get()
            item["sp_def"] = row.css('td.cell-num:nth-child(7)::text').get()
            item["speed"] = row.css('td.cell-num:nth-child(8)::text').get()
            item["icon_url"] = row.css('span.infocard-cell-img img::attr(src)').get()

            yield item
