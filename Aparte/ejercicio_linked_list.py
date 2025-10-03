class Node:
    #Clase que representa un nodo individual en la lista enlazada.
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    #Clase principal que maneja las operaciones de la lista enlazada.
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

        if self.head.value == value_to_delete:
            self.head = self.head.next_node
            print(f"'{value_to_delete}' ha sido eliminado.")
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.value != value_to_delete:
            current_node = current_node.next_node

        if current_node.next_node is None:
            print(f"'{value_to_delete}' no se encontró en la lista.")
        else:
            current_node.next_node = current_node.next_node.next_node
            print(f"'{value_to_delete}' ha sido eliminado.")

    def search(self, value_to_find):
        #Busca un valor en la lista y retorna True si lo encuentra.
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

    def reverse_list(self):
        #Invierte la lista enlazada (sin crear una nueva).
        previous_node = None
        current_node = self.head

        while current_node is not None:
            # Guarda el siguiente nodo para no perderlo
            next_node = current_node.next_node
            # Invierte el puntero del nodo actual para que apunte al anterior
            current_node.next_node = previous_node
            # Mueve los punteros un paso adelante
            previous_node = current_node
            current_node = next_node
         # El head de la lista se convierte en el último nodo de la lista original
        self.head = previous_node
        print("La lista ha sido invertida.")

# --- Código para probar la clase LinkedList ---
if __name__ == "__main__":
    my_list = LinkedList()

    print("--- Agregando elementos ---")
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print("\n")

    print("--- Imprimiendo la lista original ---")
    my_list.print_list()
    print("\n")

    print("--- Invirtiendo la lista ---")
    my_list.reverse_list()
    print("\n")

    print("--- Imprimiendo la lista invertida ---")
    my_list.print_list()
    print("\n")

    print("--- Buscando un elemento ---")
    my_list.search(30)
    my_list.search(10)
    print("\n")

    print("--- Eliminando un elemento ---")
    my_list.delete(20)
    my_list.print_list()
    print("\n")

    print("--- Eliminando el primer elemento ---")
    my_list.delete(30)
    my_list.print_list()