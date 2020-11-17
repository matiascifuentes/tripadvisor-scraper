# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

import scrapy   
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import file_utils

class TripadvisorItem(scrapy.Item):
	nombre = scrapy.Field()
	url = scrapy.Field()
	ciudad = scrapy.Field()
	direccion = scrapy.Field()
	num_valoracion = scrapy.Field()
	valoracion = scrapy.Field()
	telefono = scrapy.Field()