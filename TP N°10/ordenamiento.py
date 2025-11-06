#1
def insertion_sort(arr):
    # Recorremos el array desde el segundo elemento (índice 1)
    for i in range(1, len(arr)):
        # Guardamos el valor actual a insertar en su posición correcta
        key = arr[i]
        j = i - 1
        
        # Movemos los elementos del array mayores que 'key' una posición adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertamos 'key' en su posición correcta
        arr[j + 1] = key
    return arr

numeros = [76, 21, 34, 68, 31, 27, 53]
print(f"Números originales: {numeros}")
numeros_ordenados = insertion_sort(numeros)
print(f"Números ordenados por Inserción: {numeros_ordenados}")

#2
def selection_sort(arr):
    # Recorremos todo el array
    for i in range(len(arr)):
        # Asumimos que el elemento actual es el mínimo
        min_idx = i
        
        # Buscamos el elemento mínimo en el resto del array sin ordenar
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Intercambiamos el elemento mínimo encontrado con el elemento actual (arr[i])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numeros = [6, 2, 4, 8, 3, 7, 5]
print(f"Números originales: {numeros}")
numeros_ordenados = selection_sort(numeros)
print(f"Números ordenados por Selección: {numeros_ordenados}")

#3
def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos del array
    for i in range(n):
        # El último i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Recorrer el array de 0 a n-i-1. Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Reutilizamos insertion_sort y selection_sort de los ejercicios 1 y 2

