class Nodo:
    __item = None
    __sig = None

    def __init__(self):
        self.__sig = None
        self.__item = None
    
    def setItem(self, item):
        self.__item = item

    def setSig(self, sig):
        self.__sig = sig
    
    def getItem(self):
        return self.__item

    def getSig(self):
        return self.__sig
