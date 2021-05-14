import requests
from random import seed
from random import randint
from datetime import datetime
import json
seed(2)

NUM_TRANSACCIONES = 10000
id_usuario = 19	#Usuario1

url_sesion = "http://127.0.0.1:5000/api/v1/sesions"
url_pages = "http://127.0.0.1:5000/api/v1/pages"

hoteles = ["g488179-d13928020","g488179-d4053402","g488179-d7913180"]
restaurantes = ["g488179-d1021036","g488179-d10494591","g488179-d1100153","g488179-d12158906","g488179-d12731965","g488179-d12799377","g488179-d10130677","g488179-d10275867","g488179-d10364056","g488179-d10456043"]
atracciones = ["g488179-d10584402","g488179-d12689922","g488179-d13281063","g488179-d15020467","g488179-d6925438","g488179-d7351765","g488179-d8293400","g488179-d7289728","g488179-d6925442","g488179-d10509682"]

servicios = hoteles + restaurantes + atracciones
len_servicios = len(servicios) - 1

ok = 0
id_sesion = None
for i in range(0,NUM_TRANSACCIONES):

	if(i%10 == 0):
		now = datetime.now()
		fecha = now.strftime("%d-%m-%Y %H:%M:%S")
		datos_sesion = {
			"id_usuario": id_usuario,
			"fecha": fecha
		}
		sesion = requests.request("POST", url_sesion, headers={}, json=datos_sesion)
		if sesion.status_code == 200:
			id_sesion = json.loads(sesion.text)['success']

	if(id_sesion):
		pag_visitada = {
			"id_sesion": id_sesion,
			"id_servicio": servicios[randint(0,len_servicios)]
		}
		response = requests.request("POST", url_pages, headers={}, json=pag_visitada)
		if response.status_code == 200:
			ok = ok + 1

print("Se han insertado " + str(ok) + " listas")
