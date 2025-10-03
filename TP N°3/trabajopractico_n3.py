#1
months = ("enero", "febrero", "marzo", "abril")
print(f"El primer mes es {months[0]} y el último mes es {months[-1]}.")

#2
tuple1 = ("rojo", "verde", "azul")
tuple2 = ("amarillo", "naranja", "violeta")
tuple3 = tuple1 + tuple2
print(f"Tupla combinada: {tuple3}")

#3
numbers = (1, 2, 3, 4, 5)
filtered_numbers = tuple(n for n in numbers if n != 3)
print(f"Tupla sin el número 3: {filtered_numbers}")

#4
fruits = ("manzana", "banana", "naranja", "pera")
for index, fruit in enumerate(fruits):
    print(f"Índice {index}: {fruit}")

#5
scores = {}
while True:
    student = input("Ingresá el nombre del estudiante (o 'salir' para terminar): ")
    if student.lower() == "salir":
        break
    score = int(input(f"Ingresá la puntuación de {student}: "))
    scores[student] = score

search_name = input("Ingresá el nombre del estudiante que querés consultar: ")
if search_name in scores:
    print(f"La puntuación de {search_name} es {scores[search_name]}.")
else:
    print(f"No hay registro de {search_name}.")

#6
movie = {"title": "El padrino", "director": "Francis Ford Coppola", "year": 1972}
print(f"El director de la película es {movie['director']}.")
movie["year"] = 1974
print(f"Año actualizado: {movie['year']}.")

#7
diary = {"Juan": 47074963, "María": 46893258, "Pedro": 47123654}
del diary["María"]
print(f"Directorio actualizado: {diary}")

#8
ages = {"Juan": 30, "María": 25, "Pedro": 35}
ages["Ana"] = 28
for name, age in ages.items():
    print(f"{name} tiene {age} años.")

search_age = input("Ingresá un nombre para verificar si está en el diccionario de edades: ")
if search_age in ages:
    print(f"{search_age} está en el diccionario con edad {ages[search_age]}.")
else:
    print(f"{search_age} no está en el diccionario.")