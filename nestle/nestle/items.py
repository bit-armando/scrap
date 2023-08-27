# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Receta(scrapy.Item):
    nombre = scrapy.Field()
    porciones = scrapy.Field()
    ingredientes = scrapy.Field()
    pasos = scrapy.Field()
    pass
