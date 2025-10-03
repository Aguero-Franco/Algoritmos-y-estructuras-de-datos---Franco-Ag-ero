#Ejemplo de uso de las listas enlazadas

#Clase que representa un nodo individual en la lista enlazada.
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

#Clase que maneja las operaciones de la lista enlazada.
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        #Agrega un nuevo nodo al final de la lista.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        print(f"'{value}' ha sido agregado a la lista.")

    def delete(self, value_to_delete):
        #Elimina el primer nodo que coincida con el valor dado.
        if self.head is None:
            print("La lista está vacía, no se puede eliminar.")
            return

        #Caso 1: El nodo a eliminar es el primero (head)
        if self.head.value == value_to_delete:
            self.head = self.head.next_node
            print(f"'{value_to_delete}' ha sido eliminado.")
            return

        #Caso 2: El nodo a eliminar está en algún otro lugar de la lista
        current_node = self.head
        while current_node.next_node and current_node.next_node.value != value_to_delete:
            current_node = current_node.next_node

        if current_node.next_node is None:
            print(f"'{value_to_delete}' no se encontró en la lista.")
        else:
            current_node.next_node = current_node.next_node.next_node
            print(f"'{value_to_delete}' ha sido eliminado.")

    def search(self, value_to_find):
        #Busca un valor en la lista y retorna True si lo encuentra, de lo contrario False.
        current_node = self.head
        while current_node:
            if current_node.value == value_to_find:
                print(f"'{value_to_find}' se encontró en la lista.")
                return True
            current_node = current_node.next_node
        print(f"'{value_to_find}' no se encontró en la lista.")
        return False

    def print_list(self):
        #Imprime todos los valores de la lista en orden.
        if self.head is None:
            print("La lista está vacía.")
            return

        current_node = self.head
        print("Contenido de la lista enlazada:")
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next_node
        print("None")

##############################################################################

# Crear una nueva lista enlazada (instanciar)
my_list = LinkedList()

# 1. Agregar elementos
print("--- Agregando elementos ---")
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("\n")

# 2. Imprimir la lista actual
my_list.print_list()
print("\n")

# 3. Buscar un elemento
print("--- Buscando elementos ---")
my_list.search(20)
my_list.search(50)
print("\n")

# 4. Eliminar un elemento
print("--- Eliminando elementos ---")
my_list.delete(20)  # Elimina un elemento del medio
my_list.print_list()
print("\n")

my_list.delete(10)  # Elimina el primer elemento
my_list.print_list()
print("\n")

my_list.delete(40)  # Elimina el último elemento
my_list.print_list()
print("\n")

# 5. Intentar eliminar un elemento que no existe
my_list.delete(99)
print("\n")

# La lista final después de las operaciones
my_list.print_list()