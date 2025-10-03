#1
"""
file_words="palabras.txt"

with open("palabras.txt", "a+") as archivo:
    while True:
        palabra = input("Ingresá una palabra (o escribí 'salir' para terminar): ")
        if palabra.lower() == "salir":
            break
        archivo.write(palabra + "\n")

with open("palabras.txt", "r") as archivo:
    palabras = archivo.readlines()

print("\nPalabras guardadas:")
for palabra in palabras:
    print(palabra.strip())
print(f"\nTotal de líneas en el archivo: {len(palabras)}")
"""
#2
"""
with open("numeros.txt", "w") as archivo:
    for i in range(1, 11):
        archivo.write(f"{i}\n")

print("Archivo numeros.txt generado")
"""
#3
"""
with open("colores.txt", "w") as archivo:
    for i in range(5):
        color = input(f"Ingrese el color {i + 1}: ")
        archivo.write(color + "\n")

print("Los colores han sido guardados en colores.txt.")
"""
#4
"""
import random

with open("numeros.txt", "w") as archivo:
    for _ in range(20):
        archivo.write(f"{random.randint(1, 10)}\n")

contador = 0
with open("numeros.txt", "r") as archivo:
    for linea in archivo:
        if linea.strip() == "5":
            contador += 1

print(f"Cantidad de números iguales a 5 en el archivo: {contador}")
"""
#5
"""
import random

with open("numeros.txt", "w") as archivo:
    for _ in range(20):
        archivo.write(f"{random.randint(1, 100)}\n")

numeros = []
with open("numeros.txt", "r") as archivo:
    for linea in archivo:
        numeros.append(int(linea.strip()))

suma_total = sum(numeros)
promedio = suma_total / len(numeros) if numeros else 0

print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio}")
"""
#6
"""
import random 

def crear_archivo_numeros_azar(nombre_archivo): 
    try:
        with open(nombre_archivo, 'w') as archivo:
            for _ in range(250): 
                numero_azar = random.randint(1, 100) 
                archivo.write(f"{numero_azar}\n") 
        print(f"Archivo '{nombre_archivo}' creado exitosamente con 250 números al azar.")

def ejercicio6():
    nombre_archivo = input("Introduce el nombre para el nuevo archivo con números al azar: ") 
    crear_archivo_numeros_azar(nombre_archivo) 
"""