from memoria import *
from cuadruplos import *

tablaMemoria = Memoria()
pila = Pilas()

#listaCuadruplos = Cuadruplos()

flag = 0
txt = ""
flagtbVar = 0

def dirVirtual(self):
    if self in tablaMemoria.tbVarFun :
        return tablaMemoria.tbVarFun.get(self)[0]
    elif self in tablaMemoria.tbVar:
        return tablaMemoria.tbVar.get(self)[0]
    elif self in tablaMemoria.tbConst:
        return tablaMemoria.tbConst.get(self)
    elif self in tablaMemoria.tbTempI:
        return tablaMemoria.tbTempI.get(self)
    elif self in tablaMemoria.tbTempB:
        return tablaMemoria.tbTempB.get(self)
    elif self in tablaMemoria.tbTempP:
        return tablaMemoria.tbTempP.get(self)
    else:
        return self

listaCuadruplos = []


temp = 0
def incrementarTemp():
    global temp
    temp = temp + 1
    return "%d" %temp

def reiniciarTemp():
    global temp
    temp = 0

def getTemp():
    global temp
    return "%d" %temp

parm = 0
def incrementarParam():
    global parm
    parm = parm + 1
    return "%d" %parm

def reiniciarParam():
    global parm
    parm = 0

def getParam():
    global parm
    return "%d" %parm

tempP = 0
def incrementarTempP():
    global tempP
    tempP = tempP + 1
    return "%d" %tempP

def reiniciarTempP():
    global tempP
    tempP = 0

def getTempP():
    global tempP
    return "%d" %tempP

tempB = 0
def incrementarTempB():
    global tempB
    tempB = tempB + 1
    return "%d" %tempB

def reiniciarTempB():
    global tempB
    tempB = 0

def getTempB():
    global tempB
    return "%d" %tempB
