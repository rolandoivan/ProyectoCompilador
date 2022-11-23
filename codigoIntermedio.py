from memoria import *
from cuadruplos import *
import sys

# variables globales

tablaMemoria = Memoria()
listaCuadruplos = Cuadruplos()
Poper = []
PilaO = []
Ptipos = []
Pmigas = []
Psaltos = []

flag = 0
flagtbVar = 0

tempI = 0
tempP = 0
tempB = 0

# Funciones para el manejo Temporales

def reiniciarTemp():
    global temp
    global tempP
    global tempB
    temp = 0
    tempP = 0
    tempB = 0

def incrementarTempI():
    global tempI
    tempI = tempI + 1
    return tempI

def incrementarTempP():
    global tempP
    tempP = tempP + 1
    return tempP

def incrementarTempB():
    global tempB
    tempB = tempB + 1
    return tempB

parm = 0
def incrementarParam():
    global parm
    parm = parm + 1
    return parm

def reiniciarParam():
    global parm
    parm = 0

# Funciones para el manejo de direcciones Virtuales

def dirVirtual(var):
    if var in tablaMemoria.tbVarFun :
        return tablaMemoria.tbVarFun.get(var)[0]
    elif var in tablaMemoria.tbVar:
        return tablaMemoria.tbVar.get(var)[0]
    elif var in tablaMemoria.tbConst:
        return tablaMemoria.tbConst.get(var)
    return var


# ---------------------------------------------

class Nodo():
    pass

class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def traducir(self):
        pass

# ------------------ PROGRAM ------------------

