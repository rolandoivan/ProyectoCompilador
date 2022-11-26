from codigoIntermedio import *

class Memoria():
    def __init__(self):
        # Tabla de funciones
        self.tbFun = {}

        # Tabla de constantes
        self.tbConst = {}
        self.tbConstCont = 1200

        # Tabla de variables globales
        self.tbVar = {}
        self.tbVarCont = 5000
        self.tbVarMax = 0

        # Tabla de variables locales
        self.tbVarFun = {}
        self.tbVarFunCont = 8000
        self.tbVarFunMax = 0

        # Tabla de temporales enteros
        self.tbTempI = {}
        self.tbTempICont = 13000

        # Tabla de temporales booleanos
        self.tbTempB = {}
        self.tbTempBCont = 14000

        # Tabla de temporales punteros
        self.tbTempP = {}
        self.tbTempPCont = 21000

    # LLenar tablas
    def addtbFun(self, nombre, inicio, fin):
        self.tbFun[nombre] = [inicio, fin]

    def addtbConst(self, valor):
        self.tbConst[valor] = self.tbConstCont
        self.tbConstCont += 1

    def addtbVar(self, nombre, tipo, tamaño1, tamaño2):
        self.tbVar[nombre] = [self.tbVarCont, tipo, tamaño1, tamaño2]
        self.tbVarCont += (tamaño1)*(tamaño2)

    def addtbVarFun(self, nombre, tipo, tamaño1, tamaño2):
        self.tbVarFun[nombre] = [self.tbVarFunCont, tipo, tamaño1, tamaño2]
        self.tbVarFunCont += (tamaño1)*(tamaño2)

    def addtbTempI(self, nombre):
        self.tbTempI[nombre] = self.tbTempICont
        self.tbTempICont += 1

    def addtbTempB(self, nombre):
        self.tbTempB[nombre] = self.tbTempBCont
        self.tbTempBCont += 1

    def addtbTempP(self, nombre):
        self.tbTempP[nombre] = self.tbTempPCont
        self.tbTempPCont += 1

    # Reiniciar Temporales
    def reiniciarCont(self):
        if self.tbVarFunMax < self.tbVarFunCont-8000:
            self.tbVarFunMax = self.tbVarFunCont-8000
        if self.tbVarMax < self.tbVarCont-5000:
            self.tbVarMax = self.tbVarCont-5000
        self.tbVarFunCont = 8000
        self.tbTempICont = 13000
        self.tbTempBCont = 14000
        self.tbTempPCont = 21000
        
        # Reiniciar diccionarios de temporales

    def reiniciarContTbVarFun(self):
        self.tbVarFunCont = 8000

    # Obtener Contadores
    def getContTbTempI(self):
        return self.tbTempICont

    def getContTbTempB(self):
        return self.tbTempBCont

    def getContTbTempP(self):
        return self.tbTempPCont

    def getContTbVarFun(self):
        return self.tbVarFunCont

    def getContTbVar(self):
        return self.tbVarCont

    def getVarFunMax(self):
        return self.tbVarFunMax

    def getVarMax(self):
        return self.tbVarMax