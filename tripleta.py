#Fichero tripleta.py para gestión de la clase tripleta
import foto
import slide

class tripleta:
    def __init__ (self, identificador):
        self.id = identificador
        self.listaSlide = []

    def anyadirSlide(self, idSlide):
        self.listaSlide.append(idSlide)

    def valorTransicion(self, tags1, tags2):
        dif1 = 0        #Valores diferentes en tag1
        eq = 0          #Valores diferentes
        iguales = False
        while len(tags1) > 0:    
            aux = tags1.pop()
            #Si hay en tags2 un tag igual a aux lo indica en iguales
            for x in range(len(tags2)):
                if (tags2[x] == aux):
                    tags2.pop([x])
                    iguales = True
                    break
            #Si ha habido algún igual incrementa eq, si no incrementa dif
            if (iguales):
                eq = eq + 1
            else:
                dif1 = dif1 + 1
            iguales = False
        return min(dif1, len(tags2), eq)

    def permutas(self):


    def tagsPrimero(self):
        return self.listaSlide[2]
    
    def tagsUltimo(self):
        return self.listaSlide[0]

    def dameSlides(self):
    	return self.listaSlide

    