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
