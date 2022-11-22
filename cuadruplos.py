class cuadruplo:
    _counter = 0
    def __init__(self, operador, operando1, operando2, resultado):
        cuadruplo._counter += 1
        self.operador = operador
        self.operando1 = operando1
        self.operando2 = operando2
        self.resultado = resultado

    def cuad4(self):
        return str(self.operador) + "\t""\t" + str(self.operando1) + "\t""\t" + str(self.operando2) + "\t""\t" + str(self.resultado)

    def cuad3(self):
        return str(self.operador) + "\t" + str(self.operando1) + "\t" + str(self.resultado)

    def cuad2(self):
        return str(self.operador) + "\t" + str(self.resultado)

    def cuad1(self):
        return str(self.operador)

    def cuadEnd(self):
        # Reiniciamos temporales
        #print(tablaMemoria.tbTempI)
        #print(tablaMemoria.tbTempB)
        #print(tablaMemoria.tbTempP)
        return str(self.operador) + "\t" + str(self.resultado)

    def cuadExp(self):
        return str(self.operador) + "\t""\t" + str(self.operando1) + "\t""\t" + str(self.operando2) + "\t""\t" + str(self.resultado)
    
    def getCont(cuadruplo):
        return cuadruplo._counter

class Pilas():
    def __init__(self):
        self.Poper = []
        self.PilaO = []
        self.Ptipos = []
        self.Pmigas = []
        self.Psaltos = []

    def addPoper(self, operador):
        self.Poper.append(operador)

    def addPilaO(self, operando):
        self.PilaO.append(operando)

    def addPtipos(self, tipo):
        self.Ptipos.append(tipo)

    def addPmigas(self, migas):
        self.Pmigas.append(migas)

    def addPsaltos(self, saltos):
        self.Psaltos.append(saltos)

    def addStartPsaltos(self, n, saltos):
        self.Psaltos.insert(n,saltos)

    def addPilaSaltos(self, saltos):
        self.PilaSaltos.append(saltos)

    def delPoper(self):
        return self.Poper.pop()

    def delPilaO(self, n):
        return self.PilaO.pop(n)

    def delPtipos(self, n):
        return self.Ptipos.pop(n)

    def delPmigas(self, n):
        return self.Pmigas.pop(n)

    def delPsaltos(self,n):
        return self.Psaltos.pop(n)

    def delPilaSaltos(self):
        return self.PilaSaltos.pop()

    def lenPilaO(self):
        return len(self.PilaO)

    def lenPmigas(self):
        return len(self.Pmigas)