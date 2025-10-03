class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()
    
    def superior(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

    def mostrar(self):
        if self.esta_vacia():
            print("PILA: [] (vacía)")
        else:
            print(f"PILA: BASE -> {self.items} <- TOPE")
             # Devuelve una copia de la lista de elementos
    
# Ejemplo de uso
print("Creando una nueva Pila")
mi_pila = Pila()
print()

print("Apilando elementos: 10, 20, 'Python'")
mi_pila.apilar(10)
mi_pila.apilar(20)
mi_pila.apilar("Python")
print()

print(f"Consultando el tope sin eliminarlo")
tope = mi_pila.superior()
print(f"El elemento en el tope es: {tope}")
print()

print("Mostrando todos los elementos de la pila")
mi_pila.mostrar()

print("Desapilando un elemento")
elemento_quitado = mi_pila.desapilar()
print(f"Elemento desapilado: {elemento_quitado}")
print()

print("Desapilando dos veces más")
mi_pila.desapilar()
mi_pila.desapilar()
print()

print("Intentando desapilar de una pila vacía")
elemento_quitado = mi_pila.desapilar()
print(f"Elemento desapilado: {elemento_quitado}")

print("verificando si la pila está vacía:")
print("(True = vacia / False = no lo está)")
print(mi_pila.esta_vacia())