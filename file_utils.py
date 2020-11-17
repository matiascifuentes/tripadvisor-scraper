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

