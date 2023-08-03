
# Importar librerias
import json

# Declaracion de variables globales

AC = 0 # Acumulador

Memoria = {} # Memoria
Datos = {} # Datos
ES = {} # Entrada / Salida

# Declaracion de funciones

# Funcion que permite saber que instrucion ejecutar segun el valor que se le pase
def selectInstruction(valor):
    if valor == 1:
       instructionOne() #llamar a una funcion 
    elif valor == 2:
      instructionTwo()
    elif valor == 3:
        instructionThree()
    elif valor == 4:
        instructionFour()
    elif valor == 5:
        instructionFive()
    elif valor == 6:
        instructionSix()
    elif valor == 7:
        instructionSeven()
    elif valor == 8:
        instructionEight()
    elif valor == 9:
        instructionNine()
    elif valor == 10:
        instructionTen()
    elif valor == 11:
        instructionEleven()
    elif valor == 12:
        instructionTwelve()
    elif valor == 13:
        instructionThirteen()

# Funciones de lectura y escritura de archivos

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
# Funciones que representan las instrucciones

# Carga de memoria 1 hacia AC
def instructionOne():
    print("Instruccion 1")

# Almacenar en memoria 1 desde AC
def instructionTwo():
    print("Instruccion 2")

# Suma: memoria 1 + AC
def instructionThree():
    print("Instruccion 3")

# Suma: memoria 1 + memoria 2 + AC
def instructionFour():
    print("Instruccion 4")

# Resta: AC – memoria 1, almacena en AC
def instructionFive():
    print("Instruccion 5")

# Resta: AC – memoria 1, almacena en memoria 2
def instructionSix():
    print("Instruccion 6")

# Multiplicación: memoria 1 x AC, almacena en AC
def instructionSeven():
    print("Instruccion 7")

# Carga de AC desde dispositivo de E/S, dónde existen hasta 10 dispositivos (identificados del 1 al 10)
def instructionEight():
    print("Instruccion 8")

# Guardar en E/S desde AC, almacena el contenido de AC en un dispositivo de E/S
def instructionNine():
    print("Instruccion 9")

# Suma: memoria 1 + memoria 2, almacena en memoria 1
def instructionTen():
    print("Instruccion 10")

# Multiplicación: memoria 1 x AC, almacena en memoria 2
def instructionEleven():
    print("Instruccion 11")

# División: AC / memoria 1, almacena en AC
def instructionTwelve():
    print("Instruccion 12")

# División: AC / memoria 1, almacena en memoria 2
def instructionThirteen():
    print("Instruccion 13")

# Funcines Logicas del procesador

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

def DecimalABinario(num):#recibe int devuelve string
    binar = bin(num)
    return str(binar)[2::]

def initial(): # Funcion que inicializa el procesador
    for clave, valor in Memoria.items():
        decimal = BinarioADecimal(valor[0:4])
        selectInstruction(decimal)
    
    # Al finalizar convetir los diccionarios a JSON y guardarlos en su respectivo archivo

def Main(): # Llamada a la funcion principal
   readJsonDataFile() # Llamada a la funcion que lee el archivo de instrucciones
   readMemoryFile()
   readESFile()
   initial()

Main() # Llamada a la funcion principal