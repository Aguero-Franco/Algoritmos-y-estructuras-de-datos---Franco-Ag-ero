#Ejercicio 2.
"""
Escribe un programa que genere un archivo de texto llamado nombres.txt,
 el cual almacene los nombres de 10 personas uno por línea.
El programa debe filtrar aquellos nombres que tengan una longitud mayor a 5 caracteres
y guardar estos nombres filtrados en un nuevo archivo llamado nombres_filtrados.txt,
 además debe imprimir los nombres filtrados en la consola.
"""

names = ["Macarena","Franco","Juan","Mariela","Brian","Carolina","Mia","Lucas","Isis","Candela"]
with open("nombres.txt", "w") as archivo:
    for nombre in names: 
        archivo.write(f"{nombre}\n")
filtrados=[]
with open("nombres.txt", "r") as archivo:
    for l in archivo:
        nombre = l.strip()  
        if len(nombre) > 5:
            filtrados.append(nombre)
with open("nombres_filtrados.txt", "w") as archivo:
    for nombre in filtrados:
        archivo.write(nombre + "\n")
print("Nombres con mas de 5 letras: ")
for nombre in filtrados:
    print(nombre)
 
