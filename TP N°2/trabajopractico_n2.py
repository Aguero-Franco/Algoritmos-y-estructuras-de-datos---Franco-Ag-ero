#1
word1="Mordor"
print(word1[0])
print(word1[2])

#2
word2=input("Palabra: ")
print(word2[0].capitalize())

#3
word3=input("Palabra: ")
if len(word3)>5:
    print(word3[0])
    print(word3[1])
    print(word3[2])

#4
numb1=int(input("Ingrese un numero mayor a 1 y menor a 50: "))
for item in range(0, numb1):
    print(item)

#5
word4=input("Ingrese una palabra: ")
word5=input("Ingrese otra palabra: ")
print(f"{word4} {word5}")

#6
name=input("Ingrese su nombre: ")
surname=input("Ingrese su apellido: ")
print(f"{name} {surname}".title())

#7
frase=input("Ingrese una frase: ")
i=0
letras_pares=""
while i < len(frase):
    letras_pares += frase[i]
    i += 2 
print(letras_pares)

#8
word6=input("Ingrese una frase: ")
letter=input("Ingrese una letra: ")
counter1 = 0
for caracter in word6:
    if caracter == letter:
        counter1 += 1 
print(f"La letra '{letter}' aparece {counter1} veces en la frase.")

#9
word7=input("Ingrese una frase: ")
modified=""
for caracter in word7:
    if caracter == "a":
        modified += "4"
    elif caracter == "e":
        modified += "3"
    else:
        modified += caracter
print(f"La frase queda: {modified}")

#10
word8=input("Ingrese el nombre del archivo: ")
archive=""
for caracter in word8:
    if caracter == " ":
        archive += "_"
    elif caracter == ".":
        archive += "#"
    else:
        archive += caracter
print(f"El nombre queda: {archive}")

