"""
Imaginá que estás vendiendo entradas para diferentes tipos de funciones en un cine.

Descripción:

Tenés una lista de precios según el tipo de entrada.
También tenés una lista con la cantidad de entradas vendidas para cada tipo.
Instrucciones:

El programa debe permitir ingresar desde teclado los datos necesarios para construir dos listas:

1.     Lista de precios por tipo de entrada:

Cada elemento es una tupla con el tipo de entrada y su precio. Por ejemplo:

tipos_entradas = [('general', 8000), ('estudiante', 5000), ('vip', 12000),(‘jubilado’, 3500)]

 2.     Lista de entradas vendidas:

Cada elemento es una tupla con el tipo de entrada y la cantidad vendida. Por ejemplo:

entradas_vendidas = [('general', 3), ('vip', 2), ('jubilado', 1)]

3.     Escribí una función que reciba las dos listas y calcule el total recaudado.

El programa debe calcular el total recaudado multiplicando la cantidad de entradas vendidas por el precio correspondiente de cada tipo de entrada y luego sumar los resultados.
Texto de la respuesta Pregunta 9
"""

"""tipos_entradas = [('general', 8000), ('estudiante', 5000), ('vip', 12000),("jubilado", 3500)]

entradas_vendidas = [('general', 3), ('vip', 2), ('jubilado', 1)]"""


        
        


def entrada(tipo):
    entrada_precio=input("Ingrese el precio: ")
    entrada_cantidad=input("Ingrese la cantidad: ")
    precio=[tipo]
    precio.append(entrada_precio)
    print(precio)
    cantidad=[tipo]
    cantidad.append(entrada_cantidad)
    print(cantidad)
    return precio, cantidad

for i in range(3):
    entrada_tipo=input("Ingrese el tipo de entrada: ")

    if entrada_tipo == "general":
        entrada("general")
    elif entrada_tipo == "vip":
        entrada("vip")
    elif entrada_tipo == "estudiante":
        entrada("estudiante")
    elif entrada_tipo == "jubilado":
        entrada("jubilado")

precio_total=[]



#Como deberia haber sido

def obtener_lista_precios():
    tipos_entradas = []
    print("Ingresá los tipos de entradas y sus precios (escribí 'fin' para terminar):")
    while True:
        tipo = input("Tipo de entrada: ")
        if tipo.lower() == 'fin':
            break
        precio = int(input(f"Precio de '{tipo}': "))
        tipos_entradas.append((tipo, precio))
    return tipos_entradas

def obtener_entradas_vendidas(tipos_entradas):
    entradas_vendidas = []
    print("\nAhora ingresá la cantidad vendida de cada tipo de entrada:")
    for tipo, _ in tipos_entradas:
        cantidad = int(input(f"Cantidad vendida de '{tipo}': "))
        entradas_vendidas.append((tipo, cantidad))
    return entradas_vendidas

def calcular_recaudacion(tipos_entradas, entradas_vendidas):
    precios = dict(tipos_entradas)
    total = sum(precios[tipo] * cantidad for tipo, cantidad in entradas_vendidas)
    return total

# Ejecución del programa
tipos_entradas = obtener_lista_precios()
entradas_vendidas = obtener_entradas_vendidas(tipos_entradas)
total_recaudado = calcular_recaudacion(tipos_entradas, entradas_vendidas)

print(f"\nTotal recaudado: {total_recaudado}")