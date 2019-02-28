

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
	listaAux=[listaTripletas[0]]
	count=1
	for i in  listaTripletas:
		tripAux=optimizarUna(i, listaTripletas[i+1:100])
		listaAux[count]=tripAux
		count=count+1
	return listaAux
	
