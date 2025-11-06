#1
import random

# 1. Generar la lista de 10 números aleatorios entre 1 y 100
lista_numeros = [random.randint(1, 100) for _ in range(10)]
print(f"La lista generada es: {lista_numeros}")

# 2. Pedir el número al usuario
try:
    numero_buscar = int(input("Ingresa un número entero para buscar: "))
except ValueError:
    print("Entrada inválida. Debe ser un número entero.")
else:
    # 3. Determinar si se encuentra y en qué posición (Búsqueda Lineal)
    posiciones = []
    for indice, valor in enumerate(lista_numeros):
        if valor == numero_buscar:
            posiciones.append(indice)
    
    if posiciones:
        print(f"El número {numero_buscar} SÍ se encuentra en la lista.")
        # Se muestra la primera posición si solo se pide una, pero se recolectaron todas
        print(f"Se encontró por primera vez en la posición: {posiciones[0]}") 
    else:
        print(f"El número {numero_buscar} NO se encuentra en la lista.")

#2
lista_alumnos = ["Ana Pérez", "Juan Gómez", "María López", "Carlos Ruiz", "Sofía Torres"]
print(f"Lista de alumnos que rindieron: {lista_alumnos}")

# 1. Pedir el nombre a buscar (se recomienda estandarizar la entrada)
nombre_buscar = input("Ingresa el nombre del alumno para buscar (ej: Juan Gómez): ").strip()

# 2. Determinar si se presentó (Búsqueda Lineal)
se_presento = False
posicion = -1

# Usando un bucle simple
for i in range(len(lista_alumnos)):
    if lista_alumnos[i] == nombre_buscar:
        se_presento = True
        posicion = i # Se guarda la posición si se encuentra
        break

if se_presento:
    print(f"El alumno '{nombre_buscar}' SÍ se presentó a rendir (Posición {posicion}).")
else:
    print(f"El alumno '{nombre_buscar}' NO se presentó a rendir.")

#3
def busqueda_lineal_multiples(lista, valor_buscar):
    """Devuelve una lista con todas las posiciones del valor o [-1] si no se encuentra."""
    posiciones = []
    for i, elemento in enumerate(lista):
        if elemento == valor_buscar:
            posiciones.append(i)
    
    # Si la lista de posiciones NO está vacía, devuelve las posiciones,
    # sino, devuelve la lista con [-1]
    return posiciones if posiciones else [-1]

# Ejemplo de uso
lista_ejemplo = [10, 25, 50, 25, 100, 25, 75, 10]
valor_existente = 25
valor_inexistente = 99

resultado_existente = busqueda_lineal_multiples(lista_ejemplo, valor_existente)
resultado_inexistente = busqueda_lineal_multiples(lista_ejemplo, valor_inexistente)

print(f"Lista: {lista_ejemplo}")
print(f"Resultado para {valor_existente}: {resultado_existente}") 
print(f"Resultado para {valor_inexistente}: {resultado_inexistente}")

#4
def juego_adivinar_computadora():
    """Juego donde la computadora adivina un número usando la lógica de Búsqueda Binaria."""
    print("--- Juego de Adivinación ---")

    # 1. Pedir los límites del intervalo [a, b]
    while True:
        try:
            a = int(input("Ingresa el límite inferior (a): "))
            b = int(input("Ingresa el límite superior (b, debe ser > a): "))
            if a < b:
                break
            else:
                print("El límite inferior 'a' debe ser menor que el superior 'b'.")
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar números enteros.")

    print(f"\n¡Piensa en un número entero dentro del intervalo [{a}, {b}]!")
    input("Pulsa Enter cuando lo hayas pensado...")

    # Variables de control para la búsqueda binaria
    min_val = a
    max_val = b
    intentos = 0
    encontrado = False

    # Búsqueda Binaria para adivinar
    while min_val <= max_val:
        intentos += 1
        
        # Calcular la adivinanza (el punto medio del intervalo)
        adivinanza = (min_val + max_val) // 2
        
        print(f"\n--- Intento #{intentos} ---")
        respuesta = input(f"Mi adivinanza es: {adivinanza}. ¿Es 'mayor', 'menor' o 'igual' (o 'salir')?: ").lower().strip()

        if respuesta == 'salir':
            print("El juego ha terminado por ingreso de 'salir'.")
            return
        elif respuesta == 'igual':
            print(f"¡ACERTÉ! El número es {adivinanza}. Lo adiviné en {intentos} intentos.")
            encontrado = True
            break
        elif respuesta == 'mayor':
            # El número pensado es mayor que la adivinanza, se descarta la mitad inferior
            min_val = adivinanza + 1
        elif respuesta == 'menor':
            # El número pensado es menor que la adivinanza, se descarta la mitad superior
            max_val = adivinanza - 1
        else:
            print("Respuesta inválida. Por favor, solo responde 'mayor', 'menor', 'igual' o 'salir'.")
    
    if not encontrado and min_val > max_val:
        # Esto sucede si el usuario miente o si el número estaba fuera del rango inicial
        print("\nHubo una inconsistencia. Parece que el número que pensaste no está en el rango inicial, o me has dado una indicación incorrecta.")

# Llamada a la función para ejecutar el juego
juego_adivinar_computadora()