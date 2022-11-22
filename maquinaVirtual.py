from codigoIntermedio import *

my_list = []

with open("codigoIntermedio.txt") as file:
    for line in file:
        my_list.append(line.split())

#print(tbFun)
i = 0
while i < len(my_list):
    if my_list[i][1] == 'Main':
        i = int(my_list[i][2]) - 1
    if my_list[i][0] == 'GOSUB':
        pass
        #print(tbFun.get(my_list[i][1]))
    print(i,my_list[i])
    i += 1
