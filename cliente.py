from analizadorSintactico import *

# Lista de tests
def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dir, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont)+". "+file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = input('\nNumero de test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print("Has escogido \"%s\"\n"  %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]

# Crea arbol de parseo
#def traducir(result):
#    graphFile = open("graphviztrhee.vz","w")
#    #graphFile.write(result.traducir())
#    graphFile.close()
#    print("El programa traducido se guardo en \"graphviztrhee.vz\"")

# Crea Quadruplos
def codigoIntermedio(result):
    CIFile = open("codigoIntermedio.txt","w")
    CIFile.write(result.traducir())
    CIFile.close()
    print("Codigo Intermedio Generado")


# Abre test
directorio = "C:/Users/rolan/OneDrive/Documentos/9° semestre/Compiladores/Proyecto/test/"
archivo = buscarFichero(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

# Analiza sintacticamente
yacc.yacc()
#result = yacc.parse(cadena,debug=1)
result = yacc.parse(cadena)

# Genera arbol de parseo
#traducir(result)
codigoIntermedio(result)