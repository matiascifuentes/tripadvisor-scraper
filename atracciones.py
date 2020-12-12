# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

import scrapy   
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import file_utils
import map_utils
import db_utils
import string_utils


db = db_utils.crear_conexion()


class TripadvisorItem(scrapy.Item):
	cod_atraccion = scrapy.Field()
	nombre = scrapy.Field()
	url = scrapy.Field()
	descripcion = scrapy.Field()
	ciudad = scrapy.Field()
	direccion = scrapy.Field()
	num_valoracion = scrapy.Field()
	valoracion = scrapy.Field()
	url_mapa = scrapy.Field()

class TripadvisorSpider(CrawlSpider):

	custom_settings = {
        "CLOSESPIDER_ITEMCOUNT":5,   #Cantidad de elementos a buscar. Comienza a contar desde el 0.
        "CONCURRENT_REQUESTS":1,   #Cantidad de url que puede visitar a la vez.
        "CONCURRENT_ITEMS":1,   #Cantidad de elementos que puede visitar a la vez.
    }
	name = 'Tripadvisor'
	allowed_domain = ['www.tripadvisor.cl']

	busca = 'https://www.tripadvisor.cl/Attractions-g2615220-Activities-oa30-Maule_Region.html' 
	start_urls = [busca]

	file = open("atracciones_visitados.txt", "a+") 
	file.close()

	url_visitadas = file_utils.leer_datos("atracciones_visitados") 

	rules = (

		#deny no permite que visite las url que ya ha procesado. restrict_xpaths le restringe moverse horizontalmente solo por las siguentes paginas.
		Rule(LinkExtractor(deny = (url_visitadas), restrict_xpaths = ('//div[@class="ui_pagination is-centered"]/a'))),

		#restrict_xpaths le restringe moverse verticalmente solo por los item de la pagina actual.
		Rule(LinkExtractor( deny = (url_visitadas), restrict_xpaths = ('//div[@class="_6sUF3jUd"]/a')),

							callback = 'parse_item', follow = False)
	)

	def parse_item(self, response):
		"""Recibe una pagina y extrae los datos para luego guardarlos en la base de datos."""

		item = TripadvisorItem()

		#Extrayendo informacion.
		direccion_url = response.url
		item['cod_atraccion'] = string_utils.extraer_cod_atraccion_url(direccion_url)
		item['nombre'] = response.xpath('normalize-space(//h1[@id="HEADING"])').extract_first()
		item['url']  = response.url
		item['descripcion'] = None
		item['ciudad'] = response.xpath('normalize-space(//ul[@class="breadcrumbs"]/li[position()=4]/a/span/text())').extract_first()
		item['direccion'] = response.xpath('normalize-space(//div[@class="LjCWTZdN"]/span[position()=2])').extract_first()
		item['num_valoracion'] = response.xpath('normalize-space(//span[@class="_3WF_jKL7 _1uXQPaAr"])').extract_first()
		item['valoracion'] = None
		item['url_mapa'] = map_utils.obtener_url_mapa(item['nombre'])

		try:
			file_utils.insertar_datos("atracciones_visitados",direccion_url)
			print("Datos insertados correctamente.")
		except:
			print("No se han insertado.")
		yield item