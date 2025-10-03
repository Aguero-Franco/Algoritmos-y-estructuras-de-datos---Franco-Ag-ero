#1
vector1=[]
for element in range(5):
    five_numbers = input("Ingresá un número: ")
    for element in five_numbers:
        vector1.append(five_numbers)
print(vector1)

#2
vector2=[]
for element in range(5):
    vector_numbers = input("Ingresá un número: ")
    for element in vector_numbers:
        vector2.insert(0,vector_numbers)
print(vector2)

#3
import random
num_aleatorios = [random.randint(5, 30) for _ in range(20)]
print(num_aleatorios)
num_user=int(input("Ingrese un número entre 5 y 30: "))
if num_user in num_aleatorios:
    print(f"El número {num_user} está entre los números aleatorios")
else:
    print("El número no está en los aleatorios")

#4
vector_names=[]
while True:
    names=input("Ingrese nombres y zzz para terminar: ")
    vector_names.append(names)
    if "zzz" in names:
        vector_names.pop(-1)
        break
print(vector_names)

#5
vector_20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
posicion_X=int(input("Posición X: "))
posicion_Y=int(input("Posición Y: "))
if 1 <= posicion_X <= 20 and 1 <= posicion_Y <= 20 and posicion_X <= posicion_Y:
    print(f"El vector queda: {vector_20[posicion_X - 1:posicion_Y]}")
else:
    print("Los números nos están en el rango 1,20 o X < Y")

#6
import random
vector_30=[random.randint(1,100) for _ in range(30)]
print(vector_30)

valueX=int(input("Ingrese el valor X (entre 1 y 30): "))
valueY=int(input("Ingrese el valor Y (entre 1 y 30): "))

if 1<=valueX<=30 and 1<=valueY<=30:
    vector_30[valueX], vector_30[valueY] = vector_30[valueY], vector_30[valueX]
    print(vector_30)
else:
    print("Los valores ingresados no están entre 1 y 30")

#7
import random
vector_18=[random.randint(1,50) for _ in range(18)]
print(vector_18)

add=0
for sumatoria in vector_18:
    add=add+sumatoria
print(add)

#8
import random
vector_18=[random.randint(1,50) for _ in range(18)]
print(vector_18)

add=0
for sumatoria in vector_18:
    add=add+sumatoria
promedio=add/len(vector_18)
print(add)
print(promedio)

#9
import random
vector_18=[random.randint(1,50) for _ in range(18)]
print(vector_18)

add=0
for sumatoria in vector_18:
    add=add+sumatoria
promedio=add/len(vector_18)

print(add)
print(promedio)

vector_18.sort()
print(f"El menor valor es: {vector_18[0]}, y el mayor es: {vector_18[-1]}")

#10
import random
butacas=[random.choice([True, False]) for _ in range(20)]
print(butacas)

desocupadas=0
for butaca in butacas:
    if butaca == False:
        desocupadas+=1
print(f"La cantidad de butacas libres es: {desocupadas}")

#11
notas=[33, 11, 20, 2, 15, 1, 12, 11, 8, 14, 10]
print(f"Las notas cargadas: {notas}")

notas.sort()
print(f"La nota más baja es: {notas[0]}")
notas.pop(0)

promedio_notas=sum(notas)/len(notas)
print(f"El promedio de las notas (sin la nota mas baja) es: {promedio_notas}")

#12
import random

matrix_12=[]

for i in range(4):
    filas=[]
    for j in range(3):
        filas.append(random.randint(1,10))
    matrix_12.append(filas)
    print(matrix_12[i])

#13
import random

matrix13=[[random.randint(1,10) for _ in range(4)] for _ in range(5)]

for i in matrix13:
    print(i)

print(" ")

for j in range(4):
    columna = [matrix13 [i][j] for i in range(5)]
    print(columna)

#14
import random

matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(4)]

print("Matriz:")
for fila in matriz:
    print(fila)

print("Suma de cada fila:")
for i in range(len(matriz)):  
    print(f"Fila {i + 1}: {sum(matriz[i])}")


print("Suma de cada columna:")
for j in range(3):
    suma_columna = sum(matriz[i][j] for i in range(4))
    print(f"Columna {j + 1}: {suma_columna}")

#15
import random

a = [[random.randint(1, 10) for _ in range(3)] for _ in range(4)]

print("Matriz:")
for fila in a:
    print(fila)

print("Suma de filas:")
b=[sum(fila) for fila in a]
print(b)

print("Suma de columnas:")
c=[sum(a[i][j] for i in range(4)) for j in range(3)]
print(c)

#16
import random

matrix16 = [[random.randint(1, 6) for _ in range(6)] for _ in range(5)]
print(matrix16)

matrix16[4]=[0, 0, 0, 0, 0, 0]
print(matrix16)