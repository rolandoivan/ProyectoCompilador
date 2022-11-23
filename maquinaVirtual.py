from codigoIntermedio import *

my_list = []
Saltos = []
Migas = []
tbVar = {}

with open("variables.txt") as file:
    for line in file:
        tbVar[line.split()[0]] = line.split()[1]

with open("codigoIntermedio.txt") as file:
    for line in file:
        my_list.append(line.split())

i = 0
while i < len(my_list):
    # ASIGNNACION
    if my_list[i][0] == "=" or my_list[i][0] == "Param":
        tbVar[my_list[i][3]] = tbVar.get(my_list[i][1])
    
    elif my_list[i][0] == "print":
        if int(my_list[i][3]) >= 21000:
            #pointer = tbVar.get(my_list[i][3])
            #print(tbVar.get(pointer))
            print(tbVar.get(my_list[i][3]),"pointer")
        else:
            print(tbVar.get(my_list[i][3]))

    # OPERADORES
    if my_list[i][0] == "*":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) * int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == "/":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) / int(tbVar.get(my_list[i][2]))

    if my_list[i][0] == "+":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) + int(tbVar.get(my_list[i][2]))

    if my_list[i][0] == "-":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) - int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == "<":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) < int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == ">":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) > int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == "<=":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) <= int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == ">=":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) >= int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == "==":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) == int(tbVar.get(my_list[i][2]))
        
    if my_list[i][0] == "!=":
        tbVar[my_list[i][3]] = int(tbVar.get(my_list[i][1])) != int(tbVar.get(my_list[i][2]))

    # SALTOS
    if my_list[i][0] == "Ret":
        tbVar[my_list[i][3]] = tbVar.get(my_list[i][1])
        #Saltos.pop()
        #i = Migas.pop()+1

    if my_list[i][1] == 'Main':
        i = int(my_list[i][3])-1

    if my_list[i][0] == 'GotoV' and tbVar.get(my_list[i][1]) == True:
        i = int(my_list[i][3])-1
        
    if my_list[i][0] == 'GotoF' and tbVar.get(my_list[i][1]) == False:
        i = int(my_list[i][3])-1

    if my_list[i][0] == 'Goto':
        i = int(my_list[i][3])-1
        
    if my_list[i][0] == 'GOSUB':
        Migas.append(i-1)
        Saltos.append(int(my_list[i][3])-1)
        i = int(my_list[i][2])-2

    if len(Saltos) > 0 and i == Saltos[-1]:
        Saltos.pop()
        i = Migas.pop()+1
    i += 1
