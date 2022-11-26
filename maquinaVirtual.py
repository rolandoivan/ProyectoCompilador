cont = 0
my_list = []
Saltos = []
Migas = []
tbVar = {}
tbFunc = []

# Guarda constantes realizadas en codigo intermedio
with open("variables.txt") as file:
    for line in file:
        tbVar[line.split()[0]] = line.split()[1]

# Lee codigo intermedio
with open("codigoIntermedio.txt") as file:
    for line in file:
        my_list.append(line.split())

i = 0
# Recorre codigo intermedio
while i < len(my_list):
    #print(tbVar)
    #print(i,my_list[i])

    # VECTORES Y MATRICES
    if my_list[i][0] == "Ver":
        if (int(tbVar.get(my_list[i][1]))<=int(tbVar.get(my_list[i][3]))) and (int(tbVar.get(my_list[i][1]))>=0):
            i = i + 1
        else:
            print("ERROR, Arreglo fuera de rango")
            i = len(my_list)
    
    # ASIGNACION
    elif my_list[i][0] == "=":
        if cont == 0:
            if int(my_list[i][1]) >= 21000 and int(my_list[i][3]) >= 21000:
                #print("30")
                tbVar[tbVar.get(my_list[i][3])] = tbVar.get(tbVar.get(my_list[i][1]))
            elif int(my_list[i][3]) >= 21000:
                #print("10")
                tbVar[tbVar.get(my_list[i][3])] = tbVar.get(my_list[i][1])
            elif int(my_list[i][1]) >= 21000:
                #print("20")
                tbVar[my_list[i][3]] = tbVar.get(tbVar.get(my_list[i][1]))
            else:
                #print("40")
                tbVar[my_list[i][3]] = tbVar.get(my_list[i][1])
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                tbFunc[cont-1][my_list[i][3]] = tbFunc[cont-1].get(my_list[i][1])
            else:
                tbFunc[cont-1][my_list[i][3]] = tbVar.get(my_list[i][1])
        i = i + 1
    
    # I/O
    elif my_list[i][0] == "print":
        if cont == 0:
            if int(my_list[i][3]) >= 21000:
                print(tbVar.get(tbVar.get(my_list[i][3])))
            else:
                print(tbVar.get(my_list[i][3]))
        else:
            if int(my_list[i][3]) >= 21000:
                print(tbFunc[cont-1].get(my_list[i][3]),"pointer")
            else:
                if my_list[i][3] in tbFunc[cont-1]:
                    print(tbFunc[cont-1].get(my_list[i][3]))
                else:
                    print(tbVar[cont-1].get(my_list[i][3]))
        i += 1

    elif my_list[i][0] == "read":
        if cont == 0:
            if int(my_list[i][3]) >= 21000:
                tbVar[tbVar.get(my_list[i][3])] = input()
            else:
                tbVar[my_list[i][3]] = input()
        i += 1

    # OPERADORES
    elif my_list[i][0] == "*":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 * n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) * int(n2)
        i += 1
        
    elif my_list[i][0] == "/":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 / n2    
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) / int(n2)
        i += 1

    elif my_list[i][0] == "+":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 + n2    
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) + int(n2)
        i += 1

    elif my_list[i][0] == "-":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 - n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) - int(n2)
        i += 1
        
    elif my_list[i][0] == "<":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 < n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) < int(n2)
        i += 1
        
    elif my_list[i][0] == ">":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 > n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) > int(n2)
        i += 1
        
    elif my_list[i][0] == "<=":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 <= n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) <= int(n2)
        i += 1
        
    elif my_list[i][0] == ">=":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 >= n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) >= int(n2)
        i += 1
        
    elif my_list[i][0] == "==":
        if cont == 0:
            if int(my_list[i][1]) < 21000:
                n1 = int(tbVar.get(my_list[i][1]))
            elif tbVar.get(tbVar.get(my_list[i][1])) == None:
                print("Error: Variable no declarada declarada")
                i = len(my_list)
                break
            elif int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            if int(my_list[i][2]) < 21000:
                n2 = int(tbVar.get(my_list[i][2]))
            elif tbVar.get(tbVar.get(my_list[i][2])) == None:
                print("Error: Variable no declarada declarada")
                i = len(my_list)
                break
            elif int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            tbVar[my_list[i][3]] = n1 == n2
                
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) == int(n2)
        i += 1
        
    elif my_list[i][0] == "!=":
        if cont == 0:
            if int(my_list[i][1]) >= 21000:
                n1 = int(tbVar.get(tbVar.get(my_list[i][1])))
            else:
                n1 = int(tbVar.get(my_list[i][1]))
            if int(my_list[i][2]) >= 21000:
                n2 = int(tbVar.get(tbVar.get(my_list[i][2])))
            else:
                n2 = int(tbVar.get(my_list[i][2]))
            tbVar[my_list[i][3]] = n1 != n2
        else:
            if my_list[i][1] in tbFunc[cont-1]:
                n1 = tbFunc[cont-1].get(my_list[i][1])
            else:
                n1 = tbVar.get(my_list[i][1])
            if my_list[i][2] in tbFunc[cont-1]:
                n2 = tbFunc[cont-1].get(my_list[i][2])
            else:
                n2 = tbVar.get(my_list[i][2])
            tbFunc[cont-1][my_list[i][3]] = int(n1) != int(n2)
        i += 1

    #FUNCIONES
    elif my_list[i][0] == 'ERA':
        tbFunc.append({})
        #cont += 1
        i += 1

    elif my_list[i][0] == "Param":
        if cont == 0:
            tbFunc[cont][my_list[i][3]] = tbVar.get(my_list[i][1])
        else:
            tbFunc[cont][my_list[i][3]] = tbFunc[cont-1].get(my_list[i][1])
        i += 1

    elif my_list[i][0] == 'GOSUB':
        Migas.append(i+1)
        cont += 1
        i = int(my_list[i][2])-1

    elif my_list[i][0] == 'EndProc' and len(Migas) > 0:
        tbFunc.pop()
        cont -= 1
        i = Migas.pop()

    elif my_list[i][0] == "Ret":
        if my_list[i][1] in tbFunc[cont-1]:
            tbVar[my_list[i][3]] = tbFunc[cont-1].get(my_list[i][1])
        else:
            tbVar[my_list[i][3]] = tbVar.get(my_list[i][1])
        tbFunc.pop()
        cont -= 1
        i = Migas.pop()

    # SALTOS
    elif my_list[i][1] == 'Main':
        i = int(my_list[i][3])-1

    elif my_list[i][0] == 'GotoV':
        if cont == 0 and tbVar.get(my_list[i][1]) == True:
            i = int(my_list[i][3])-1
        elif tbFunc[cont-1].get(my_list[i][1]) == True:
            i = int(my_list[i][3])-1
        else:
            i += 1
        
    elif my_list[i][0] == 'GotoF':
        if cont == 0  and tbVar.get(my_list[i][1]) == False:
            i = int(my_list[i][3])-1
        elif cont != 0 and tbFunc[cont-1].get(my_list[i][1]) == False:
            i = int(my_list[i][3])-1
        else:
            i += 1

    elif my_list[i][0] == 'Goto':
        i = int(my_list[i][3])-1

    elif my_list[i][0] == 'EndProc':
        if len(tbFunc) > 0:
            tbFunc.pop()
        i += 1

    else :
        i += 1
    #print(cont)
    #print(tbFunc)
    #print(tbVar)

#print(stackFun)
#print(tbFunc)