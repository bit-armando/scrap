import re
from time import sleep
import scrapy
from nestle.items import Receta


class NestleSpider(scrapy.Spider):
    name = "nestle"
    allowed_domains = ["recetasnestle.com.mx"]
    custom_settings = {'FEED_FORMAT': 'json',
                       'FEED_URI': 'resultados.json',
                       'FEED_EXPORT_ENCODING': 'utf-8',
                       }
    start_urls = ['https://www.recetasnestle.com.mx/categorias/platos-fuertes',
                #   'https://www.recetasnestle.com.mx/categorias/bebidas',
                #   'https://www.recetasnestle.com.mx/categorias/postres',
                #   'https://www.recetasnestle.com.mx/categorias/cenas',
                #   'https://www.recetasnestle.com.mx/categorias/lunch',
                #   'https://www.recetasnestle.com.mx/categorias/en-frio',
                #   'https://www.recetasnestle.com.mx/categorias/al-sarten',
                  ]
        
    def parse(self, response):       
        # Listado de recetas
        recetas_item = response.xpath('//div[@class="page-contents"]//article/a/@href').getall()
        for receta in recetas_item:
            yield response.follow(receta, callback=self.parse_reseta)    
    
    def parse_reseta(self, response):
        receta = Receta()
        
        nombre = response.xpath('//h1[@class="hl-1 mb-4"]/text()').get()
        receta['nombre'] = nombre.strip()
        receta['porciones'] = int(response.xpath('//div[@class="recipeDetail__infoItem recipeDetail__infoItem--serving"]/span/text()').get())
        
        
        """CREAR FUNCION

            Se puede crear una funcion en el cual solo trate a las listas con tags para no repetir 
            mucho las list comprehension
        """
        # Obtencion de los ingredientes y los pasos de la receta
        ingredientes = response.xpath('//div[@class="recipeDetail__ingredients"]/ul/li/text()').getall()
        ingredientes = [re.sub(r'[\n\t]', '', elemento.strip()) for elemento in ingredientes]
        receta['ingredientes'] = ingredientes
        
        pasos = response.xpath('//div[@class="recipeDetail__stepItem"]//ul/li/label/div/text()').getall()
        pasos = [re.sub(r'[\n\t]', '', elemento.strip()) for elemento in pasos]
        receta['pasos'] = pasos
        
        yield receta