import numpy as np
import math
from nodo import Nodo

class Hash:
    __tam = None
    __arre = None
    __nodo = None

    def __init__(self, tam):
        self.__nodo = Nodo()
        tam = self.primo(math.floor(tam/0.70))
        self.__tam = tam
        self.__arre = np.empty(tam, dtype = Nodo)

    def primo(self,num):
        band = False
        while not band:
            band = True
            i = 2
            while i < num and band:
                if num % i == 0:
                    band = False
                i+=1
            num += 1
        return num-1

    def lleno(self):
        return range(self.__arre) != self.__tam

    def getI(self, clave):
        x = [int(a) for a in str(clave)]
        i = len(x)-1
        val = []

        if len(x)%2 != 0:
            x.insert(0,0)
            i+=1
        while i >= 0:
            num = int(str(x[i-1])+str(x[i]))
            val.append(num)
            i-=2

        num = 0
        for i in range(len(val)):
            num += val[i]

        indice = num % self.__tam
        return indice


    def insertar(self, clave):
        indice = self.getI(clave)
        if self.__arre[indice] == None:
            self.__arre[indice] = Nodo()
        if self.__arre[indice].getItem() == None:
            self.__arre[indice].setItem(clave)
        else:
            aux1 = self.__arre[indice]
            aux = self.__arre[indice].getSig()
            bol = True
            while aux != None and bol:
                if aux.getItem() == clave:
                    aux = None
                    bol = False
                aux1 = aux
                aux = aux.getSig()    
            if bol:
                actual = Nodo()
                actual.setItem(clave)
                aux1.setSig(actual)

    def buscar(self, clave):
        indice = self.getI(clave)
        if self.__arre[indice].getItem() == clave:
            return indice
        else:
            aux1 = self.__arre[indice]
            aux = self.__arre[indice].getSig()
            bol = True
            i = 1
            while bol:
                if aux.getItem() == clave:
                    bol = False
                else:
                    aux = aux.getSig()
                    i += 1
            if not bol:
                return "El indice es:" + str(indice) + " y la posicion hacia dentro es:" + str(i)
            else:
                return "\nNo se encontro el elemento"