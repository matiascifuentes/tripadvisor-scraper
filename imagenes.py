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
		try:
			url = obtenerUrlImagenHotel(driver,hotel)
			descargarImagen(url, string_utils.extraer_cod_hotel_url(hotel), "images/hotel")
			print("Descargada")
		except:
			print("No se ha descargado")

	try:
		driver.quit()
	except:
		print("Ha ocurrido un error al cerrar navegador")

def descargarImagenesRestaurantes(restaurantes):
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Firefox(options=options)

	for restaurant in restaurantes:
		try:
			print("Restaurant: " + restaurant)
			url = obtenerUrlImagenRestaurant(driver,restaurant)
			descargarImagen(url, string_utils.extraer_cod_restaurant_url(restaurant), "images/restaurant")
			print("Descargada")
		except:
			print("No se ha descargado")

	try:
		driver.quit()
	except:
		print("Ha ocurrido un error al cerrar navegador")

def descargarImagenesAtracciones(atracciones):
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Firefox(options=options)

	for atraccion in atracciones:
		try:
			print("Atraccion: " + atraccion)
			url = obtenerUrlImagenAtraccion(driver,atraccion)
			descargarImagen(url, string_utils.extraer_cod_atraccion_url(atraccion), "images/atraccion")
			print("Descargada")
		except:
			print("No se ha descargado")
			
	try:
		driver.quit()
	except:
		print("Ha ocurrido un error al cerrar navegador")

def obtenerUrlImagenHotel(driver,urlHotel):
	driver.get(urlHotel)
	time.sleep(1)
	
	divImagen = driver.find_element_by_class_name("_29cJjU62")
	driver.execute_script("arguments[0].click();", divImagen)

	nuevoHtml = driver.page_source
	soup = BeautifulSoup(nuevoHtml, "lxml")

	imagen = soup.find('img',{'class':'_1a4WY7aS'})
	urlImagen = imagen['src']
	return urlImagen

def obtenerUrlImagenRestaurant(driver,urlRestaurant):
	req = requests.get(urlRestaurant)
	time.sleep(1)

	soup = BeautifulSoup(req.text, "lxml")
	divPhoto = soup.findAll("div", {"class": "large_photo_wrapper"})
	imagen = divPhoto[0].findAll("img", {"class": "basicImg"})
	urlImagen = imagen[0]["data-lazyurl"]
	return urlImagen

def obtenerUrlImagenAtraccion(driver,urlAtraccion):
	driver.get(urlAtraccion)
	time.sleep(3)

	divImagen = driver.find_element_by_class_name("_2n0JSv4h")
	driver.execute_script("arguments[0].click();", divImagen)

	nuevoHtml = driver.page_source
	soup = BeautifulSoup(nuevoHtml, "lxml")

	imagen = soup.find('img',{'class':'_1a4WY7aS'})
	urlAtraccion = imagen['src']
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
time.sleep(30)
descargarImagenesRestaurantes(restaurantes)
time.sleep(30)
descargarImagenesAtracciones(atracciones)