#Definir la clase Nodo y la clase ListaEnlazada
class Nodo:
    """Representa un nodo individual en la lista enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo, None si es el último

class ListaEnlazada:
    """Representa la lista enlazada simple y su cabecera."""
    def __init__(self):
        self.cabeza = None  # Inicialmente, la lista está vacía

    # Función auxiliar para agregar nodos al final (para crear listas de prueba)
    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # Función auxiliar para imprimir la lista (para verificación)
    def imprimir_lista(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")


#1
def contar_nodos(lista):
    """Devuelve la cantidad de nodos en la lista enlazada."""
    contador = 0
    actual = lista.cabeza
    while actual:
        contador += 1
        actual = actual.siguiente
    return contador
"""
# Prueba
lista1 = ListaEnlazada()
lista1.agregar_final(10)
lista1.agregar_final(20)
lista1.agregar_final(30)
lista1.imprimir_lista() # Salida: 10 -> 20 -> 30 -> None
print(f"Cantidad de nodos (Ejercicio 1): {contar_nodos(lista1)}") # Salida: 3
"""

#2
def buscar_posicion_nodo(lista, dato_buscado):
    """Muestra la primera posición (índice base 0) donde se encuentra el dato, o -1 si no se encuentra."""
    actual = lista.cabeza
    posicion = 0
    while actual:
        if actual.dato == dato_buscado:
            return posicion
        actual = actual.siguiente
        posicion += 1
    return -1
"""
# Prueba
lista2 = ListaEnlazada()
lista2.agregar_final('a')
lista2.agregar_final('b')
lista2.agregar_final('c')
lista2.agregar_final('b') # El dato 'b' está en la posición 1 y 3
lista2.imprimir_lista() # Salida: a -> b -> c -> b -> None
dato_a_buscar = 'b'
pos = buscar_posicion_nodo(lista2, dato_a_buscar)
print(f"La posición del dato '{dato_a_buscar}' (Ejercicio 2): {pos}") # Salida: 1
print(f"La posición del dato 'z' (Ejercicio 2): {buscar_posicion_nodo(lista2, 'z')}") # Salida: -1
"""

#3
def eliminar_penultimo(lista):
    """Elimina el penúltimo nodo de la lista enlazada."""
    if lista.cabeza is None or lista.cabeza.siguiente is None:
        print("No se puede eliminar el penúltimo nodo: la lista tiene menos de 2 nodos.")
        return

    # Caso especial: la lista tiene solo 2 nodos (cabeza es el penúltimo)
    if lista.cabeza.siguiente.siguiente is None:
        lista.cabeza = lista.cabeza.siguiente
        return

    # Caso general: la lista tiene 3 o más nodos
    # Usamos 'actual' para encontrar el nodo antepenúltimo
    actual = lista.cabeza
    # El bucle se detiene cuando 'actual' es el antepenúltimo nodo,
    # es decir, cuando actual.siguiente.siguiente es el último nodo (cuyo .siguiente es None)
    while actual.siguiente.siguiente.siguiente:
        actual = actual.siguiente

    # 'actual' es el antepenúltimo. Su siguiente es el penúltimo.
    # Conectamos el antepenúltimo con el último (saltando el penúltimo)
    actual.siguiente = actual.siguiente.siguiente
    print("Penúltimo nodo eliminado.")
"""
# Prueba
lista3 = ListaEnlazada()
lista3.agregar_final(1)
lista3.agregar_final(2)
lista3.agregar_final(3)
lista3.agregar_final(4)
print("Lista original (Ejercicio 3): ", end="")
lista3.imprimir_lista() # Salida: 1 -> 2 -> 3 -> 4 -> None

eliminar_penultimo(lista3)
print("Lista después de eliminar penúltimo (Ejercicio 3): ", end="")
lista3.imprimir_lista() # Salida: 1 -> 2 -> 4 -> None
"""

#4
def lista_solo_impares(lista_original):
    """Crea y devuelve una nueva lista enlazada solo con los números impares de la lista original."""
    nueva_lista = ListaEnlazada()
    actual = lista_original.cabeza
    while actual:
        if isinstance(actual.dato, int) and actual.dato % 2 != 0:
            nueva_lista.agregar_final(actual.dato)
        actual = actual.siguiente
    return nueva_lista
"""
# Prueba
lista4 = ListaEnlazada()
lista4.agregar_final(10)
lista4.agregar_final(5)
lista4.agregar_final(8)
lista4.agregar_final(13)
lista4.agregar_final(1)
print("Lista original (Ejercicio 4): ", end="")
lista4.imprimir_lista() # Salida: 10 -> 5 -> 8 -> 13 -> 1 -> None

