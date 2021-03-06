def leer_datos(nombre_archivo):
	"""Lee un archivo txt y devuelve un array donde cada posicion es una fila del archivo.
	Argumentos:	
	nombre_archivo: String. No debe tener la extension. 
	"""

	array = []
	archivo = open(nombre_archivo + '.txt','r')
	linea = archivo.readline()
	while linea != '':
		cadena = linea.strip('\n')
		array.append(cadena)
		linea = archivo.readline()
	archivo.close()
	return array

def insertar_datos(nombre_archivo,cadena):
	"""Inserta un string en una fila de un archivo txt.
	Argumentos:
	nombre_archivo: String. No debe tener la extension.
	cadena: String a escribir en el archivo.
	"""

	archivo = open(nombre_archivo + '.txt', "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()
	archivo.seek(final_de_archivo)
	archivo.write(cadena)
	archivo.write('\n')
	archivo.close()