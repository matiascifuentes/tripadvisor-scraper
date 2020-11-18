# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

def obtener_url_mapa(titulo_servicio):
	
	options = Options()
	options.add_argument('--headless')

	driver = webdriver.Firefox(options=options)
	url = 'https://www.google.cl/maps'
	driver.get(url)

	inputElement = driver.find_element_by_id('searchboxinput')
	inputElement.send_keys(titulo_servicio)
	inputElement.send_keys(Keys.ENTER)

	time.sleep(4)

	current_url = driver.current_url
	print(current_url)
	driver.close()

	return current_url