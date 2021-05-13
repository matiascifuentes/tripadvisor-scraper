import requests
seed(1)

NUM_TRANSACCIONES = 10000
id_usuario = 19	#Usuario1

url = "http://127.0.0.1:5000/api/v1/lists"

hoteles = ["g488179-d13928020","g488179-d4053402","g488179-d7913180"]
restaurantes = ["g488179-d1021036","g488179-d10494591","g488179-d1100153","g488179-d12158906","g488179-d12731965","g488179-d12799377","g488179-d10130677","g488179-d10275867","g488179-d10364056","g488179-d10456043"]
atracciones = ["g488179-d10584402","g488179-d12689922","g488179-d13281063","g488179-d15020467","g488179-d6925438","g488179-d7351765","g488179-d8293400","g488179-d7289728","g488179-d6925442","g488179-d10509682"]

len_restaurantes = len(restaurantes) 
len_atracciones = len(atracciones)

ok = 0
for i in range(0,NUM_TRANSACCIONES):
	servicios = []
	#Agregar restaurantes
	for j in range(0,randint(0,5)):
		servicios.append({"id_servicio":restaurantes[randint(0,len_restaurantes)]})
	#Agregar atracciones
	for k in range(0,randint(0,5)):
		servicios.append({"id_servicio":atracciones[randint(0,len_atracciones)]})

	datos = {
		"id_usuario": id_usuario,
		"servicios": servicios
	}

	response = requests.request("POST", url, headers={}, json=datos)
	if response.status_code == 201:
		ok = ok + 1

print("Se han insertado " + ok + "listas")
