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

def insertar_servicio(db,datos):
	sentencia = "INSERT INTO servicio(id_servicio,nombre,url,direccion,ciudad,descripcion,valoracion,num_valoracion,url_mapa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	cursor = db.cursor()
	cursor.execute(sentencia,datos)
	db.commit()

def insertar_hotel(db,item):
	sentencia = "INSERT INTO hotel(COD_HOTEL,NOMBRE,URL,DESCRIPCION,CIUDAD,DIRECCION,NUM_VALORACION,VALORACION,URL_MAPA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	datos = (item['cod_hotel'],item['nombre'],item['url'],item['descripcion'],item['ciudad'],item['direccion'],item['num_valoracion'],item['valoracion'],item['url_mapa'])

	cursor = db.cursor()
	cursor.execute(sentencia,datos)
	db.commit()

def insertar_restaurant(db,item):
	sentencia = "INSERT INTO restaurant(COD_RESTAURANT,NOMBRE,URL,CIUDAD,DIRECCION,NUM_VALORACION,VALORACION,TELEFONO,URL_MAPA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
	datos = (item['cod_restaurant'],item['nombre'],item['url'],item['ciudad'],item['direccion'],item['num_valoracion'],item['valoracion'],item['telefono'],item['url_mapa'])

	cursor = db.cursor()
	cursor.execute(sentencia,datos)
	db.commit()