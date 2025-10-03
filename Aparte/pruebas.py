#Dada una matriz de 6x5 con números enteros mayores a 50 generados aleatoriamente, crea una función que retorne una matriz
#que tenga una columna más (6x6), con los valores originales de la matriz ingresada y en la columna extra, 
#coloque la suma de los numeros de cada fila

""""
import random

matriz=[[random.randint(1,50) for _ in range(5)] for _ in range(6)]

for row in matriz:
    print(row)
print()
for row in matriz:
    suma=0
    for column in row:
        suma=suma + column
    row.append(suma)
    print(row)
"""

#1
"""
word1=input("Ingrese una palabra: ")
if word1[-1] == "a" or word1[-1] == "o":
    print("La palabra termina en A o en O")
else:
    print("No termina en A ni en O")
"""
#2
"""
lista_num=[1,2,3,4,5,6,7,8,9,10]

for entre in lista_num:
    if entre < 3 and entre > 1:
        print(entre)
"""
#3
"""
lista_50=[i * (10 / 49) for i in range(50)]
print(lista_50)
"""
#4
"""
lista_50=[i * (10 / 49) for i in range(50)]
print(lista_50)

for x in lista_50:
    y=(2*x)-(x*x)
    print(y)
"""
#5
"""
import random
lista_12=[random.randint(1,50) for _ in range(12)]
print(lista_12)
print()

for incremento in range(len(lista_12)):
    if incremento % 2 == 0:
        lista_12[incremento]+=1
print(lista_12)
"""
#6
"""
frase=input("Ingrese una frase: ")
suma=0
for a in frase:
    if a == "a":
        suma+=1
print(f"Su frase tiene {suma} letras A")
"""
#7
"""
lista_diez=[]
for i in range(10):
    diez=int(input("Ingrese número: "))
    lista_diez.append(diez)
print(lista_diez)
print()

suma=0
may=0
men=0
for val in lista_diez:
    suma=suma+val
    if val >= 10:
        may+=1
    else:
        men+=1
promedio=suma/len(lista_diez)

print(f"El promedio de los números es: {promedio}")
print(f"Hay {may} números mayores que 10")
print(f"Hay {men} números menores que 10")
"""
#8
"""
word8=input("Ingrese una palabra: ")

for v in word8:
    if v == "a" or v=="e" or v=="i" or v=="o" or v=="u":
        print(v)
"""
#9
"""
valores_8=[]
for i in range(8):
    valores_user=int(input("Ingrese un número: "))
    valores_8.append(valores_user)

pos=0
for posicion in range(len(valores_8)):
    if posicion % 2==1:
        pos=valores_8[posicion]+pos
print(f"La suma de los valores de posicion impar es: {pos}")
"""

"""
def capitalizar_palabras(texto):
    resultado = ""
    
    for i in range(len(texto)):
        if i == 0 or texto[i - 1] == " ":  # Si es la primera letra o sigue a un espacio
            resultado += texto[i].capitalize()  # Usamos capitalize() en la letra
        else:
            resultado += texto[i]

    return resultado

# Prueba
texto = "hola mundo esto es un test"
print(capitalizar_palabras(texto))  # "Hola Mundo Esto Es Un Test"
"""
"""
file_name = "mi_archivo.txt"                #Creamos el archivo
file = open(file_name, "a")                 #Abrimos el archivo
name = input("Ingrese su nombre: ") 
competidor = input("Competidor: ")
file.write(f"Su nombre es: {name}\n")
file.write(f"El competidor es: {name}\n")
file.close()
"""

import math

def es_primo(n):
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            print(d)
            return d  # n no es primo, devuelve su menor divisor
    print("0")
    return 0  # n es primo

es_primo(3738)