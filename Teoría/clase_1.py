#Data types

#Enteros: Números enteros

#Variable: En minúscula, puede variar en el programa  %d
number = 5 
#Constant: En mayúsculas, no varía en el programa
NUMBER = 4

#Float: Números con decimales  %f
number_float = 5.5

#String: Cadena de caractéres  %s
message = "Brisa vas a ser mia"

#Booleans: Verdadero o falso  %s
boolean = True

#Para saber cual es el tipo de variable
print(type(number))

#Para cambiarle el type a la variable  (El "int" es el tipo de variable que quiero)
variable1=int(input=("Ingrese un valor: "))

#Forma de dar formato a textos

print("Valor de number: %d, valor de message %s" % (number, message))

print("Valor de number: {}, valor de message: {}".format (number, message))

print(f"Valor de number: {number}, valor de message: {message}")

print("Valor de number: {0}, valor de message: {1}".format(number, message))

#Para pedirle algo al usuario  input()
name = input("Ingrese su nombre: ").capitalize()
print(f"Hola {name}, como estás?")

#Ejemplo
number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese otro número: "))

result = number1 + number2
print(f"La suma es: {result}")




#PARA AGREGAR A LA LISTA

#append (para agregar un objeto al final de la lista)
#variable.append(objeto)


#insert (para agregar un objeto en alguna posición de la lista)
#variable.insert(posición, objeto)

#PARA QUITAR DE LA LISTA

#pop (para quitar de una posición especifica)
#variable.pop(posición)

#PARA RECORRER ELEMENTOS DE LA LISTA

#variable_lista=[1,2,3]
#for element in variable_lista:
#   print (element)

#for index in range(len(variable_lista)):
#   print(variable_lista[index])


#VECTORES
#Son listas unidimensionales
vector = [1,2,3]

#MATRICES
#Son listas dentro de listas, cada lista es una fila y cada elemento de adentro es la columna
matrix = [[1,2,3,4],[0,6,7,0],[4,2,7,5]]

#Acceder a un elemento de una matriz
#Se nombra primero la lista a la que quiero acceder, luego el elemento dentro de esa lista
print(matrix[0][2])

#Para modificar un elemento
#Nombramos la matriz, elegimos la lista dentro de ella, luego el elemento que queremos reemplazar y después le damos el nuevo valor
matrix[0][1]=8

#Para modificar una fila completa
#Nombramos la matriz, nombramos la lista completa y le damos un nuevo valor
matrix[0]=[4,3,2,1]

#Matriz con strings
students=[["Lopez", "Carlos", "18"], ["Ruiz", "Carla", "19"], ["Perez", "Martina", "20"]]

#Se accede de la misma manera que a las otras listas
#Para una fila
print(students[0])

#Para un solo elemento
print(students[2][1])

#Para la matriz completa
print(students)

#Imprimirla de forma de matriz
for element in students:
    print(element)

#Para crear una matriz de cero
matrix1=[]
for row in range(2): #Para el numero de filas
    rows=[]
    for column in range(3): #Para el número de columnas
        rows.append(0)
    matrix1.append(rows) #Para agregar las filas creadas a la matriz
print(matrix1)

#Otra forma de crear una matriz
import random
matrix=[[random.randint(1,10) for _ in range(4)] for _ in range(5)] #range(4) es la cantidad de columnas y range(5) la cantidad de filas

#Para imprimir los elementos de la matriz uno debajo del otro
matrix2=[[1,2,3],[3,2,1]]
rows1=len(matrix2)
columns=len(matrix2[0])
for row1 in range(rows1):
    for column1 in range(columns):
        print(matrix2[row1][column1])


#MATRICES TRIDIMENSIONALES
#filas x columnas x profundidad

#El primer corchete es para definir la matriz, el segundo para definir la profundidad, 
#el tercero define las filas, y los elementos definen las columnas

#matriz 2x2x2
matriz = [[[1,2],[2,0]],
          [[2,3],[4,3]]]

#matriz completa
print(matriz)
#profundidad
print(len(matriz))
#filas
print(len(matriz[0]))
#columnas
print(len(matriz[0][0]))


#FUNCIONES
"""
def nombre_funcion(parámetros):
    bloque de código
    return
"""


#ARCHIVOS

#Forma vieja
file_name = "mi_archivo.txt"                #Creamos el archivo
file = open(file_name, "a")                 #Abrimos el archivo
name = input("Ingrese su nombre: ")         #Le pedimos datos al usuario por consola
file.write(f"Su nombre es: {name}\n")       #Agregamos esa informacíón al archivo
print(file.readlines())                     #Hace que cada linea del texto sea un elemento de una lista
file.strip()                                #Elimina todos los espaciados (\) del principio y final del string
file.close()                                #Cerramos el archivo de forma segura

#Forma nueva
with open(file_name, "r") as file:          #Se utiliza el ´with´ que genera un bloque de código y cierra de forma segura el archivo
    for line in file:                       #El ´for´ es un ejemplo de como se puede recorrer las lineas de un archivo
        line = line.strip()                 #Se eliminan los espaciados 
        print(line)                         #Y se imprime cada elemento en una fila separada

#Para comprobar la existencia de un archivo
import os                                   #Importamos el módulo ´os´
if os.path.exist(file_name):                #Comprobamos su existencia
    print("Existe")                         #Si existe ejecuta este print
else:                                       
    print("No existe")                      #Si no existe ejecuta este print

#Para eliminar archivos
import os
if os.path.exist(file_name):                #Comprueba la existencia
    os.remove(file_name)                    #Si existe lo elimina
else:
    print("No existe")                      #Si no existe ejecuta el print

#Para determinar la ruta del archivo
import os
ruta = os.path.abspath(file_name)           #Le pedimos que busque la ruta
print(ruta)                                 #Y la mostramos en pantalla