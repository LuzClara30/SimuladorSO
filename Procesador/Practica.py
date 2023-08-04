
# Importar librerias
import json

# Declaracion de variables globales

AC = 0 # Acumulador

Memoria = {} # Memoria
Datos = {} # Datos
ES = {} # Entrada / Salida

# Declaracion de funciones ----------------------------------------------------------------------------------------

# Funcion para convertir de binario a decimal
def BinarioADecimal(string):#recibe string devuelve int
    binario = int(string)
    decimal = 0
    i = 0
    while (binario>0):
        digito  = binario%10
        binario = int(binario//10)
        decimal = decimal+digito*(2**i)
        i = i+1
    return decimal

# Funcion para convertir de decimal a binario
def DecimalABinario(num):#recibe int devuelve string
    binar = bin(num)
    return (str(binar)).split("b")[1]

# Funcion que permite saber que instrucion ejecutar segun el valor que se le pase
def selectInstruction(valor, memoria1, memoria2):
    if valor == 1:
       instructionOne(memoria1) #llamar a una funcion 
    elif valor == 2:
      instructionTwo(memoria1)
    elif valor == 3:
        instructionThree(memoria1)
    elif valor == 4:
        instructionFour(memoria1, memoria2)
    elif valor == 5:
        instructionFive(memoria1)
    elif valor == 6:
        instructionSix(memoria1, memoria2)
    elif valor == 7:
        instructionSeven(memoria1)
    elif valor == 8:
        instructionEight(memoria1)
    elif valor == 9:
        instructionNine(memoria1)
    elif valor == 10:
        instructionTen(memoria1, memoria2)
    elif valor == 11:
        instructionEleven(memoria1, memoria2)
    elif valor == 12:
        instructionTwelve(memoria1)
    elif valor == 13:
        instructionThirteen(memoria1, memoria2)

# Funciones de lectura y escritura de archivos ----------------------------------------------------------------------

def readJsonDataFile(): # Funcion que lee el archivo de instrucciones
    # Abrir el archivo en modo de lectura
    with open('datos.txt', 'r') as archivo:
        contenido = archivo.read()

    global Datos
    # Convertir el contenido JSON en un diccionario
    Datos = json.loads(contenido)

    # Ahora 'diccionario' contiene la información del archivo en formato de diccionario
    print(Datos)

def readMemoryFile(): # Funcion que lee el archivo de memoria
        # Abrir el archivo en modo de lectura
    with open('memoria.txt', 'r') as archivo:
        contenido = archivo.read()

    global Memoria
    # Convertir el contenido JSON en un diccionario
    Memoria = json.loads(contenido)

    # Ahora 'diccionario' contiene la información del archivo en formato de diccionario
    print(Memoria)

# leer el archivo Es y cargarlo al diccionario 
def readESFile(): # Funcion que lee el archivo de ES
        # Abrir el archivo en modo de lectura
    with open('ES.txt', 'r') as archivo:
        contenido = archivo.read()

    global ES
    # Convertir el contenido JSON en un diccionario
    ES = json.loads(contenido)

    # Ahora 'diccionario' contiene la información del archivo en formato de diccionario
    print(ES)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#resta AC - Memoria1 o Memoria2
def restaACMemory(memoria1):
    global AC
    global Datos
    temp = AC
    mem1 = BinarioADecimal(memoria1)
    dato1 = BinarioADecimal(Datos[str(mem1)])
    return temp - dato1

#suma de memoria1 y memoria2
def sumaMemorias(memoria1, memoria2):
    global Datos
    mem1 = BinarioADecimal(memoria1)
    mem2 = BinarioADecimal(memoria2)
    dato1 = BinarioADecimal(Datos[str(mem1)])
    dato2 = BinarioADecimal(Datos[str(mem2)])
    return dato1 + dato2

#Memoria1 x AC
def Memoria1xAC(memoria1):
    global AC
    temp = AC
    mem1 = BinarioADecimal(memoria1)
    dato1 = BinarioADecimal(Datos[str(mem1)])
    return dato1 * temp

#AC / memoria 1
def divisionACMemoria(memoria1):
    global AC
    temp = AC
    mem1 = BinarioADecimal(memoria1)
    dato1 = BinarioADecimal(Datos[str(mem1)])
    return AC / dato1

# Funciones que representan las instrucciones ------------------------------------------------------------------------

# Carga de memoria 1 hacia AC
def instructionOne(memoria1):
    global Datos
    global AC
    clave = BinarioADecimal(memoria1)
    num2 = BinarioADecimal(Datos[str(clave)])
    #Carga a AC
    AC = num2
    print("Instruccion 1")

# Almacenar en memoria 1 desde AC
def instructionTwo(memoria1):
    global AC
    global Datos
    num = DecimalABinario(AC)
    num2 = BinarioADecimal(memoria1)
    Datos[str(num2)] = num
    print("Instruccion 2")
    
# Suma: memoria 1 + AC
def instructionThree(memoria1):
    global AC
    temp = AC
    mem1 = BinarioADecimal(memoria1)
    dato1 = BinarioADecimal(Datos[str(mem1)])
    AC = dato1 + temp
    print("Instruccion 3")

# Suma: memoria 1 + memoria 2 + AC
def instructionFour(memoria1, memoria2):
    global AC
    global Datos
    temp = AC
    valor = sumaMemorias(memoria1, memoria2)
    AC = temp + valor
    print("Instruccion 4")

# Resta: AC – memoria 1, almacena en AC
def instructionFive(memoria1):
    global AC
    AC = restaACMemory(memoria1)
    print("Instruccion 5")

# Resta: AC – memoria 1, almacena en memoria 2
def instructionSix(memoria1, memoria2):
    num = restaACMemory(memoria1)
    global Datos
    clave = BinarioADecimal(memoria2)
    Datos[str(clave)] = DecimalABinario(num)
    print("Instruccion 6")

# Multiplicación: memoria 1 x AC, almacena en AC
def instructionSeven(memoria1):
    global AC
    resultado = Memoria1xAC(memoria1)
    AC = resultado
    print("Instruccion 7")

# Carga de AC desde dispositivo de E/S, dónde existen
#  hasta 10 dispositivos (identificados del 1 al 10)
def instructionEight(memoria1):
    global ES, AC
    posicion = BinarioADecimal(memoria1)
    datos = ES[str(posicion)]
    AC = BinarioADecimal(datos) 
    print("Instruccion 8")

# Guardar en E/S desde AC, almacena el contenido de AC en un dispositivo de E/S
def instructionNine(memoria1):
    global AC, ES
    posicion = BinarioADecimal(memoria1)
    datos = DecimalABinario(int(AC))
    ES[str(posicion)] = datos
    print("Instruccion 9")

# Suma: memoria 1 + memoria 2, almacena en memoria 1
def instructionTen(memoria1, memoria2):
    resultado = sumaMemorias(memoria1, memoria2)
    global Datos
    clave = BinarioADecimal(memoria1)
    Datos[str(clave)] = DecimalABinario(resultado)
    print("Instruccion 10")

# Multiplicación: memoria 1 x AC, almacena en memoria 2
def instructionEleven(memoria1, memoria2):
    resultado = Memoria1xAC(memoria1)
    global Datos
    clave = BinarioADecimal(memoria2)
    Datos[str(clave)] = DecimalABinario(resultado)
    print("Instruccion 11")

# División: AC / memoria 1, almacena en AC
def instructionTwelve(memoria1):
    global AC
    resultado = divisionACMemoria(memoria1)
    AC = resultado
    print("Instruccion 12")

# División: AC / memoria 1, almacena en memoria 2
def instructionThirteen(memoria1, memoria2):
    resultado = divisionACMemoria(memoria1)
    global Datos
    clave = BinarioADecimal(memoria2)
    Datos[str(clave)] = DecimalABinario(resultado)
    print("Instruccion 13")

# --------------------------------------------------------------------------------------------------------

def actualizar(nombre, diccionario):
    Primero=True
    with open(str(nombre), "w") as archivo:
        archivo.write('{\n')
        for clave, valor in diccionario.items():
            if Primero:
                archivo.write('"'+clave+'": '+'"'+valor+'"')
                Primero=False
            else:
                archivo.write(',\n"'+clave+'": '+'"'+valor+'"')

        archivo.write('\n}\n')

def initial(): # Funcion que inicializa el procesador
    for clave, valor in Memoria.items():
        decimal = BinarioADecimal(valor[:4])
        memoria1 = valor[4:15]
        memoria2 = valor[15:]
        selectInstruction(decimal, memoria1, memoria2)
    global AC, Datos, ES
    print("ACUMULADOR: ")
    print(int(AC))    
    actualizar("datos.txt", Datos)
    print("DATOS ES: " + str(ES))
    actualizar("ES.txt", ES)
    
    # Al finalizar convetir los diccionarios a JSON y guardarlos en su respectivo archivo

def Main(): # Llamada a la funcion principal
   readJsonDataFile() # Llamada a la funcion que lee el archivo de instrucciones
   readMemoryFile()
   readESFile()
   initial()

Main() # Llamada a la funcion principal