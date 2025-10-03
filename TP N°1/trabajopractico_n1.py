#1
print("Hola mundo")
#2
hello = "Hola mundo"
print(hello)
#3
number=3
print(number)
#4
numberdec=5.5
print(numberdec)
#5
name=input("Ingrese su nombre: ")
print(f"Hola {name}, bienvenido")
#6
number1=input("Ingrese un valor: ")
number2=input("Ingrese otro valor:")
print(f"Los valores son {number2} y {number1}")
#7
number_required=input("Ingrese un número: ")
print(f"Has introducido {number_required} gracias")
#8
value1=int(input("Valor para operar: "))
value2=int(input("Otro valor: "))
addition=value1+value2
subtraction=value1-value2
multiplication=value1*value2
division=value1/value2
print(f"La suma es: {addition}")
print(f"La resta es: {subtraction}")
print(f"La multiplicación es: {multiplication}")
print(f"La división es: {division}")
#9
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro valor para operar: "))
ecuacion1=5*num1+10*num2
print(f"5a+10b={ecuacion1}")
ecuacion2=num2*num2
print(f"b^2={ecuacion2}")
ecuacion3=2*num1-num2
print(f"2x-y={ecuacion3}")
ecuacion4=(2*num1-1)/(2*num1-1)
print(f"(2n-1)/(2n-1)={ecuacion4}")
#10
dec=float(input("Ingrese un número con decimales: "))
ent=int(input("Ingrese un número entero: "))
suma=float(dec+ent)
print(f"La suma es: {suma}")
#11
same1=int(input("Valor 1: "))
same2=int(input("Valor 2: "))
if same1==same2:
    print("Son iguales")
#12
n1=int(input("Primer valor: "))
n2=int(input("Segundo valor: "))
if n1>n2:
    print(f"El mayor valor es: {n1}")
else:
    print(f"El mayor valor es: {n2}")
#13
#len(word) cantidad de caracteres
word=input("Ingrese una palabra: ")
if len(word)>5:
    print(len(word))
#14
numcomp1=int(input("numero 1: "))
numcomp2=int(input("numero 2: "))
if numcomp1>numcomp2:
    print("El primero es mayor")
elif numcomp2>numcomp1:
    print("El segundo es mayor")
else:
    print("Son iguales")
#15
word1=input("palabra: ")
word2=input("palabra 2: ")
if len(word1)>len(word2):
    print("la primera es mas larga")
elif len(word1)<len(word2):
    print("la segunda es mas larga")
else:
    print("son iguales")
#16
posoneg=int(input("Numero: "))
if posoneg>0:
    print("Es positivo")
elif posoneg<0:
    print("Es negativo")
else:
    print("Es cero")
#17
numb1=int(input("Numero 1: "))
numb2=int(input("Numero 2: "))
numb3=int(input("Numero 3: "))
numeros=[numb1, numb2, numb3]
numeros.sort()
print(numeros)
#18
dividendo=int(input("Dividendo: "))
divisor=int(input("Divisor: "))
if divisor==0:
    print("Math Error")
else:
    print(dividendo/divisor)