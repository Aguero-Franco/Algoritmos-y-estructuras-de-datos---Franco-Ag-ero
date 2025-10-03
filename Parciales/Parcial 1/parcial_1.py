"""
Dada una matriz de 6x5 con números enteros mayores a 50 generados de manera aleatoria, 
crea una función que retorne una matriz que tenga una columna más (6x6), 
con los valores originales de la matriz ingresada y en la columna extra, 
coloque la suma de los números de cada fila.
"""

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