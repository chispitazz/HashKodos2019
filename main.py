
numero_fotos = 0
def extraer_datos(f):
	numero_fotos = int(f.readline())
	salida = open ('salida.txt','w')
	numero_fotos_str = str(numero_fotos-1)+'\n'
	salida.write(numero_fotos_str)
	aux = ""
	verticales = 0
	for id_foto in range(0,numero_fotos):
		lista = f.readline().split()
		orientacion = lista[0]
		nro_tags = lista[1]
		resto = lista[2:]
		print(orientacion)
		print(nro_tags)
		print(resto)

		if orientacion == 'V':
			verticales=verticales+1
			if verticales == 1:
				aux += str(id_foto)
			if verticales == 2:
				verticales = 0
				aux += ' '+str(id_foto)
				salida.write(aux+'\n')
		else:
			salida.write(str(id_foto)+'\n')
		# Ir añadiendo instancias de fotos.
	f.close()
	salida.close()
f = open("a_example.txt")
extraer_datos(f)

