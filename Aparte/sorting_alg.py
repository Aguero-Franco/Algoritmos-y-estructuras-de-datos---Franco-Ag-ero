"""
Ordenamiento por Inserción (Insertion Sort)
"""
def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1, n):                       #Empieza en el segundo elemento porque siempre se considera que el primero es una sublista ordenada
        
        clave = arr[i]                          #Guardamos el valor actual, que es el elemento que vamos a insertar en la sublista ordenada
        
        j = i - 1                               #El puntero arranca a la izquierda de la ´clave´, marcando el último elemento de la sublista ordenada
        
        while j >= 0 and clave < arr[j]:        #Mientras la clave sea menor que el elemento a su izquierda, realizamos el desplazamiento
            
            arr[j + 1] = arr[j]                 #Se desplaza el elemento mayor una posición hacia la derecha
            j -= 1
        
        arr[j + 1] = clave                      #Cuando el bucle while termina, significa que encontramos la posición correcta e insertamos la clave en el hueco
        
    return arr

# --- Ejemplo de Uso ---
print("--- Insertion Sort ---")
lista_simple = [8, 3, 1, 6, 4]
print("Original:", lista_simple)
insertion_sort(lista_simple)
print("Ordenada:", lista_simple)
# Salida: Ordenada: [1, 3, 4, 6, 8]





"""
    Ordenamiento por Mezcla (Merge Sort)
"""
def merge_sort(arr):

    if len(arr) <= 1:                           #Es por si la lista tiene 0 o 1 elemento, ya está ordenada
        return arr

    medio = len(arr) // 2                       #Encontramos el punto medio y dividimos el arreglo en dos mitades
    
    izquierda = merge_sort(arr[:medio])         #La función se llama a sí misma para ordenar la mitad izquierda y la derecha, repitiendo hasta llegar al caso base
    derecha = merge_sort(arr[medio:])

    return merge(izquierda, derecha)            #Cuando las mitades vuelven a la recursión ya ordenadas, se llama a la función merge para combinarlas

"""
Función auxiliar para fusionar dos listas ordenadas en una sola.
"""
def merge(izquierda, derecha):                  #Toma dos listas ordenadas y usa dos punteros para comparar sus elementos y mover el menor a la lista ´resultado´
    
    resultado = []
    i = j = 0                                   #Punteros para cada sublista

    while i < len(izquierda) and j < len(derecha): 
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])             #Después de que una lista se vacía, agregamos los elementos restantes de la otra lista, ya ordenados
    resultado.extend(derecha[j:])
    
    return resultado


# --- Ejemplo de Uso ---
print("\n--- Merge Sort ---")
lista_compleja = [12, 11, 13, 5, 6, 7]
print("Original:", lista_compleja)
lista_ordenada = merge_sort(lista_compleja)
print("Ordenada:", lista_ordenada)
# Salida: Ordenada: [5, 6, 7, 11, 12, 13]





"""
Ejercicio para usar Insertion sort
"""
def insertar_nueva_puntuacion(top_canciones, nueva_puntuacion):
    
    top_canciones.append(nueva_puntuacion)                                                  #Agregamos el elemento al final del array
    
    i = len(top_canciones) - 1                                                              #El índice ´i´ apunta al elemento que acabamos de agregar
    
    j = i - 1
    
    while j >= 0 and top_canciones[j] < top_canciones[j + 1]:                               #El bucle compara el elemento actual con el de la izquierda,
                                                                                            #si el elemento de la izquierda es menor, realiza el intercambio
        
        top_canciones[j], top_canciones[j + 1] = top_canciones[j + 1], top_canciones[j]     #Realiza el intercambio (swap)
        
        j -= 1                                                                              #Mueve el puntero hacia la izquierda
        
    return top_canciones[:5]                                                                #Devolvemos el array pero solo con las primeras 5 posiciones

# --- Ejecución del Ejercicio ---
top_inicial = [95, 88, 75, 62, 59]
nueva = 80

print("\n--- Ejercicio: Top de Canciones ---")
print(f"Top 5 Inicial: {top_inicial}")
print(f"Nueva Puntuación a Insertar: {nueva}")

# Llamar a la función
top_actualizado = insertar_nueva_puntuacion(top_inicial, nueva)
print(f"Top 5 Actualizado: {top_actualizado}")
# Salida Esperada: Top 5 Actualizado: [95, 88, 80, 75, 62]
print("\n")