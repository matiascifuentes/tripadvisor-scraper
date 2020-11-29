# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

def extraer_cod_url(url):
	codigo = url[40:]
	codigo = codigo.split("-Reviews")
	return codigo[0]