#11
numb_letter=["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
numb2=input("Ingrese un número de un solo dígito: ")
if len(numb2) == 1:
    print(f"El número es: {numb_letter[int(numb2)]}")
else:
    print("Error")

#12
word9 = input("Ingrese una frase: ")
word_temp = ""
for char in word9:
    if char == " ": 
        print(word_temp)
        word_temp = "" 
    else:
        word_temp += char
if word_temp:
    print(word_temp)

#13
lista1=[2, 65, 34, 3, 8, 65]
suma=lista1[0]+lista1[2]+lista1[5]
print(f"{lista1[0]} + {lista1[2]} + {lista1[5]} = {suma}")

#14
lista2=["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutilla"]
lista2.remove("Frutilla")
lista2.append("Canela en polvo")
for i in lista2:
    print(f"{i}")

#15
lista3=[56, 7, 34, 19, 3, 1, 76, 2, 81, 4, 2, 8]
for i in range(len(lista3)):
    if i % 2==0:
        print(lista3[i])

#16
colores = ["amarillo", "azul", "violeta"]
verduras = ["zapallo", "tomate", "limón"]

combinada = colores + verduras
print(combinada)

#17
movies = []
for _ in range(10):
    pelicula = input("Ingresa el nombre de una película: ")
    movies.append(pelicula)

n = int(input("Ingresa un número del 1 al 10: "))

if 1 <= n <= 10:
    print(f"La película en la posición {n} es: {movies[n-1]}")
else:
    print("Número fuera de rango")

#18
list1 = ["damasco", "frutilla", "ananá"]
list2 = ["zanahoria", "berenjena", "tomate"]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print(list3)

#19
valid_users = ["Ana", "Carlos", "Maria", "Luis", "Sofia"]
nombre_usuario = input("Ingrese su nombre: ")

if nombre_usuario in valid_users:
    print("El nombre es válido")
else:
    print("El nombre no está en la lista")

#20
phrase = input("Ingresa una frase: ")
words_list = phrase.split()

print(words_list)

#21
phrase = input("Ingresa una frase: ")
letters_list = list(phrase)

print(letters_list)

#22
full_names = []
last_names = []

while True:
    name = input("Ingresa un nombre completo (o escribe 'fin' para terminar): ")
    if name.lower() == "fin":
        break
    full_names.append(name)
    last_names.append(name.split()[-1])

print("Lista de nombres:", full_names)
print("Lista de apellidos:", last_names)

#23
grades = []

for _ in range(8):
    grade = float(input("Ingresa una nota: "))
    grades.append(grade)

average = round(sum(grades) / len(grades), 2)

print("El promedio de las notas es:", average)

#24
phrase = input("Ingresa una frase: ")

#con listas
word_list1 = phrase.split()
word_count_list1 = len(word_list1)

#sin listas
word_count_no_list = len(phrase.split())

print("Cantidad de palabras usando listas:", word_count_list1)
print("Cantidad de palabras sin usar listas:", word_count_no_list)

#25
numbers = [123, 4567, 89, 12345, 678, 9012]  # Puedes modificar esta lista o pedir datos al usuario
digit_counts = [len(str(num)) for num in numbers]

print("Lista de números:", numbers)
print("Cantidad de dígitos en cada número:", digit_counts)

#26
import random

dice_rolls = [random.randint(1, 6) for _ in range(20)]
average_roll = round(sum(dice_rolls) / len(dice_rolls), 2)

print("El promedio de las 20 tiradas es:", average_roll)

#27
dice_rolls_2500 = [random.randint(1, 6) for _ in range(2500)]
average_roll_2500 = round(sum(dice_rolls_2500) / len(dice_rolls_2500), 2)

print("El promedio de las 2500 tiradas es:", average_roll_2500)

#28
brands = []

for _ in range(10):
    brand = input("Ingresa una de tus marcas favoritas: ")
    brands.append(brand)

random_brand = random.choice(brands)

print("Una marca al azar de tu lista es:", random_brand)

#29
num_grades = int(input("Ingresa la cantidad de notas que deseas ingresar: "))
grades = []

for _ in range(num_grades):
    grade = float(input("Ingresa una nota: "))
    grades.append(grade)

print("Las notas ingresadas son:", grades)

#30
#con while
countdown1 = int(input("Ingresa un número positivo: "))

while countdown1 >= 0:
    print(countdown1)
    countdown1 -= 1

#con for
countdown2 = int(input("Ingresa un número positivo: "))

for num in range(countdown2, -1, -1):
    print(num)

#31
positive_count = 0
negative_count = 0

for _ in range(10):
    number1 = int(input("Ingresa un número: "))
    if number1 > 0:
        positive_count += 1
    elif number1 < 0:
        negative_count += 1

print("Cantidad de números positivos:", positive_count)
print("Cantidad de números negativos:", negative_count)

#32
numbers1 = []

while True:
    user_input = input("Ingresa un número entero (o escribe 's' para salir): ")
    if user_input.lower() == "s":
        break
    numbers1.append(int(user_input))

print("Números ingresados:", numbers1)

#33
num_entries = int(input("Ingresa la cantidad de números a ingresar: "))
sum_even = 0
odd_flag = False

for _ in range(num_entries):
    number2 = int(input("Ingresa un número: "))
    
    if number2 == 99:
        break
    
    if number2 % 2 == 0:
        sum_even += number2
    else:
        odd_flag = True

print("Suma de los números pares:", sum_even)
if odd_flag:
    print("Se ingresaron impares.")

#34
numbers2 = []

for _ in range(10):
    number3 = int(input("Ingresa un número: "))
    numbers2.append(number3)

min_number = min(numbers2)
max_number = max(numbers2)

print("El menor número ingresado es:", min_number)
print("El mayor número ingresado es:", max_number)

#35
number4 = input("Ingresa un número de 6 cifras: ")

if len(number4) == 6 and number4.isdigit():
    inverted_number = number4[::-1]
    print(f"El número ingresado es {number4}, invertido es: {inverted_number}")
else:
    print("Por favor, ingresa un número válido de 6 cifras.")

#36
import random

# Solicitar al usuario dos números positivos
lower_limit = int(input("Ingresa un número positivo para el límite inferior: "))
upper_limit = int(input("Ingresa un número positivo para el límite superior: "))

# Validar que el primer número sea menor que el segundo
while lower_limit >= upper_limit:
    print("El primer número debe ser menor que el segundo. Inténtalo nuevamente.")
    lower_limit = int(input("Ingresa un número positivo para el límite inferior: "))
    upper_limit = int(input("Ingresa un número positivo para el límite superior: "))

# Mostrar los números en el intervalo
print(f"Números en el intervalo [{lower_limit}, {upper_limit}]:")
for value in range(lower_limit, upper_limit + 1):
    print(value, end=" ")

print("\n")

# Seleccionar un número aleatorio dentro del intervalo
hidden_number = random.randint(lower_limit, upper_limit)

# El usuario tiene 10 intentos para adivinar
attempts = 10

while attempts > 0:
    guess = int(input("Adivina el número seleccionado por la computadora: "))

    if guess == hidden_number:
        print("¡Éxito! Has acertado el número.")
        break
    else:
        attempts -= 1
        print(f"Pucha... Número incorrecto. Intentos restantes: {attempts}")

# Si el usuario agotó sus intentos sin acertar
if attempts == 0:
    print(f"Has agotado tus intentos. El número era {hidden_number}.")
