
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    
    print(f"Buscando {objetivo} en {lista}")
    
    while inicio <= fin:
        # 1. Calcular el índice medio
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]
        
        print(f"--- Paso: Rango [{inicio}, {fin}], Medio: {medio} (Valor: {valor_medio}) ---")
        
        # 2. Comparación
        if valor_medio == objetivo:
            return medio  # ¡Elemento encontrado!
        
        elif valor_medio < objetivo:
            # Descartar la mitad inferior (el objetivo está a la derecha)
            inicio = medio + 1
            print("29 es mayor. Nuevo inicio:", inicio)
            
        else: # valor_medio > objetivo
            # Descartar la mitad superior (el objetivo está a la izquierda)
            fin = medio - 1
            print("29 es menor. Nuevo fin:", fin)
            
    return -1

# Datos del ejercicio
temperaturas = [20, 22, 23, 25, 27, 28, 29, 30, 31, 33, 35]
target = 29

# Ejecución
indice_encontrado = busqueda_binaria(temperaturas, target)

# Resultado final
if indice_encontrado != -1:
    print(f"\n La temperatura {target}°C fue encontrada en el índice: {indice_encontrado}")
else:
    print(f"\n La temperatura {target}°C no fue encontrada.")