# ---------------------------

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
        global txt
        global flagtbVar

        # REGLA
        # CUADRUPLO DE INICIO
        listaCuadruplos.append(cuadruplo("Goto",None,None,'Main').cuad3())
        #migajitas.append(cuadruplo.getCont(cuadruplo))
        pila.addPmigas(cuadruplo.getCont(cuadruplo))
        
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
        #Psaltos.insert(0, cuadruplo.getCont(cuadruplo)+1)
        pila.addStartPsaltos(0,cuadruplo.getCont(cuadruplo)+1)

        # BLOCK
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO DE FIN
        listaCuadruplos.append(cuadruplo("EndProc",None,None,None).cuadEnd())
        tablaMemoria.reiniciarCont()
        reiniciarTemp()
        reiniciarTempB()
        reiniciarTempP()

        # REGLA
        #print(Memoria.__str__())
        print(tablaMemoria.tbFun)
        print(tablaMemoria.tbConst)
        print(tablaMemoria.tbVar)
        print(tablaMemoria.tbTempI)
        print(tablaMemoria.tbTempB)
        print(tablaMemoria.tbTempP)
        #aux = migajitas.pop(0)
        aux = pila.delPmigas(0)
        for i in range(len(listaCuadruplos)):
            if i == aux-1:
                txt = txt + str(listaCuadruplos.pop(0)) + " " + str(pila.delPsaltos(0)) + "\n"
                if pila.lenPmigas() > 0:
                    aux = pila.delPmigas(0)
            else:
                txt = txt + str(listaCuadruplos.pop(0)) + "\n"
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
        
        tablaMemoria.addtbFun(pila.delPilaO(-1),cuadruplo.getCont(cuadruplo)+1)
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

        print(tablaMemoria.tbVarFun)
        tablaMemoria.tbVarFun.clear()
        # REGLA
        # CUADRUPLO DE FIN DE FUNCION
        listaCuadruplos.append(cuadruplo("EndProc",None,None,None).cuadEnd())
        tablaMemoria.reiniciarCont()
        reiniciarTemp()
        reiniciarTempB()
        reiniciarTempP()
        #fun.setFin(cuadruplo.getCont(cuadruplo))

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
        tablaMemoria.addtbVarFun(pila.delPilaO(0), pila.delPtipos(0),1,1)

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
        tablaMemoria.addtbVarFun(pila.delPilaO(0), pila.delPtipos(0),1,1)

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
        listaCuadruplos.append(cuadruplo("Ret",None, None, pila.delPilaO(-1)).cuad4())

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
        global txt
        # ID
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()
        #print("size 1")

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
        tipo = pila.delPtipos(-1)
        for i in range(pila.lenPilaO()):
            if flagtbVar == 0:
                tablaMemoria.addtbVar(pila.delPilaO(0), tipo, 1, 1)
            else:
                tablaMemoria.addtbVarFun(pila.delPilaO(0), tipo, 1, 1)

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
        
        size = pila.delPilaO(-1)
        if flagtbVar == 0:
            tablaMemoria.addtbVar(pila.delPilaO(0), pila.delPtipos(0), size+1, 1)
        else:
            tablaMemoria.addtbVarFun(pila.delPilaO(0), pila.delPtipos(0), size+1, 1)

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

        size = pila.delPilaO(-1)
        size2 = pila.delPilaO(-1)
        if flagtbVar == 0:
            tablaMemoria.addtbVar(pila.delPilaO(0), pila.delPtipos(0), size+1, size2+1)
        else:
            tablaMemoria.addtbVarFun(pila.delPilaO(0), pila.delPtipos(0), size+1, size2+1)

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
        listaCuadruplos.append(cuadruplo(pila.delPoper(),pila.delPilaO(-1),None,pila.delPilaO(-1)).cuad4())

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
        listaCuadruplos.append(cuadruplo("GotoF",None, None, pila.delPilaO(-1)).cuad4())
        #migajitas.append(cuadruplo.getCont(cuadruplo))
        pila.addPmigas(cuadruplo.getCont(cuadruplo))
        
        # BLOCK
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # PILA DE SALTO GOTF IF
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

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
        # CUADRUPLO GOTF ELIF
        listaCuadruplos.append(cuadruplo("GotoF",None,None,pila.delPilaO(-1)).cuad4())
        #migajitas.append(cuadruplo.getCont(cuadruplo))
        pila.addPmigas(cuadruplo.getCont(cuadruplo))

        # BLOCK
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # PILA DE SALTO GOTOF ELIF
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)
        
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
        #Psaltos.pop()
        pila.delPsaltos(-1)
        listaCuadruplos.append(cuadruplo("Goto",None,None,None).cuad3())
        #migajitas.append(cuadruplo.getCont(cuadruplo))
        pila.addPmigas(cuadruplo.getCont(cuadruplo))
        # REGLA
        # PILA DE SALTO GOTOF
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

        # BLOCK
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # PILA DE SALTO GOTO ELSE
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

# --------------------------- WHILE LOOP ---------------------------

class while_loop(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        # REGLA
        # PILA DE SALTO GOTO WHILE
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        #REGLA
        # CUADRUPLO GOTOF WHILE
        listaCuadruplos.append(cuadruplo("GotoF",None,None,pila.delPilaO(-1)).cuad4())
        #migajitas.append(cuadruplo.getCont(cuadruplo))
        pila.addPmigas(cuadruplo.getCont(cuadruplo))

        # BLOCK
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLA
        # CUADRUPLO GOTO WHILE
        listaCuadruplos.append(cuadruplo("Goto",None,None,pila.delPsaltos(-1)).cuad4())
        
        # REGLA
        # PILA DE SALTO GOTOF WHILE
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)


# --------------------------- DO WHILE ---------------------------