lista_impares = lista_solo_impares(lista4)
print("Nueva lista con impares (Ejercicio 4): ", end="")
lista_impares.imprimir_lista() # Salida: 5 -> 13 -> 1 -> None
"""

#5
def dividir_positivos_negativos(lista_original):
    """Divide la lista original en dos nuevas listas: una de positivos y otra de negativos."""
    positivos = ListaEnlazada()
    negativos = ListaEnlazada()
    actual = lista_original.cabeza

    while actual:
        dato = actual.dato
        if isinstance(dato, (int, float)): # Asegurar que es un número
            if dato > 0:
                positivos.agregar_final(dato)
            elif dato < 0:
                negativos.agregar_final(dato)
        actual = actual.siguiente
        
    return positivos, negativos
"""
# Prueba
lista5 = ListaEnlazada()
lista5.agregar_final(5)
lista5.agregar_final(-10)
lista5.agregar_final(0)
lista5.agregar_final(3)
lista5.agregar_final(-2)
print("Lista original (Ejercicio 5): ", end="")
lista5.imprimir_lista() # Salida: 5 -> -10 -> 0 -> 3 -> -2 -> None

positivos, negativos = dividir_positivos_negativos(lista5)
print("Lista de Positivos (Ejercicio 5): ", end="")
positivos.imprimir_lista() # Salida: 5 -> 3 -> None
print("Lista de Negativos (Ejercicio 5): ", end="")
negativos.imprimir_lista() # Salida: -10 -> -2 -> None
"""

#6
VOCALES = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

def eliminar_vocales(lista):
    """Elimina todas las vocales (mayúsculas y minúsculas) de la lista enlazada de caracteres."""
    # 1. Eliminar vocales al inicio (cabeza)
    while lista.cabeza and lista.cabeza.dato in VOCALES:
        lista.cabeza = lista.cabeza.siguiente

    # 2. Eliminar vocales en el resto de la lista
    actual = lista.cabeza
    while actual and actual.siguiente:
        if actual.siguiente.dato in VOCALES:
            # Saltamos el nodo vocal (actual.siguiente)
            actual.siguiente = actual.siguiente.siguiente
            # NO movemos 'actual' ya que el nuevo actual.siguiente también podría ser una vocal
        else:
            actual = actual.siguiente
"""
# Prueba
lista6 = ListaEnlazada()
lista6.agregar_final('e')
lista6.agregar_final('s')
lista6.agregar_final('t')
lista6.agregar_final('r')
lista6.agregar_final('u')
lista6.agregar_final('c')
lista6.agregar_final('t')
lista6.agregar_final('u')
lista6.agregar_final('r')
lista6.agregar_final('a')
print("Lista original (Ejercicio 6): ", end="")
lista6.imprimir_lista() # Salida: e -> s -> t -> r -> u -> c -> t -> u -> r -> a -> None

eliminar_vocales(lista6)
print("Lista sin vocales (Ejercicio 6): ", end="")
lista6.imprimir_lista() # Salida: s -> t -> r -> c -> t -> r -> None
"""

#7
def contar_ocurrencias(lista, dato_buscado):
    """Regresa cuántas veces aparece un dato específico en la lista enlazada."""
    contador = 0
    actual = lista.cabeza
    while actual:
        if actual.dato == dato_buscado:
            contador += 1
        actual = actual.siguiente
    return contador
"""
# Prueba
lista7 = ListaEnlazada()
lista7.agregar_final(1)
lista7.agregar_final(5)
lista7.agregar_final(1)
lista7.agregar_final(8)
lista7.agregar_final(1)
print("Lista original (Ejercicio 7): ", end="")
lista7.imprimir_lista() # Salida: 1 -> 5 -> 1 -> 8 -> 1 -> None

dato_a_contar = 1
veces = contar_ocurrencias(lista7, dato_a_contar)
print(f"El dato {dato_a_contar} aparece {veces} veces (Ejercicio 7).") # Salida: 3
"""