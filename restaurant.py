# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

import scrapy   
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import file_utils
import db_utils

db = db_utils.crear_conexion()

class TripadvisorItem(scrapy.Item):
	nombre = scrapy.Field()
	url = scrapy.Field()
	ciudad = scrapy.Field()
	direccion = scrapy.Field()
	num_valoracion = scrapy.Field()
	valoracion = scrapy.Field()
	telefono = scrapy.Field()
	url_mapa = scrapy.Field()


class TripadvisorSpider(CrawlSpider):

	custom_settings = {
        "CLOSESPIDER_ITEMCOUNT":5,   #Cantidad de elementos a buscar. Comienza a contar desde el 0.
        "CONCURRENT_REQUESTS":1,   #Cantidad de url que puede visitar a la vez.
        "CONCURRENT_ITEMS":1,   #Cantidad de elementos que puede visitar a la vez.
    }
	name = 'Tripadvisor'
	allowed_domain = ['www.tripadvisor.cl']

	busca = 'https://www.tripadvisor.cl/Restaurants-g2615220-Maule_Region.html' 
	start_urls = [busca]

	file = open("restaurant_visitados.txt", "a+") 
	file.close()

	url_visitadas = leer_datos("restaurant_visitados")

	#Reglas para la extraccion de url.
	rules = (

		#deny no permite que visite las url que ya ha procesado. restrict_xpaths le restringe moverse horizontalmente solo por las siguentes paginas.
		Rule(LinkExtractor(deny = (url_visitadas), restrict_xpaths = ('//div[@class="unified pagination js_pageLinks"]/a'))),

		#restrict_xpaths le restringe moverse verticalmente solo por los item de la pagina actual.
		Rule(LinkExtractor( deny = (url_visitadas), restrict_xpaths = ('//div[@class="wQjYiB7z"]/span/a')),

		#Una vez que consigue las url llama mediante callback a la funcion 'parse_item' para procesar y extraer los datos.
							callback = 'parse_item', follow = False)
	)

	def parse_item(self, response):
		"""Recibe una pagina y extrae los datos para luego guardarlos en la base de datos."""

		item = TripadvisorItem()

		#Extrayendo informacion.
		direccion_url = response.url
		item['nombre'] = response.xpath('normalize-space(//h1[@class="_3a1XQ88S"])').extract_first()
		item['url']  = response.url
		item['ciudad'] = response.xpath('normalize-space(//ul[@class="breadcrumbs"]/li[position()=4]/a/span/text())').extract_first()
		item['direccion'] = response.xpath('normalize-space(//div[@class="bk7Uv0cc"]/div[position()=3]/span/span/a/text())').extract_first()
		item['num_valoracion'] = response.xpath('normalize-space(//span[@class="_3Wub8auF"])').extract_first()
		item['valoracion'] = response.xpath('normalize-space(//span[@class="r2Cf69qf"])').extract_first()
		item['telefono'] = response.xpath('normalize-space(//div[@class="bk7Uv0cc"]/div[position()=3]/span[position()=2]/span/span[position()=2]/a/text())').extract_first()
		item['url_mapa'] = map_utils.obtener_url_mapa(item['nombre'])

		try:
			insertar_datos("restaurant_visitados",direccion_url)
			db_utils.insertar_restaurant(db,item)
			print("Datos insertados correctamente.")
		except:
			print("No se han insertado.")
		yield item