class do_while_loop(Nodo):
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2
        
    def traducir(self):

        # REGLA
        # PILA DE SALTO GOTO
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

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
        listaCuadruplos.append(cuadruplo("GotoV",pila.delPilaO(-1),None,pila.delPsaltos(-1)).cuad4())
        
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
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

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

        #REGLA
        # CUADRUPLO GOTOF FOR
        listaCuadruplos.append(cuadruplo("GotoF",None,None,pila.delPilaO(-1)).cuad4())
        #migajitas.append(cuadruplo.getCont(cuadruplo))
        pila.addPmigas(cuadruplo.getCont(cuadruplo))

        # BLOCK
        if type(self.son4) == type(tuple()):
            self.son4[0].traducir()
        else:
            self.son4.traducir()

        #REGLA
        # CUADRUPLO GOTO FOR
        listaCuadruplos.append(cuadruplo("Goto",None,None,pila.delPsaltos(-1)).cuad4())
        
        # REGLA
        # PILA DE SALTO GOTOF
        #Psaltos.append(cuadruplo.getCont(cuadruplo)+1)
        pila.addPsaltos(cuadruplo.getCont(cuadruplo)+1)

class for_param1(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        global txt
        # ASIGNACION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

class for_param2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        global txt
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
        
        # REGLAS
        reiniciarParam()
        fun = pila.delPilaO(-1)

        # CUADRUPLO ERA
        listaCuadruplos.append(cuadruplo("ERA",None,None,fun).cuad4())

        # FUN_PARAM
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

        # REGLAS
        # CUADRUPLO GOSUB
        listaCuadruplos.append(cuadruplo("GOSUB",None,None,fun).cuad4())
        # CUADRUPLO ASIGNACION DE FUN A TEMP
        if flag == 0:
            tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTemp()))
            listaCuadruplos.append(cuadruplo("=",fun,None,tablaMemoria.getContTbTempI()).cuad4())
            #PilaO.append("t{temp}".format(temp=temp))
            pila.addPilaO("t{temp}".format(temp=temp))
        

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
        # CUADRUPLO PARAM
        listaCuadruplos.append(cuadruplo("Param",pila.delPilaO(-1),None,"par{parm}".format(parm=incrementarParam())).cuad4())

        # FUN_PARAM
        if type(self.son2) == type(tuple()):
            self.son2[0].traducir()
        else:
            self.son2.traducir()

class fun_param2(Nodo):
    def __init__(self, son1):
        self.son1 = son1

    def traducir(self):
        global txt
        # EXPRESSION
        if type(self.son1) == type(tuple()):
            self.son1[0].traducir()
        else:
            self.son1.traducir()

        # REGLA
        # CUADRUPLO PARAM
        listaCuadruplos.append(cuadruplo("Param",pila.delPilaO(-1),None,"par{parm}".format(parm=incrementarParam())).cuad4())


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
        # CUADRUPLO WRITE
        listaCuadruplos.append(cuadruplo("print",None,None,pila.delPilaO(-1)).cuad4())

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
        listaCuadruplos.append(cuadruplo("print",None,None,pila.delPilaO(-1)).cuad4())
        
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
        listaCuadruplos.append(cuadruplo("read",None,None,pila.delPilaO(-1)).cuad4())
        
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
        listaCuadruplos.append(cuadruplo("read",None,None,pila.delPilaO(-1)).cuad4())
        

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
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-2), pila.delPilaO(-1), tablaMemoria.getContTbTempB()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempB())
        

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
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-2), pila.delPilaO(-1), tablaMemoria.getContTbTempB()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempB())

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
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-2), pila.delPilaO(-1), tablaMemoria.getContTbTempB()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempB())


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
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-2), pila.delPilaO(-1), tablaMemoria.getContTbTempB()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempB())

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
        tablaMemoria.addtbTempB("tb{temp}".format(temp=incrementarTempB()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-2), pila.delPilaO(-1), tablaMemoria.getContTbTempB()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempB())

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
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTemp()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-2), pila.delPilaO(-1), tablaMemoria.getContTbTempI()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempI())

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
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTemp()))
        listaCuadruplos.append(cuadruplo(pila.delPoper(), pila.delPilaO(-1), pila.delPilaO(-1), tablaMemoria.getContTbTempI()).cuadExp())
        pila.addPilaO(tablaMemoria.getContTbTempI())
        
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
        global txt
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

        # REGLA PROVISIONAL
        a = pila.delPilaO(-1)
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
        ver = pila.delPilaO(-1)
        listaCuadruplos.append(cuadruplo("Ver", ver, "0", s1).cuad4())
        tablaMemoria.addtbTempP("tp{temp}".format(temp=incrementarTempP()))
        listaCuadruplos.append(cuadruplo("+", ver, tablaMemoria.tbConst.get(dirA), tablaMemoria.getContTbTempP()).cuad4())
        #PilaO.append("tp{temp}".format(temp=tempP)) ##Pointer
        pila.addPilaO("tp{temp}".format(temp=incrementarTempP()))


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

        # REGLA PROVISIONAL
        a = pila.delPilaO(-1)
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
        # CUADRUPLO MATRIZ1
        ver = pila.delPilaO(-1)
        listaCuadruplos.append(cuadruplo("Ver", ver, "0", s1).cuad4())
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTemp()))
        listaCuadruplos.append(cuadruplo("*", ver, s1, tablaMemoria.getContTbTempI()).cuad4())
        #PilaO.append("t{temp}".format(temp=temp))
        pila.addPilaO("t{temp}".format(temp=incrementarTemp()))

        # EXPRESSION
        if type(self.son3) == type(tuple()):
            self.son3[0].traducir()
        else:
            self.son3.traducir()

        # REGLA
        # CUADRUPLO MATRIZ2
        ver = pila.delPilaO(-1)
        listaCuadruplos.append(cuadruplo("Ver", ver, "0", s2).cuad4())
        tablaMemoria.addtbTempI("t{temp}".format(temp=incrementarTemp()))
        listaCuadruplos.append(cuadruplo("+", pila.delPilaO(-1), ver, tablaMemoria.getContTbTempI()).cuad4())
        #PilaO.append("t{temp}".format(temp=temp))
        pila.addPilaO("t{temp}".format(temp=incrementarTemp()))
        tablaMemoria.addtbTempP("tp{temp}".format(temp=incrementarTempP()))
        listaCuadruplos.append(cuadruplo("+", pila.delPilaO(-1), tablaMemoria.tbConst.get(dirM), tablaMemoria.getContTbTempP()).cuad4())
        #PilaO.append("tp{tempP}".format(tempP=tempP)) ##Pointer
        pila.addPilaO("tp{tempP}".format(tempP=incrementarTempP()))

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
        #PilaO.append(self.name)
        pila.addPilaO(self.name)

