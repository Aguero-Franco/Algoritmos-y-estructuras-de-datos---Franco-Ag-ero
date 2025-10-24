def buscar_lineal(lista, objetivo):
    """
    Busca el objetivo recorriendo la lista con un contador de índice.
    Es O(n).
    """
    
    print(f"\n--- BÚSQUEDA LINEAL BÁSICA ---")
    
    indice = 0 # Inicializamos el contador en 0
    
    # Mientras el índice no se salga del final de la lista
    while indice < len(lista):
        valor_actual = lista[indice]
        print(f"Revisando índice {indice} (Valor: {valor_actual})")
        
        # Comparamos
        if valor_actual == objetivo:
            print(f"¡Encontrado! El valor {objetivo} está en la posición {indice}.")
            return indice  # Retornamos y salimos
            
        # Movemos al siguiente elemento
        indice = indice + 1
            
    # Si el bucle termina, el elemento no está
    print(f"El valor {objetivo} no fue encontrado.")
    return -1

# Datos de prueba
datos = [40, 10, 30, 50, 20]
target = 50

buscar_lineal(datos, target)






def buscar_binaria(lista_ordenada, objetivo):
    """
    Busca el objetivo dividiendo la lista a la mitad en cada paso.
    Es O(log n) y REQUIERE que la lista esté ORDENADA.
    """
    
    print(f"\n--- BÚSQUEDA BINARIA BÁSICA ---")
    
    inicio = 0
    fin = len(lista_ordenada) - 1
    
    # Mientras el rango de búsqueda sea válido (inicio no haya pasado a fin)
    while inicio <= fin:
        # 1. Encontrar el índice del medio
        medio = (inicio + fin) // 2
        valor_medio = lista_ordenada[medio]
        
        print(f"Rango actual: [{inicio}, {fin}] | Valor medio: {valor_medio}")
        
        # 2. Verificar, Decidir y Ajustar el rango
        if valor_medio == objetivo:
            print(f"¡Encontrado! El valor {objetivo} está en la posición {medio}.")
            return medio
            
        elif valor_medio < objetivo:
            # Descarto la mitad inferior (el objetivo está a la derecha)
            inicio = medio + 1 
            
        else:
            # Descarto la mitad superior (el objetivo está a la izquierda)
            fin = medio - 1

    # Si el bucle termina, el elemento no está
    print(f"El valor {objetivo} no fue encontrado.")
    return -1

# Datos de prueba (DEBE estar ordenada)
datos_ordenados = [10, 20, 30, 40, 50, 60, 70]
target = 20

buscar_binaria(datos_ordenados, target)








def buscar_hashing(datos_set, objetivo):
    """
    Busca el objetivo usando la estructura Set (Hashing).
    Internamente es O(1): una verificación directa sin recorrer nada.
    """
    
    print(f"\n--- BÚSQUEDA POR HASHING ---")
    
    # 1. El 'set' calcula dónde DEBERÍA estar 30 (función hash)
    # 2. El 'set' va directamente a esa ubicación para verificar
    
    # La operación 'in' es la que ejecuta todo el proceso de hashing
    if objetivo in datos_set:
        print(f"La consulta es directa.")
        print(f"¡Encontrado! El valor {objetivo} existe en el conjunto.")
        return True
    else:
        print(f"La consulta es directa.")
        print(f"El valor {objetivo} no fue encontrado.")
        return False

# Datos de prueba: Usamos un 'set' (conjunto)
datos_set = {10, 20, 30, 40, 50}
target_existente = 30
target_inexistente = 99

# Ejecución 1: Elemento existente
buscar_hashing(datos_set, target_existente)

# Ejecución 2: Elemento inexistente
buscar_hashing(datos_set, target_inexistente)