import scrapy
import re
from nestle.items import Receta

class EkiluSpider(scrapy.Spider):
    name = "ekilu"
    allowed_domains = ["ekilu.com"]
    custom_settings = {'FEED_FORMAT': 'json',
                       'FEED_URI': 'resultados.json',
                       'FEED_EXPORT_ENCODING': 'utf-8'
                       }
    start_urls = ["https://ekilu.com/es/recetas/hamburguesas",
                  "https://ekilu.com/es/recetas/pollo?page=2"]

    
    def parse(self, response):
        # Obtener recetas
        recetas_item = response.xpath('//div[@class="card result-item-card"]/a/@href').getall()
        for receta in recetas_item:
            yield response.follow(receta, callback=self.parse_receta)
    
    def parse_receta(self, response):
        titulo = response.xpath('//div[@class="recipe__content"]/h1/text()').get()
        
        porciones = response.xpath('//div[@class="number-counter"]/p/text()').get()
        patron = r"\d+"
        porciones = int(re.search(patron, porciones).group())
        
        ingredientes = response.xpath('//div[@class="body3-text color-ek-darkpurple-text"]/text()').getall()
        cantidad_ingredientes = response.xpath('//div[@class="item__value-measure body3-text"]/p/span/text()').getall()
        unidad_ingredientes = response.xpath('//div[@class="item__value-measure body3-text"]/p/text()').getall()
        for i in range(0, len(ingredientes)):
            ingredientes[i] = ingredientes[i] + ' ' + cantidad_ingredientes[i] + unidad_ingredientes[i]
        
        pasos = response.xpath('//div[@class="item__text body3-text color-ek-darkpurple-text"]/text()').getall()
        
        receta = Receta()
        receta['nombre'] = titulo
        receta['porciones'] = porciones
        receta['ingredientes'] = ingredientes
        receta['pasos'] = pasos
        
        yield receta
    