# Función para obtener los números del usuario
def obtener_numeros_usuario():
    numeros = []
    print("Ingrese 6 números enteros:")
    for i in range(6):
        while True:
            try:
                num = int(input(f"Número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return numeros

# Obtener los números
# Solo se pedirá una vez, luego se copiará la lista para ordenar con cada método
numeros_originales = obtener_numeros_usuario()
print(f"\nNúmeros ingresados: {numeros_originales}")

# Ordenar con cada método
# Se usa list.copy() para que cada método ordene una copia, manteniendo el original para el siguiente
print("\n--- Ordenación por Selección ---")
lista_sel = selection_sort(numeros_originales.copy())
print(f"Números ordenados: {lista_sel}")

print("\n--- Ordenación por Inserción ---")
lista_ins = insertion_sort(numeros_originales.copy())
print(f"Números ordenados: {lista_ins}")

print("\n--- Ordenación por Burbuja ---")
lista_bur = bubble_sort(numeros_originales.copy())
print(f"Números ordenados: {lista_bur}")

#4
import random

def generar_archivo_numeros(filename="nros.txt", count=50):
    """Genera un archivo con 50 números aleatorios (1-100) en líneas separadas."""
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(str(random.randint(1, 100)) + '\n')
    print(f"Se ha generado el archivo '{filename}' con {count} números.")

# La función insertion_sort ya está definida en el Ejercicio 1

def ordenar_archivo(input_filename="nros.txt", output_filename="ordenado.txt"):
    try:
        # 1. Leer los números del archivo
        with open(input_filename, 'r') as f:
            # Leer todas las líneas, eliminar espacios en blanco y convertir a enteros
            numeros_str = [linea.strip() for linea in f if linea.strip()]
            numeros = [int(num) for num in numeros_str]
            
        # 2. Ordenar la lista de números (usamos Insertion Sort)
        numeros_ordenados = insertion_sort(numeros)
        
        # 3. Guardar los números ordenados en el nuevo archivo
        with open(output_filename, 'w') as f:
            for num in numeros_ordenados:
                f.write(str(num) + '\n')
                
        print(f"Números leídos ({len(numeros)}) y ordenados guardados en '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: El archivo '{input_filename}' no fue encontrado. Ejecute la generación del archivo primero.")
    except ValueError:
        print("Error: El archivo contiene datos que no son números enteros.")

# Ejecución
generar_archivo_numeros()
ordenar_archivo()

#5
import array

# Reutilizamos la función insertion_sort (funciona con listas de Python)

def insertion_sort_array(arr_obj):
    """Implementación de Insertion Sort para un objeto array.array de Python."""
    n = len(arr_obj)
    # Los objetos array.array soportan la mayoría de las operaciones de lista (incluida la asignación por índice)
    for i in range(1, n):
        key = arr_obj[i]
        j = i - 1
        
        while j >= 0 and key < arr_obj[j]:
            arr_obj[j + 1] = arr_obj[j]
            j -= 1
        
        arr_obj[j + 1] = key
    return arr_obj

# Datos de prueba
datos_lista = [5, 2, 4, 6, 1, 3]
datos_array = array.array('i', datos_lista) # 'i' para enteros (int)

# Ordenar la lista
lista_ordenada = insertion_sort(datos_lista.copy()) # Usa .copy() para no modificar la lista original
print(f"Lista original: {datos_lista}")
print(f"Lista ordenada (list): {lista_ordenada}")

# Ordenar el objeto array.array
array_ordenado = insertion_sort_array(datos_array)
print(f"Array original: {list(datos_array)}") # Convertimos a list para mostrar
print(f"Array ordenado (array.array): {list(array_ordenado)}")

print("\n--- ¿Diferencias? ¿En qué? ---")
print("> Diferencias Notadas:")
print("1. Inicialización")
print("2. Eficiencia y Uso de Memoria")
print("3. Sintaxis")

#6
import random

# Reutilizamos bubble_sort, selection_sort, y insertion_sort

# 1. Generar el arreglo de 10 números al azar
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print(f"Arreglo aleatorio original: {numeros_aleatorios}")

# 2. Ordenar con los tres métodos (usando copias)

print("\n--- Ordenación por Burbuja (Bubble Sort) ---")
lista_bur = bubble_sort(numeros_aleatorios.copy())
print(f"Resultado: {lista_bur}")

print("\n--- Ordenación por Selección (Selection Sort) ---")
lista_sel = selection_sort(numeros_aleatorios.copy())
print(f"Resultado: {lista_sel}")

print("\n--- Ordenación por Inserción (Insertion Sort) ---")
lista_ins = insertion_sort(numeros_aleatorios.copy())
print(f"Resultado: {lista_ins}")

#7
# Reutilizamos insertion_sort y bubble_sort

def obtener_precios_usuario():
    precios = []
    print("Ingrese 10 precios de golosinas:")
    for i in range(10):
        while True:
            try:
                # Se usa float para precios, ya que pueden tener decimales
                precio = float(input(f"Precio {i + 1}: "))
                precios.append(precio)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un precio válido (número).")
    return precios

# Obtener los precios
precios_originales = obtener_precios_usuario()
print(f"\nPrecios ingresados: {precios_originales}")

# Ordenar con los dos métodos (usando copias)
print("\n--- Ordenación por Inserción ---")
precios_ins = insertion_sort(precios_originales.copy())
print(f"Precios ordenados: {precios_ins}")

print("\n--- Ordenación por Burbuja ---")
precios_bur = bubble_sort(precios_originales.copy())
print(f"Precios ordenados: {precios_bur}")

#8
import random
import array

# Reutilizamos selection_sort y insertion_sort

# 1. Generar la lista y el array
numeros_aleatorios = [random.randint(1, 50) for _ in range(6)]
lista_numeros = numeros_aleatorios.copy()
# Usamos array.array para el array de 1 dimensión
array_numeros = array.array('i', numeros_aleatorios) 

print(f"Lista original: {lista_numeros}")
print(f"Array original: {list(array_numeros)}")

# 2. Ordenar la Lista con Selection Sort
print("\n--- Lista ordenada con Selection Sort ---")
lista_ordenada = selection_sort(lista_numeros)
print(f"Resultado: {lista_ordenada}")

# 3. Ordenar el Array con Insertion Sort
print("\n--- Array ordenado con Insertion Sort ---")
# Usamos insertion_sort_array del Ejercicio 5
array_ordenado = insertion_sort_array(array_numeros)
print(f"Resultado: {list(array_ordenado)}")

#9
import random

# Reutilizamos insertion_sort

def generar_matriz_aleatoria(filas, columnas):
    """Genera una matriz (lista de listas) con números aleatorios."""
    matriz = []
    for _ in range(filas):
        fila = [random.randint(0, 100) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def ordenar_filas_matriz(matriz):
    """Ordena cada fila de la matriz usando Insertion Sort."""
    matriz_ordenada = []
    for fila in matriz:
        # insertion_sort ordena la lista en su lugar, se usa .copy()
        fila_ordenada = insertion_sort(fila.copy())
        matriz_ordenada.append(fila_ordenada)
    return matriz_ordenada

# 1. Generar la matriz 4x6
FILAS = 4
COLUMNAS = 6
matriz_original = generar_matriz_aleatoria(FILAS, COLUMNAS)

print("--- Matriz Original (4x6) ---")
for fila in matriz_original:
    print(fila)

# 2. Ordenar la matriz por filas
matriz_ordenada = ordenar_filas_matriz(matriz_original)

print("\n--- Matriz Ordenada por Filas ---")
for fila in matriz_ordenada:
    print(fila)

#10
# Datos de ejemplo para pacientes.txt (según la fuente)
DATOS_PACIENTES = """Sanchez, Luis, 64, OSDE
Balaz, Sara, 32, OSECAD
Lipa, Julieta, 27, OSDE
Perez, Lucila, 30, OSECAD"""

def generar_archivo_pacientes(filename="pacientes.txt", data=DATOS_PACIENTES):
    """Genera el archivo pacientes.txt con los datos de ejemplo."""
    with open(filename, 'w') as f:
        f.write(data)
    print(f"Se ha generado el archivo '{filename}'.")

def parse_paciente(linea):
    """Convierte una línea de texto a un diccionario de paciente."""
    partes = [p.strip() for p in linea.split(',')]
    if len(partes) == 4:
        try:
            return {
                'apellido': partes[0],
                'nombre': partes[1],
                'edad': int(partes[2]),
                'obra_social': partes[3]
            }
        except ValueError:
            return None # Ignorar líneas con edad no numérica
    return None

def bubble_sort_pacientes_por_edad(pacientes):
    """Ordena la lista de diccionarios (pacientes) por el campo 'edad'."""
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparar y ordenar por edad
            if pacientes[j]['edad'] > pacientes[j + 1]['edad']:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    return pacientes

def procesar_pacientes(input_filename="pacientes.txt", output_filename="pacientes_por_edad.txt"):
    try:
        # 1. Leer y parsear los datos del archivo
        with open(input_filename, 'r') as f:
            lineas = f.readlines()
            pacientes = [parse_paciente(linea) for linea in lineas]
            # Filtrar los pacientes que se pudieron parsear correctamente
            pacientes = [p for p in pacientes if p is not None]
        
        # 2. Ordenar la lista de pacientes por edad
        pacientes_ordenados = bubble_sort_pacientes_por_edad(pacientes)
        
        # 3. Mostrar los datos ordenados
        print("--- Pacientes Ordenados por Edad ---")
        for p in pacientes_ordenados:
            print(f"Apellido: {p['apellido']}, Nombre: {p['nombre']}, Edad: {p['edad']}, Obra Social: {p['obra_social']}")
            
        # 4. Guardar los datos ordenados en el nuevo archivo
        with open(output_filename, 'w') as f:
            for p in pacientes_ordenados:
                linea = f"{p['apellido']}, {p['nombre']}, {p['edad']}, {p['obra_social']}\n"
                f.write(linea)
                
        print(f"\nDatos ordenados guardados en '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: El archivo '{input_filename}' no fue encontrado. Ejecute la generación del archivo primero.")

# Ejecución
generar_archivo_pacientes()
procesar_pacientes()

#11
def obtener_notas_usuario():
    notas = []
    print("Ingrese 10 notas de examen (0 a 10):")
    for i in range(10):
        while True:
            try:
                nota = float(input(f"Nota {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Por favor, ingrese una nota entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    return notas

def encontrar_mejor_y_peor_nota(notas):
    if not notas:
        return None, None
        
    # Inicializar con el primer elemento
    mejor_nota = notas[0]
    peor_nota = notas[0]
    
    # Recorrer la lista desde el segundo elemento
    for nota in notas[1:]:
        if nota > mejor_nota:
            mejor_nota = nota
        if nota < peor_nota:
            peor_nota = nota
            
    return mejor_nota, peor_nota

# Obtener las notas
notas = obtener_notas_usuario()
mejor, peor = encontrar_mejor_y_peor_nota(notas)

print(f"\nNotas ingresadas: {notas}")
print(f"La **Mejor Nota** (máximo) es: {mejor}")
print(f"La **Peor Nota** (mínimo) es: {peor}")

#12
# Lista de ejemplo (se pueden cambiar a 10 nombres o más)
nombres = ["Gandalf", "Sam", "Frodo", "Sauron", "Gollum", "Aragorn", "Boromir", "Pippin", "Merry", "Legolas"]
print(f"Nombres desordenados: {nombres}")

def insertion_sort_por_longitud(arr):
    """Ordena una lista de strings basándose en la longitud de cada string."""
    for i in range(1, len(arr)):
        key = arr[i]
        key_longitud = len(key)
        j = i - 1
        
        # Mover los elementos cuya longitud es mayor que la longitud de 'key'
        while j >= 0 and key_longitud < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr

nombres_ordenados = insertion_sort_por_longitud(nombres.copy())
print(f"Nombres ordenados por longitud: {nombres_ordenados}")

#13
import time
import random

# Reutilizamos insertion_sort, selection_sort, y bubble_sort

def medir_tiempo(algoritmo, datos):
    """Mide el tiempo de ejecución de un algoritmo de ordenación."""
    # Hacer una copia para que el algoritmo trabaje sobre datos_copia
    datos_copia = datos.copy()
    
    start_time = time.time()
    algoritmo(datos_copia)
    end_time = time.time()
    
    return end_time - start_time

# 1. Lista Pequeña (10 números)
LISTA_PEQUENA_SIZE = 10
lista_pequena = [random.randint(1, 1000) for _ in range(LISTA_PEQUENA_SIZE)]

print(f"--- Medición para Lista Pequeña ({LISTA_PEQUENA_SIZE} números) ---")

tiempo_ins_peq = medir_tiempo(insertion_sort, lista_pequena)
print(f"Insertion Sort: {tiempo_ins_peq:.6f} segundos")

tiempo_sel_peq = medir_tiempo(selection_sort, lista_pequena)
print(f"Selection Sort: {tiempo_sel_peq:.6f} segundos")

tiempo_bur_peq = medir_tiempo(bubble_sort, lista_pequena)
print(f"Bubble Sort: {tiempo_bur_peq:.6f} segundos")

# 2. Lista Grande (6 millones de números)
# Nota: La ordenación de 6 millones de elementos con estos algoritmos O(n^2) es EXTREMADAMENTE lenta.
# Para el ejemplo, usaremos un tamaño más manejable que demuestre la diferencia, por ejemplo 15,000,
# y luego se dará la conclusión teórica basada en la complejidad O(n^2).
LISTA_GRANDE_SIZE = 15000 
# LISTA_GRANDE_SIZE = 6000000 # Advertencia: Descomentar si el tiempo de ejecución no es crítico.

print(f"\n--- Medición para Lista Grande ({LISTA_GRANDE_SIZE} números) ---")

lista_grande = [random.randint(1, 100000) for _ in range(LISTA_GRANDE_SIZE)]

# En el mundo real, para O(n^2) con 6 millones:
# Bubble/Selection/Insertion Sort tardarían HORAS o incluso DÍAS.
# Por eso, la conclusión se basa en la complejidad algorítmica.

# Para el ejemplo de 15,000 elementos:
tiempo_ins_gra = medir_tiempo(insertion_sort, lista_grande)
print(f"Insertion Sort: {tiempo_ins_gra:.4f} segundos")

tiempo_sel_gra = medir_tiempo(selection_sort, lista_grande)
print(f"Selection Sort: {tiempo_sel_gra:.4f} segundos")

tiempo_bur_gra = medir_tiempo(bubble_sort, lista_grande)
print(f"Bubble Sort: {tiempo_bur_gra:.4f} segundos")


print("\n--- Conclusión (Algoritmos O(n^2)) ---")
print("Para una lista pequeña (10 números), la diferencia de tiempo es mínima y casi insignificante")
print("Para una lista grande (6 millones de números, basado en la complejidad O(n^2))")
print("Tardan más (más lentos)")
print("Serían más rápidos")