class Const_string(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_STRING
        # REGLA
        #PilaO.append(self.name)
        pila.addPilaO(self.name)

class Const_int(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_INT
        # REGLA
        if self.name not in tablaMemoria.tbConst:
            tablaMemoria.addtbConst(self.name)
        #PilaO.append(self.name)
        pila.addPilaO(self.name)

class Const_float(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_FLOAT
        # REGLA
        #PilaO.append(str(self.name))
        pila.addPilaO(str(self.name))

class Const_bool(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # CONST_BOOL
        # REGLA
        #PilaO.append(str(self.name))
        pila.addPilaO(str(self.name))

class Int(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # INT
        # REGLA
        #Ptipos.append(str(self.name))
        pila.addPtipos(str(self.name))

class Float(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # FLOAT
        # REGLA
        #Ptipos.append(str(self.name))
        pila.addPtipos(str(self.name))

class String(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # STRING
        # REGLA
        #Ptipos.append(str(self.name))
        pila.addPtipos(str(self.name))

class Bool(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # BOOL
        # REGLA
        #Ptipos.append(str(self.name))
        pila.addPtipos(str(self.name))

class Void(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        # VOID
        # REGLA
        #Ptipos.append(str(self.name))
        pila.addPtipos(str(self.name))

class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # ASSIGN
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Plus(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # PLUS
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Minus(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # MINUS
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Times(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # TIMES
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Divide(Nodo):
    def __init__(self, name):
        self.name = name
    
    def traducir(self):
        # DIVIDE
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Equals(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # EQUALS
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Not_equals(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # NOT_EQUALS
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Lt(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # LT
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Gt(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # GT
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Lte(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # LTE
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Gte(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # GTE
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Bool_and(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # BOOL_AND
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Bool_or(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # BOOL_OR
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

class Bool_not(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        # BOOL_NOT
        # REGLA
        #Poper.append(self.name)
        pila.addPoper(self.name)

