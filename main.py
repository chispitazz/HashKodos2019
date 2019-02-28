from tripleta import tripleta
from foto import foto
from slide import slide

numero_fotos = 0
slides = []
lista_tripletas = []


def listas(a,b):
	lista_final=[]
	for i in a:
		if (i not in lista_final) and (i in b):
			lista_final.append(i)
	return lista_final

def listass(a,b):
	lista_final=[]
	for i in a:
		if (i not in lista_final) and (i not in b):
			lista_final.append(i)
	return lista_final

def listasss(a,b):
	lista_final=[]
	for i in b:
		if (i not in lista_final) and (i not in a):
			lista_final.append(i)
	return lista_final


def comunes(tags1, tags2):
	lista_res=listas(tags1, tags2)
	num=len(lista_res)
	return num


def enSiperonoSimas1():
	lista_res=listass(tags1, tags2)
	num=len(lista_res)
	return num


def enSimas1peronoSi():
	lista_res=listasss(tags1, tags2)
	num=len(lista_res)
	return num


def transiciones(tags1, tags2):
	numComun = comunes(tags1, tags2)
	num2 = enSiperonoSimas1(tags1, tags2)
	num3 = enSimas1peronoSi(tags1, tags2)
	numFinal=min(numComun, num2, num3)
	return numFinal



def sacarTransicion(trip1, trip2):
	list1=trip1.dameLista()
	list2=trip2.dameLista()
	slide1=list1[3]
	slide3=list2[1]
	gay=slide1.dametags()
	gay2=slide3.dametags()
	return transiciones(gay, gay2)


def optimizarUna(tripleta, listaTripletas):
	auxMax=-1
	auxTripleta = 0
	i=0
	for i in listaTripletas:
		maxi=sacarTransicion(tripleta,i)
		if maxi>auxMax:
			auxMax=maxi
			auxTripleta=i.dameID()

	return auxTripleta

def optimizar(listaTripletas):
	listaAux=[]
	listaAux.append(listaTripletas[0])
	count=0
	for i in listaTripletas:
		tripAux=optimizarUna(i, listaTripletas[count+1:100])
		listaAux[count]=tripAux
		count=count+1
	return listaAux



def dameOrden(listaTripletas):
	lista_slides=[]
	lista=optimizar(listaTripletas)
	for i in lista:
		lista_slides=lista_slides+i.dameSlides()
	return lista_slides


def extraer_datos(f):
	numero_fotos = int(f.readline())
	salida = open ('salida.txt','w')
	numero_fotos_str = str(numero_fotos-1)+'\n'
	salida.write(numero_fotos_str)
	aux = ""
	contador_tripletas = 0
	verticales = 0
	contador=0
	lista_slides=[]
	contar_slides = 0
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
			aux2= id_foto
			if verticales == 1:
				photo1 = foto(id_foto,nro_tags,resto,orientacion)
			if verticales == 2:
				verticales = 0
				photo2 = foto(id_foto,nro_tags,resto,orientacion)

				aux += ' '+str(id_foto)
				salida.write(aux+'\n')
		else:
			slide_a_meter = slide (contador, id_foto, -1, resto)
			lista_slides.append(slide_a_meter)


			slides.append(1)
			slides.append(id_foto)
			salida.write(str(id_foto)+'\n')
		# Ir añadiendo instancias de fotos.

		contar_slides+=1
		if contar_slides == 3: 
			contar_slides = 0
			tripletaAA = tripleta(contador_tripletas)
			contador_tripletas+=1
			for slideA in lista_slides:	
				tripletaAA.anyadirSlide(slideA)
			lista_tripletas.append(tripletaAA)

	lista_terminada=dameOrden(lista_tripletas)
	for i in lista_terminada:
		printf(dameID(i))



	f.close()
	salida.close()

f = open("a_example.txt")
extraer_datos(f)


