#1
"""
def cuadrado(numero):
    resultado= numero ** 2
    extra="ejemplo"
    extra2=True
    print(locals())
    print(resultado)
    
cuadrado(5)
"""
#2
"""
n=4
def cuadrado(numero):
    numero=3
    resultado= numero ** 2
    print(resultado)
    
cuadrado(n)
"""
#Para modificar el valor de n desde dentro del def, hay que asignarselo dentro de la función y se anula el valor global

#3
#No imprimirá nada porque no está siendo llamada la función
#El alcance de frase global es a todo el código pero frase dentro de def solo sirve si la llamamos desde afuera
"""
frase="Hola"

def f():
    frase="Es un lindo dia"
    print(frase)
"""
#4
"""
x=3
def f():
    y=x+1
    print(x)
    def g():
        x=1
        print(y)
        print(x)
    g()
f()
"""
#Se imprime el valor inicial de x (3), luego se modifica el valor de x a 1 y se imprime Y que fue definida en f(),
#y por último se imprime el valor de x modificado (1)

#5
"""
def lado(num):
    perimetro=num*4
    area=num**2
    print(perimetro)
    print(area)

lado(3)
"""
#6
"""
def tabla(num):
    for i in range(11):
        multi=num*i
        print(multi)

tabla(int(input("Numero: ")))
"""
#7
"""
def cuadrante(x, y):
    if x > 0 and y > 0:
        print("Primer cuadrante")
    elif x < 0 and y > 0:
        print("Segundo cuadrante")
    elif x < 0 and y < 0:
        print("Tercer cuadrante")
    else:
        print("Cuarto cuadrante")

cuadrante(int(input("X=")), int(input("Y=")))
"""
#8
"""
def potencia(base, exp):
    y=base ** exp
    print(y)

potencia(2, -2)
"""
#9
"""
def frase(string, letra):
    suma=0
    for i in string:
        if i == letra:
            suma+=1
    print(suma)

frase("Barcelona", "a")
"""

#10
"""
def frase(string, letra):
    suma=0
    for i in string:
        for j in i:
            if j == letra:
                suma+=1
    print(f"La letra ´{letra}´ aparece {suma} veces en esas palabras")


diez_palabras=[]
for j in range(3):
    word=str(input("Palabra: "))
    diez_palabras.append(word)

caracter=str(input("Letra: "))
frase(diez_palabras, caracter)
"""
#11
"""
def paridad(num):
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

paridad(int(input("Número: ")))

#Otra opción

def par(num1):
    return num1 % 2 == 0

print(par(int(input("Número: "))))
"""
#12
"""
def triangulo(caracter, numero):
    ancho=numero
    for i in range(ancho):
        for j in range(ancho):
            print(caracter, end=" ")
        print()
        ancho=ancho-1

triangulo("*", 4)
"""
#13
"""
import math

def primo(numero):
    raiz= math.floor(math.sqrt(numero))
    if numero < 2:
        return False
    for i in range(2, raiz+1):
            if numero % i == 0:
                return False
    return True

print(primo(int(input("Numero: "))))
"""
#14
"""
def mayor(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print("Son iguales")

print(mayor(int(input("X: ")), int(input("Y: "))))
"""
#15
"""
def promedio(a, b, c, d, e):
    lista_promedio=[a, b, c, d, e]
    suma=0
    for i in lista_promedio:
        suma=suma+i
    prom=suma/len(lista_promedio)
    print(prom)
    
promedio(5, 4, 3, 2, 1)
"""
#16
"""
def comparacion(binario):
    suma_cero=0
    suma_uno=0
    convertido=str(binario)
    for i in convertido:
        if i == "0":
            suma_cero+=1
        elif i == "1":
            suma_uno+=1
    print(suma_uno)
    print(suma_cero)
    if suma_cero == suma_uno:
        print("Tienen la misma cantidad")
    else:
        print("No tienen la misma cantidad de 1 que de 0")

comparacion(100111)
"""
#17
"""
def posicion(cadena, letra):
    palabra=str(cadena)
    suma=0
    for i in palabra:
        suma+=1    
        if i == letra:
            return suma

print(posicion("arbol", "l"))
"""
#18
"""
def cuadro(numero, simbolo):
    for i in range(numero):
        if i == 0 or i == numero-1:
            for j in range(numero):
                print(simbolo, end=" ")
        else:
            for k in range(numero):
                if k==0 or k==numero-1:
                    print(simbolo, end=" ")
                else:
                    print(" ", end=" ")
        print()

cuadro(5, "*")
"""
#19
"""
def mayus(cadena):
    palabra=""

    for i in range(len(cadena)):
        if i == 0 or cadena[i-1] == " ":
            palabra += cadena[i].capitalize()
        else:
            palabra += cadena[i]
    return palabra
    

print(mayus("hola mundo franco"))
"""
#20
"""
def array(vector1, vector2, bool):
    print(vector1)
    print(vector2)
    print(bool)
    print()
    lista_array=[]
    posicion=len(vector1)
    if bool == True:
        for i in range(len(vector1)):
            posicion -= 1
            for index in vector2:
                if vector1[posicion] == vector2:
                    lista_array.append(vector1[posicion])
    print(lista_array)        

array([1,2,3,4,5,6], [1,2,3,6,7,8,9], True)
"""
#21
"""
def calcular_ganador():
    reglas = {("R", "S"): "Player 1", ("S", "R"): "Player 2",
              ("P", "R"): "Player 1", ("R", "P"): "Player 2",
              ("S", "P"): "Player 1", ("P", "S"): "Player 2"}

    puntaje = {"Player 1": 0, "Player 2": 0}

    cantidad_rondas = int(input("¿Cuántas rondas quieres jugar? "))

    jugadas = []
    for i in range(cantidad_rondas):
        jugador1 = input(f"Ronda {i+1} - Jugador 1 (R/P/S): ").upper()
        jugador2 = input(f"Ronda {i+1} - Jugador 2 (R/P/S): ").upper()
        
        if jugador1 not in "RPS" or jugador2 not in "RPS":
            print("Entrada inválida, por favor usa R, P o S.")
            continue
        
        jugadas.append((jugador1, jugador2))

        if jugador1 == jugador2:
            continue
        ganador = reglas.get((jugador1, jugador2))
        if ganador:
            puntaje[ganador] += 1

    if puntaje["Player 1"] > puntaje["Player 2"]:
        resultado = "Player 1"
    elif puntaje["Player 2"] > puntaje["Player 1"]:
        resultado = "Player 2"
    else:
        resultado = "Tie"

    print(f"Resultado final: {resultado}")


calcular_ganador()
"""