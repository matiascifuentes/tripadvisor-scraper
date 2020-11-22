# -*- coding: utf-8 -*-
__author__ = "Matias Cifuentes Lara"

import psycopg2

def crear_conexion():
	return psycopg2.connect(
				database="SISTEMA_TURISTICO", 
				user="postgres", 
				password="postgres", 
				host="127.0.0.1", 
				port="5432")

def insertar_hotel(db,item):
	sentencia = valores = "INSERT INTO hotel(NOMBRE,URL,DESCRIPCION,CIUDAD,DIRECCION,NUM_VALORACION,VALORACION,URL_MAPA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
	datos = (item['nombre'],item['url'],,item['descripcion'],item['ciudad'],item['direccion'],item['num_valoracion'],item['valoracion'],item['url_mapa'])

	cursor = db.cursor()
	cursor.execute(sentencia,datos)
	db.commit()