txt = " "
cont = 0

def incrementarCont():
    global cont
    cont = cont + 1
    return "%d" %cont

class Nodo():
    pass

class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"
        return id

class program(Nodo):
    def __init__(self, son1, son2,son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        txt += id+"[label= "+self.name+"]"+"\n\t"
        txt += id+"->"+son1+"\n\t"
        txt += id+"->"+son2+"\n\t"
        txt += id+"->"+son3+"\n\t"
        txt += id+"->"+son4+"\n\t"
        return "digraph G {\n\t"+txt+"}"
    
class block(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class content_block(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class functions(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
    
    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        return id

class param(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class params1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class params2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id


class statment1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment7(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment8(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class statment9(Nodo):
    pass

class vars(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class vars_n1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class vars_n2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class assignment(Nodo):
    def __init__(self, son1, son2,son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class condition(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class condition_else1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class condition_else2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class for_loop(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        return id

class for_param1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class for_param2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class for_param3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class while_loop(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class function_call(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class fun_param1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class fun_param2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class write_function(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class write1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class write2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        return id

class write3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class write4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id



class expression1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class expression2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class exp_lo_1_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class exp_lo_1_2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class exp_lo_2_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class exp_lo_2_2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class exp_lo_3_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class exp_lo_3_2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class exp_lo_3_3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class exp1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class exp2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class term1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class term2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id

class factor1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class factor2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id



class const_var1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class const_var2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class const_var3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class const_var4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id 

class type1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class type2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class type3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class type4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class type_fun1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class type_fun2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id



class arithmetic_op_l1_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class arithmetic_op_l1_2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class arithmetic_op_l2_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class arithmetic_op_l2_2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class relational_op_l1_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class relational_op_l1_2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class relational_op_l2_1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class relational_op_l2_2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class relational_op_l2_3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class relational_op_l2_4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class logical_op_l1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class logical_op_l2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class logical_op_l3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def traducir(self):
        global txt
        id = incrementarCont()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id


class Id(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+str(self.name)+"\"]"+"\n\t"
        return id

class Const_string(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Const_int(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+str(self.name)+"\"]"+"\n\t"
        return id

class Const_float(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+str(self.name)+"\"]"+"\n\t"
        return id

class Int(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Float(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class String(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Void(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Bool(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Plus(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Minus(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Times(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Divide(Nodo):
    def __init__(self, name):
        self.name = name
    
    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Equals(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Not_equals(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Lt(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Gt(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Lte(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Gte(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Bool_and(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Bool_or(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

class Bool_not(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarCont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"
        return id

