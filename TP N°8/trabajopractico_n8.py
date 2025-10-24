#TRABAJO PRACTICO NUMERO 8
pila = []
pila.append("A")
pila.append("B")
pila.append("C")
print("Pila original:", pila)

pila_invertida = []

while pila:
    elemento = pila.pop()  
    pila_invertida.append(elemento)  

print("Pila invertida:", pila_invertida)
#EJERCICIO 2 
palabra = input("Ingrese una palabra: ")
pila = []
for letra in palabra:
    pila.append(letra)
print("Palabra original:", palabra)
palabra_invertida = ""
while pila:
    palabra_invertida += pila.pop()
print("Palabra invertida:", palabra_invertida)
#EJERCICIO 3
# Leer palabra
palabra = input("Ingrese una palabra: ")
pila = []
for letra in palabra:
    pila.append(letra)
palabra_invertida = ""
while pila:
    palabra_invertida += pila.pop()
print("Palabra original:", palabra)
print("Palabra invertida:", palabra_invertida)

if palabra == palabra_invertida:
    print("La palabra es un palíndromo ")
else:
    print("La palabra NO es un palíndromo")
#EJERCICIO 4
pueblos = ["Origen", "A", "B", "C", "Destino"]
pila = []
print("Camino de ida:")
for pueblo in pueblos:
    pila.append(pueblo)
    print(" →", pueblo)
print("\nCamino de vuelta:")
while pila:
    pueblo = pila.pop()
    print(" →", pueblo)
#EJERCICIO 5
cadena = input("Ingrese una cadena con paréntesis: ")
pila = []
error = False
for i, simbolo in enumerate(cadena):
    if simbolo == "(":
        pila.append(simbolo)
    elif simbolo == ")":
        if pila:
            pila.pop()
        else:
            print(f"Error en posición {i}: Falta un '(' antes de ')'")
            error = True
            break
if not error:
    if not pila:
        print("Los paréntesis están balanceados ")
    else:
        print(f"Error: Faltan {len(pila)} símbolo(s) ')' de cierre ")
#EJERCICIO 6
class Pila:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad
    def push(self, item):
        if len(self.items) < self.capacidad:
            self.items.append(item)
        else:
            print("Error: La pila está llena")
    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("Error: La pila está vacía")
            return None
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    def esta_vacia(self):
        return len(self.items) == 0
    def mostrar(self):
        print("Pila:", self.items)
def retirar_contenedor(pila, id_contenedor):
    pila_aux = Pila(pila.capacidad)
    while not pila.esta_vacia() and pila.cima() != id_contenedor:
        pila_aux.push(pila.pop())
    if not pila.esta_vacia() and pila.cima() == id_contenedor:
        print(f"Retirando contenedor {pila.pop()} ")
    else:
        print("El contenedor no está en la pila ")
    while not pila_aux.esta_vacia():
        pila.push(pila_aux.pop())
# Ejemplo de uso
almacen = Pila(10)
for id_c in [101, 102, 103, 104, 105]:
    almacen.push(id_c)
print("Estado inicial:")
almacen.mostrar()
retirar_contenedor(almacen, 103)
print("Estado final:")
almacen.mostrar()
#EJERCICIO 7
def invertir_archivo(nombre_archivo):
    pila = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            pila.append(linea.rstrip("\n"))
    with open("invertido.txt", "w", encoding="utf-8") as archivo_invertido:
        while pila:
            archivo_invertido.write(pila.pop() + "\n")
# ------------------------------
# Ejemplo de uso
invertir_archivo("original.txt")
print("Archivo 'invertido.txt' generado correctamente")
#EJERCICIO 8
def invertir_frase(frase):
    pila = []
    for palabra in frase.split():
        pila.append(palabra)
    frase_invertida = []
    while pila:
        frase_invertida.append(pila.pop())

    return " ".join(frase_invertida)
# ------------------------------
# Ejemplo con la frase solicitada
frase = "que tengas buena suerte"
resultado = invertir_frase(frase)

print("Frase original:", frase)
print("Frase invertida:", resultado)
#EJERICICIO 9
from collections import deque
cola = deque()
pacientes = [
    {"nombre": "Ana", "obra_social": True},
    {"nombre": "Juan", "obra_social": False},
    {"nombre": "María", "obra_social": True},
    {"nombre": "Pedro", "obra_social": False},
    {"nombre": "Lucía", "obra_social": True}
]

for paciente in pacientes:
    cola.append(paciente)
con_obra_social = 0
while cola:
    paciente_actual = cola.popleft()  
    print(f"Atendiendo a {paciente_actual['nombre']}")
    
    if paciente_actual["obra_social"]:
        con_obra_social += 1

print(f"\nCantidad de pacientes con obra social: {con_obra_social}")
#EJERCICIO 10
from collections import deque
MAX_CARTAS = 3  
personas = [
    {"nombre": "Ana", "cartas": 7},
    {"nombre": "Juan", "cartas": 2},
    {"nombre": "María", "cartas": 5},
    {"nombre": "Pedro", "cartas": 1}
]
cola = deque(personas)
while cola:
    persona = cola.popleft()  
    cartas_a_enviar = min(persona["cartas"], MAX_CARTAS)
    
    print(f"{persona['nombre']} entrega {cartas_a_enviar} cartas")
    
    persona["cartas"] -= cartas_a_enviar
    if persona["cartas"] > 0:
        print(f"{persona['nombre']} vuelve a la cola con {persona['cartas']} cartas restantes")
        cola.append(persona)

print("\nTodas las cartas han sido entregadas.")
#EJERICIO 11
from collections import deque

def simulacion_cola_impresion(documentos):
    """
    """
    cola = deque(documentos)
    
    while cola:
        doc_actual = cola.popleft() 
        print(f"Imprimiendo '{doc_actual['documento']}' ({doc_actual['paginas']} páginas)")
    
    print("\nTodos los documentos han sido impresos.")
documentos = [
    {"documento": "Informe1", "paginas": 5},
    {"documento": "Tarea", "paginas": 2},
    {"documento": "Proyecto", "paginas": 10},
]
simulacion_cola_impresion(documentos)

