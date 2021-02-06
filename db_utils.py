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
	datos_servicio = (item['cod_hotel'],item['nombre'],item['url'],item['direccion'],item['ciudad'],item['descripcion'],item['valoracion'],item['num_valoracion'],item['url_mapa'])
	insert_servicio(db,datos_servicio)

	insert_hotel = "INSERT INTO hotel(id_servicio) VALUES (%s);"
	datos_hotel = (item['cod_hotel'])
	cursor = db.cursor()
	cursor.execute(insert_hotel,datos_hotel)
	db.commit()

def insertar_restaurant(db,item):
	datos_servicio = (item['cod_restaurant'],item['nombre'],item['url'],item['direccion'],item['ciudad'],item['descripcion'],item['valoracion'],item['num_valoracion'],item['url_mapa'])
	insert_servicio(db,datos_servicio)

	insert_restaurant = "INSERT INTO restaurant(id_servicio) VALUES (%s);"
	datos_restaurant = (item['cod_restaurant'])
	cursor = db.cursor()
	cursor.execute(insert_restaurant,datos_restaurant)
	db.commit()

def insertar_atraccion(db,item):
	datos_servicio = (item['cod_atraccion'],item['nombre'],item['url'],item['direccion'],item['ciudad'],item['descripcion'],item['valoracion'],item['num_valoracion'],item['url_mapa'])
	insert_servicio(db,datos_servicio)

	insert_atraccion = "INSERT INTO atraccion(id_servicio) VALUES (%s);"
	datos_atraccion = (item['cod_atraccion'])
	cursor = db.cursor()
	cursor.execute(insert_atraccion,datos_atraccion)
	db.commit()