class program(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        txt = ""
        variables = ""
        global flagtbVar

        # REGLA
        # CUADRUPLO DE INICIO
        listaCuadruplos.cuad3("Goto",'Main',0)
        Pmigas.append(listaCuadruplos.getCont())
        
        # DEF_VARS
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        flagtbVar = 1
        # FUNCIONS
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        flagtbVar = 0

        # REGLA
        # PILA DE SALTOS
        Psaltos.insert(0,listaCuadruplos.getCont())

        # BLOCK
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO DE FIN
        listaCuadruplos.cuad4("EndProc",0,0,0)

        #print(len(tablaMemoria.tbFun),"Funciones")
        print(len(tablaMemoria.tbConst),"Constantes")
        print(tablaMemoria.tbConst)
        print(tablaMemoria.getVarMax(),"Variables globales")
        print(tablaMemoria.tbVar)
        print(tablaMemoria.getVarFunMax(),"Variables locales")
        print(tablaMemoria.tbVarFun)
        print(len(tablaMemoria.tbTempI),"Temporales Int")
        print(tablaMemoria.tbTempI)
        print(len(tablaMemoria.tbTempB),"Temporales Bool")
        print(tablaMemoria.tbTempB)
        print(len(tablaMemoria.tbTempP),"Temporales Pointer")
        print(tablaMemoria.tbTempP)
        for key in tablaMemoria.tbConst:
            variables += str(tablaMemoria.tbConst[key])+" "+str(key)+"\n"
        # Escribir en archivo
        varFile = open("variables.txt","w")
        varFile.write(variables)
        varFile.close()


        # REGLA
        # VACIAR PILA DE SALTOS y PILA DE MIGAS
        aux = Pmigas.pop(0)
        for lista in listaCuadruplos.cuadruplos:
            for i in range(len(lista)):
                txt = txt + str(lista[i])
            if len(lista) == 5:
                txt += "\t" + str(Psaltos.pop(0))
            if lista[0] == 'GOSUB':
                txt += "\t" + str(tablaMemoria.tbFun.get(lista[2])[0]) + "\t" + str(tablaMemoria.tbFun.get(lista[2])[1])
            txt = txt + "\n"
        return txt

# -------------------- FUNCTIONS --------------------

class functions(Nodo):
    def __init__(self, son1, son2, son3, son4, son5):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
    
    def traducir(self):
        # TYPE_FUN
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # ID
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # MEMORIA TABLA DE FUNCIONES
        fun = PilaO.pop()
        inicio = listaCuadruplos.getCont()+1

        reiniciarParam()
        tablaMemoria.reiniciarContTbVarFun()

        # PARAM
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # BLOCK
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            self.son4.traducir()

        #print(tablaMemoria.tbVarFun)

        # REGLA
        # CUADRUPLO DE FIN DE FUNCION
        listaCuadruplos.cuad4("EndProc",0,0,0)
        
        #print(len(tablaMemoria.tbVarFun),"Variables locales")
        tablaMemoria.tbVarFun.clear()
        tablaMemoria.reiniciarCont()
        reiniciarTemp()

        # REGLA
        # MEMORIA TABLA DE FUNCIONES
        tablaMemoria.addtbFun(fun,inicio,listaCuadruplos.getCont())

        # FUNCIONS (RECURSIÓN)
        if type(self.son5) == type(tuple()):
            self.son5[0].traducir()
        else:
            self.son5.traducir()

class param1(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # TYPE_ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # ID
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # MEMORIA TABLA DE VARIABLES FUN
        var = PilaO.pop()
        tipo = Ptipos.pop()
        tablaMemoria.addtbVarFun(var, tipo,1,1)

        # PARAM (RECURSIÓN)
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

class param2(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # TYPE_ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # ID
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # MEMORIA TABLA DE VARIABLES FUN
        var = PilaO.pop()
        tipo = Ptipos.pop()
        tablaMemoria.addtbVarFun(var, tipo,1,1)
# ------------------ BLOCK ------------------
    
class block(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONTENT_BLOCK
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class content_block(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # STATEMENT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # CONTENT_BLOCK (RECURSIÓN)
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

# ---------------------------- STATMENT ----------------------------

class statment1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # DEF_VARS
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class statment2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # ASIGNMENT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class statment3(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONDITION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class statment4(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # WHILE_LOOP
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class statment5(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # FOR_LOOP
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class statment6(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        global flag
        
        # REGLA
        flag = 1

        # FUNCTION_CALL
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        flag = 0

class statment7(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # WRITE_FUNCTION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class statment8(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # RETURN EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        #REGLA
        # CUADRUPLO DE RETORNO CON EXPRESION
        listaCuadruplos.cuad4("Ret",dirVirtual(PilaO.pop()), 0, 22000)

class statment9(Nodo):
    pass

class statment10(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # READ_FUNCTION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

# --------------------------- DEF_VARS ---------------------------

class def_vars(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global flagtbVar
        # TYPE
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # VARS_N
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # DEF_VARS (RECURSIÓN)
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

class vars_n1(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # VARS_N (RECURSIÓN)
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

class vars_n2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # CUADRUPLO DE DECLARACION DE VARIABLE
        tipo = Ptipos.pop()
        for i in range(len(PilaO)):
            if flagtbVar == 0:
                tablaMemoria.addtbVar(PilaO.pop(0), tipo, 1, 1)
            else:
                tablaMemoria.addtbVarFun(PilaO.pop(0), tipo, 1, 1)

class vars_n3(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # CONST_INT
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        
        # REGLA
        # CUADRUPLO DE DECLARACION DE ARREGLO
        if flagtbVar == 0:
            tablaMemoria.addtbVar(PilaO.pop(0), Ptipos.pop(0), PilaO.pop()+1, 1)
        else:
            tablaMemoria.addtbVarFun(PilaO.pop(0), Ptipos.pop(0), PilaO.pop()+1, 1)

class vars_n4(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # CONST_INT
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # CONST_INT
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO DE DECLARACION DE MATRIZ
        if flagtbVar == 0:
            tablaMemoria.addtbVar(PilaO.pop(0), Ptipos.pop(0), PilaO.pop()+1, PilaO.pop()+1)
        else:
            tablaMemoria.addtbVarFun(PilaO.pop(0), Ptipos.pop(0), PilaO.pop()+1, PilaO.pop()+1)

# --------------------------- ASSIGNMENT ---------------------------

class assignment(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # VAR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # ASSIG
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # EXPRESSION
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO DE ASIGNACION
        listaCuadruplos.cuad4(Poper.pop(),dirVirtual(PilaO.pop()),0,dirVirtual(PilaO.pop()))

# --------------------------- CONDICION ---------------------------

class condition(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        #REGLA
        # CUADRUPLO DE GOTOF IF
        listaCuadruplos.cuad3("GotoF",PilaO.pop() ,0)
        Pmigas.append(listaCuadruplos.getCont())
        
        # BLOCK
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # PILA DE SALTO GOTF IF
        Psaltos.append(listaCuadruplos.getCont()+1)

        # CONDITION_ESLE (SI EXISTE)
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

class condition_else1(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):

        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # CUADRUPLO GOTOF ELIF
        listaCuadruplos.cuad3("GotoF",PilaO.pop() ,0)
        Pmigas.append(listaCuadruplos.getCont())

        # BLOCK
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # PILA DE SALTO GOTOF ELIF
        Psaltos.append(listaCuadruplos.getCont()+1)
        
        # CONDITION_ESLE (RECURSIÓN)
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

class condition_else2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        #REGLA
        # CUADRUPLO GOTO ELSE
        Psaltos.pop()
        listaCuadruplos.cuad3("Goto",0,0)
        Pmigas.append(listaCuadruplos.getCont())

        # REGLA
        # PILA DE SALTO GOTOF
        Psaltos.append(listaCuadruplos.getCont()+1)

        # BLOCK
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # PILA DE SALTO GOTO ELSE
        Psaltos.append(listaCuadruplos.getCont()+1)

# --------------------------- WHILE LOOP ---------------------------

class while_loop(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # REGLA
        # PILA DE SALTO GOTO WHILE
        Psaltos.append(listaCuadruplos.getCont())

        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # CUADRUPLO GOTOF WHILE
        listaCuadruplos.cuad3("GotoF",PilaO.pop() ,0)
        Pmigas.append(listaCuadruplos.getCont())

        # BLOCK
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # CUADRUPLO GOTO WHILE
        listaCuadruplos.cuad4("Goto",0,0,Psaltos.pop())
        
        # REGLA
        # PILA DE SALTO GOTOF WHILE
        Psaltos.append(listaCuadruplos.getCont()+1)



# --------------------------- DO WHILE ---------------------------

class do_while_loop(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2
        
    def traducir(self):

        # REGLA
        # PILA DE SALTO GOTO
        Psaltos.append(listaCuadruplos.getCont()+1)

        # BLOCK
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # EXPRESSION
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # CUADRUPLO GOTOV DO WHILE
        listaCuadruplos.cuad4("GotoV",dirVirtual(PilaO.pop()),0,Psaltos.pop())

# --------------------------- FOR LOOP ---------------------------

class for_loop(Nodo):
    def __init__(self, son1, son2, son3, son4):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def traducir(self):
        # FOR PARAM1
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # PILA DE SALTO GOTO
        Psaltos.append(listaCuadruplos.getCont())

        # FOR PARAM2
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # FOR PARAM3
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO GOTOF FOR
        listaCuadruplos.cuad3("GotoF", PilaO.pop() ,0)
        Pmigas.append(listaCuadruplos.getCont())

        # BLOCK
        if type(self.son4) == type(tuple()):
            self.son4[0].traducir()
        else:
            self.son4.traducir()

        # REGLA
        # CUADRUPLO GOTO FOR
        listaCuadruplos.cuad4("Goto",0,0,Psaltos.pop())
        
        # REGLA
        # PILA DE SALTO GOTOF
        Psaltos.append(listaCuadruplos.getCont()+1)

class for_param1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # ASIGNACION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class for_param2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class for_param3(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # ASIGNACION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

# --------------------------- FUNCTION CALL ---------------------------

class function_call(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global flag
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        
        # REGLA
        # CUADRUPLO ERA
        #tablaMemoria.reiniciarContTbVarFun()
        fun = PilaO.pop()
        listaCuadruplos.cuad4("ERA",0,0,fun)

        # FUN_PARAM
        tablaMemoria.reiniciarContTbVarFun()
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        tablaMemoria.reiniciarContTbVarFun()

        reiniciarParam()
        # REGLA
        # CUADRUPLO GOSUB
        print(tablaMemoria.tbVarFun)
        listaCuadruplos.cuad2("GOSUB",fun)

        # REGLA
        # CUADRUPLO ASIGNACION DE FUN A TEMP
        if flag == 0:
            tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTempI()))
            listaCuadruplos.cuad4("=",22000,0,tablaMemoria.getContTbTempI()-1)
            PilaO.append(tablaMemoria.getContTbTempI()-1)
        

class fun_param1(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # TABLA DE MEMORIA VARFUN
        tablaMemoria.addtbVarFun("p{param}".format(param=incrementarParam()),"int",1,1)

        # REGLA
        # CUADRUPLO PARAM
        listaCuadruplos.cuad4("Param",dirVirtual(PilaO.pop()),0,tablaMemoria.getContTbVarFun()-1)
        
        # FUN_PARAM
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

class fun_param2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # TABLA DE MEMORIA VARFUN
        tablaMemoria.addtbVarFun("p{param}".format(param=incrementarParam()),"int",1,1)

        # REGLA
        # CUADRUPLO PARAM
        listaCuadruplos.cuad4("Param",dirVirtual(PilaO.pop()),0,tablaMemoria.getContTbVarFun()-1)

# --------------------------- WRITE FUNCTION ---------------------------

class write_function(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # WRITE
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class write1(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        #REGLA
        # CUADRUPLO PRINT
        listaCuadruplos.cuad4("print",0,0,dirVirtual(PilaO.pop()))

        # WRITE (RECURSIÓN)
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

class write2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # CUADRUPLO PRINT
        listaCuadruplos.cuad4("print",0,0,dirVirtual(PilaO.pop()))

# --------------------------- READ FUNCTION ---------------------------

class read_function(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # WRITE
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class read1(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        #REGLA
        # CUADRUPLO READ
        listaCuadruplos.cuad4("read",0,0,dirVirtual(PilaO.pop()))

        # read (RECURSIÓN)
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

class read2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # CUADRUPLO READ
        listaCuadruplos.cuad4("read",0,0,dirVirtual(PilaO.pop()))

# ---------------------------- EXPRESSIONS ----------------------------

class expression1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXP_OR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()    

class expression2(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
        # LOGICAL OR
            self.son1.traducir()
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # EXP_OR
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempB())
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        PilaO.append(tablaMemoria.getContTbTempB()-1)
        

class exp_or1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXP_AND
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class exp_or2(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXP_OR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # LOGICAL AND
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            self.son2.traducir()
        # EXP_AND
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()
        
        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempB())
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        PilaO.append(tablaMemoria.getContTbTempB()-1)

class exp_and1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXP_NOT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class exp_and2(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXP_AND
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        # LOGICAL NOT
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # EXP_NOT
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempB())
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        PilaO.append(tablaMemoria.getContTbTempB()-1)


class exp_not1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXP
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class exp_not2(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXP
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # RELATIONAL_L1
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # TERM
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempB())
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        PilaO.append(tablaMemoria.getContTbTempB()-1)

class exp_not3(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXP
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # RELATIONAL_L2
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            self.son2.traducir()
        # TERM
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempB())
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        PilaO.append(tablaMemoria.getContTbTempB()-1)

class exp1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # TERM
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class exp2(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # EXP
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # ARITHMETIC_L1
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # TERM
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()
        
        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempI())
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTempI()))
        PilaO.append(tablaMemoria.getContTbTempI()-1)

class term1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # FACTOR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class term2(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        # FACTOR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        # ARITHMETIC_L2
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        # TERM
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()
        
        # REGLA
        # CUADRUPLO EXP
        listaCuadruplos.cuad4(Poper.pop(), dirVirtual(PilaO.pop(-2)), dirVirtual(PilaO.pop()), tablaMemoria.getContTbTempI())
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTempI()))
        PilaO.append(tablaMemoria.getContTbTempI()-1)

class factor1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class factor2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONST_VAR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class factor3(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # FUNCTION_CALL
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class factor4(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # NOT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

# ---------------------------- OPERATORS ----------------------------

class arithmetic_l1_1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # PLUS
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class arithmetic_l1_2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # MINUS
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class arithmetic_l2_1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # TIMES
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class arithmetic_l2_2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # DIVIDE
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class relational_l1_1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # EQUALS
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class relational_l1_2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # NOT_EQUALS
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class relational_l2_1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # LESS_THAN
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class relational_l2_2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # GREATER_THAN
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class relational_l2_3(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # LESS_THAN_OR_EQUAL
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class relational_l2_4(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # GREATER_THAN_OR_EQUAL
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class logical_or(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # OR
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class logical_and(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # AND
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class logical_not(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # NOT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

# ---------------------------- CONST_VAR ----------------------------
class const_var1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONST_INT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class const_var2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONST_FLOAT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class const_var3(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONST_STRING
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class const_var4(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # CONST_BOOL
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class var1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class var2(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global flagtbVar
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # S1 Y DIRECCION BASE ARREGLO
        a = PilaO.pop()
        if flagtbVar == 1 and a in tablaMemoria.tbVarFun:
            s1 = tablaMemoria.tbVarFun.get(a)[2] - 1
            dirA = tablaMemoria.tbVarFun.get(a)[0]
        else:
            s1 = tablaMemoria.tbVar.get(a)[2] - 1
            dirA = tablaMemoria.tbVar.get(a)[0]

        if dirA not in tablaMemoria.tbConst:
            tablaMemoria.addtbConst(dirA)

        # EXPRESSION
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()
        
        # REGLA
        # CUADRUPLO ARREGLO
        ver = PilaO.pop()
        listaCuadruplos.cuad4("Ver", dirVirtual(ver), 0, dirVirtual(s1))  
        listaCuadruplos.cuad4("+", dirVirtual(ver), tablaMemoria.tbConst.get(dirA), tablaMemoria.getContTbTempP())
        tablaMemoria.addtbTempP("tp{temp}".format(temp=incrementarTempP()))       
        PilaO.append(tablaMemoria.getContTbTempP()-1)


class var3(Nodo):
    def __init__(self, son1, son2, son3):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global flagtbVar
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # S1, S2 Y DIRECCION BASE MATRIZ
        a = PilaO.pop()
        if flagtbVar == 1 and a in tablaMemoria.tbVarFun:
            s1 = tablaMemoria.tbVarFun.get(a)[2] - 1
            s2 = tablaMemoria.tbVarFun.get(a)[3] - 1
            dirM = tablaMemoria.tbVarFun.get(a)[0]
        else:
            s1 = tablaMemoria.tbVar.get(a)[2] - 1
            s2 = tablaMemoria.tbVar.get(a)[3] - 1
            dirM = tablaMemoria.tbVar.get(a)[0]

        if dirM not in tablaMemoria.tbConst:
            tablaMemoria.addtbConst(dirM)

        # EXPRESSION
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # CUADRUPLO MATRIZ 1
        ver = PilaO.pop()
        listaCuadruplos.cuad4("Ver", dirVirtual(ver), 0, dirVirtual(s1))
        listaCuadruplos.cuad4("*", dirVirtual(ver),dirVirtual(s1), tablaMemoria.getContTbTempI())
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTempI()))
        PilaO.append(tablaMemoria.getContTbTempI()-1)

        # EXPRESSION
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO MATRIZ 2
        ver = PilaO.pop()
        listaCuadruplos.cuad4("Ver", dirVirtual(ver), 0, dirVirtual(s2))
        listaCuadruplos.cuad4("+", dirVirtual(PilaO.pop()), dirVirtual(ver), tablaMemoria.getContTbTempI())
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTempI()))
        PilaO.append(tablaMemoria.getContTbTempI()-1)
        listaCuadruplos.cuad4("+", dirVirtual(PilaO.pop()), tablaMemoria.tbConst.get(dirM), tablaMemoria.getContTbTempP())
        tablaMemoria.addtbTempP("tp{temp}".format(temp=incrementarTempP()))
        PilaO.append(tablaMemoria.getContTbTempP()-1)

# ---------------------------- TYPES -------------------------------------

class type1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # INT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class type2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # FLOAT
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class type3(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # STRING
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class type4(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # BOOL
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class type_fun1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # TYPE
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class type_fun2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        # VOID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

# ---------------------------- X ----------------------------

class Id(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global flagtbVar
        # ID
        # REGLA
        PilaO.append(self.name)

class Const_string(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_STRING
        # REGLA
        PilaO.append(self.name)

class Const_int(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_INT
        # REGLA
        if self.name not in tablaMemoria.tbConst:
            tablaMemoria.addtbConst(self.name)
        #PilaO.append(tablaMemoria.tbConst.get(self.name))
        PilaO.append(self.name)

class Const_float(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_FLOAT
        # REGLA
        PilaO.append(str(self.name))

class Const_bool(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_BOOL
        # REGLA
        PilaO.append(str(self.name))

class Int(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # INT
        # REGLA
        Ptipos.append(str(self.name))

class Float(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # FLOAT
        # REGLA
        Ptipos.append(str(self.name))

class String(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # STRING
        # REGLA
        Ptipos.append(str(self.name))

class Bool(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # BOOL
        # REGLA
        Ptipos.append(str(self.name))

class Void(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # VOID
        # REGLA
        Ptipos.append(str(self.name))

class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # ASSIGN
        # REGLA
        Poper.append(self.name)

class Plus(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # PLUS
        # REGLA
        Poper.append(self.name)

class Minus(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # MINUS
        # REGLA
        Poper.append(self.name)

class Times(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # TIMES
        # REGLA
        Poper.append(self.name)

class Divide(Nodo):
    def __init__(self, name):
        self.name = name
    
    def traducir(self):
        # DIVIDE
        # REGLA
        Poper.append(self.name)

class Equals(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # EQUALS
        # REGLA
        Poper.append(self.name)

class Not_equals(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # NOT_EQUALS
        # REGLA
        Poper.append(self.name)

class Lt(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # LT
        # REGLA
        Poper.append(self.name)

class Gt(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # GT
        # REGLA
        Poper.append(self.name)

class Lte(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # LTE
        # REGLA
        Poper.append(self.name)

class Gte(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # GTE
        # REGLA
        Poper.append(self.name)

class Bool_and(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # BOOL_AND
        # REGLA
        Poper.append(self.name)

class Bool_or(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # BOOL_OR
        # REGLA
        Poper.append(self.name)

class Bool_not(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # BOOL_NOT
        # REGLA
        Poper.append(self.name)

