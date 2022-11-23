class Cuadruplos:
    def __init__(self):
        self.txt = ""
        self.cuadruplos = []
        self._counter = 0

    def cuad4(self, operador, operando1, operando2, resultado):
        self._counter += 1
        self.cuadruplos.append([operador , "\t" , operando1 , "\t" , operando2 , "\t" , resultado])

    def cuad3(self, operador, operando1, resultado):
        self._counter += 1
        self.cuadruplos.append([operador , "\t" , operando1 ,  "\t" , resultado])
    def cuad2(self, operador, resultado):
        self._counter += 1
        self.cuadruplos.append([operador ,  "\t" , resultado])
    def getCont(cuadruplo):
        return cuadruplo._counter