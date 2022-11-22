class Cuadruplos:
    def __init__(self):
        self.txt = ""
        self.cuadruplos = []
        self._counter = 0

    def cuad4(self, operador, operando1, operando2, resultado):
        self._counter += 1
        self.cuadruplos.append(str(operador) + "\t" + str(operando1) + "\t" + str(operando2) + "\t" + str(resultado))

    def cuad3(self, operador, operando1, resultado):
        self._counter += 1
        self.cuadruplos.append(str(operador) + "\t" + str(operando1) + "\t"  + str(resultado) + "\t")

    def getCont(cuadruplo):
        return cuadruplo._counter