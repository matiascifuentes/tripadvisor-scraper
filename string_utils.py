# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

def extraer_cod_url(url,pos_inicial):
	codigo = url[pos_inicial:]
	codigo = codigo.split("-Reviews")
	return codigo[0]

def extraer_cod_hotel_url(url):
	return extraer_cod_url(url,40)

def extraer_cod_restaurant_url(url):
	return extraer_cod_url(url,45)
