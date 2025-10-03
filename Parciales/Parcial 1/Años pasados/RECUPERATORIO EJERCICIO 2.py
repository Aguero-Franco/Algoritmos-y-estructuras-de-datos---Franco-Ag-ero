#Crear un programa que genere 20 (veinte) números aleatorios entre 1 y 10 y los guarde en
#una matriz de 5 x 4. 

#Posteriormente debe recorrer la matriz y guardar cada número de la matriz en un archivo 
#llamado numeros.txt (uno por línea). 

#Luego, solicite al usuario los valores de M y N para crear una nueva matriz MxN,
# la cual debe ser completada con los números almacenados en el archivo (es decir, 
#se debe cumplir que NxM >= 20).

#Mostrar por partalla la nueva matriz. En caso de que necesite más números para 
#completarla, hacerlo con ceros.

import random

matriz54=[[random.randint(1,10) for _ in range(4)]for _ in range(5)]

numeros=[]

for i in matriz54:
    print(i)
    for j in i:
        numeros.append(j)
print(numeros)

def nueva_matriz(m, n):
    import random
    matrix_nm=[[random.randint(1,10)]]









































"""import random
print("MATRIZ GENERADA 5X3:")
matriz= []
for i in range (5):
    fila=[]
    for j in range(4):
        fila.append(random.randint(1,10))
    matriz.append(fila.copy())
    
for matriz_generada in matriz:
    print(matriz_generada)
    
with open("numeros.txt", "w") as file:
    for fila in matriz:
        for numero in fila:
            file.write(f"{numero}\n")

while True:
    n = int(input("Ingrese el número de filas (n): "))
    m = int(input("Ingrese el número de columnas (m): "))
    if n*m >=20:
        break
    else:
        print("ERROR= n*m=<20")
        print("INGRESAR NUEVAMENTE N Y M")
                    
numeros=[]
with open("numeros.txt","r")as file:
    for linea in file:
        numeros.append(linea.strip())
        
n_matriz=[]
contador=0
for i in range(m):
    fila=[]
    for j in range(n):
        if contador<len(numeros):
            fila.append(numeros[contador])
            contador+=1
        else:
            fila.append(0)
    n_matriz.append(fila)

for fila in n_matriz:
    print(fila)"""