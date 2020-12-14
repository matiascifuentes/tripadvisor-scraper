# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from pathlib import Path
import time
import file_utils
import string_utils

def descargarImagen(url,nombre,path):
	filepath = os.path.join(path, nombre+".jpg")
	if not os.path.exists(filepath):
		if not os.path.exists(path):
			os.makedirs(path)
	urllib.request.urlretrieve(url,filepath)

def descargarImagenesHoteles(hoteles):
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Firefox(options=options)

	for hotel in hoteles:
		print("Hotel: " + hotel)
		url = obtenerUrlImagenHotel(driver,hotel)
		descargarImagen(url, string_utils.extraer_cod_hotel_url(hotel), "img/hotel")

	try:
		driver.quit()
	except:
		print("Ha ocurrido un error al cerrar navegador")

def descargarImagenesRestaurantes(restaurantes):
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Firefox(options=options)

	for restaurant in restaurantes:
		url = obtenerUrlImagenRestaurant(driver,restaurant)
		descargarImagen(url, string_utils.extraer_cod_restaurant_url(url), "img/restaurant")

	try:
		driver.quit()
	except:
		print("Ha ocurrido un error al cerrar navegador")

def descargarImagenesAtracciones(atracciones):
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Firefox(options=options)

	for atraccion in atracciones:
		url = obtenerUrlImagenAtraccion(driver,atraccion)
		descargarImagen(url, string_utils.extraer_cod_atraccion_url(url), "img/atraccion")

	try:
		driver.quit()
	except:
		print("Ha ocurrido un error al cerrar navegador")

def obtenerUrlImagenHotel(driver,urlHotel):

	driver.get(urlHotel)

	divImagen = driver.find_element_by_class_name("_29cJjU62")
	driver.execute_script("arguments[0].click();", divImagen)

	nuevoHtml = driver.page_source
	soup = BeautifulSoup(nuevoHtml, "lxml")

	imagen = soup.find('img',{'class':'_1a4WY7aS'})
	urlImagen = imagen['src']
	time.sleep(1)
	return urlImagen

def obtenerUrlImagenRestaurant(driver,urlRestaurant):
	return urlRestaurant

def obtenerUrlImagenAtraccion(driver,urlAtraccion):
	return urlAtraccion


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
#time.sleep(60)
#descargarImagenesRestaurantes(restaurantes)
#time.sleep(60)
#descargarImagenesAtracciones(atracciones)
