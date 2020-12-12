# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import file_utils
import string_utils

def descargarImagen(url,nombre):
	pass

def descargarImagenesHoteles(hoteles):
	for url in hoteles:
		print(url)
		descargarImagen(url, string_utils.extraer_cod_hotel_url(url))

def descargarImagenesRestaurantes(restaurantes):
	for url in restaurantes:
		print(url)
		descargarImagen(url, string_utils.extraer_cod_restaurant_url(url))

def descargarImagenesAtracciones(atracciones):
	for url in atracciones:
		print(url)
		descargarImagen(url, string_utils.extraer_cod_atraccion_url(url))


file = open("hoteles_visitados.txt", "a+") 
file.close()

file = open("restaurant_visitados.txt", "a+") 
file.close()

file = open("atracciones_visitados.txt", "a+") 
file.close()

hoteles = file_utils.leer_datos("hoteles_visitados") 
restaurantes = file_utils.leer_datos("restaurant_visitados")
atracciones = file_utils.leer_datos("atracciones_visitados")

descargarImagenesHoteles(hoteles)
descargarImagenesRestaurantes(restaurantes)
descargarImagenesAtracciones(atracciones)
