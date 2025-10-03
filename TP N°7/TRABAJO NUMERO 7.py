#1
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir_atributos(self):
        
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_resultado(self):
        
        if self.nota >= 6:
            print(f"El alumno {self.nombre} ha aprobado.")
        else:
            print(f"El alumno {self.nombre} ha reprobado.")
alumno1 = Alumno("Ana", 8.5)
alumno2 = Alumno("Luis", 4.0)
print("--- Información de Alumno 1 ---")
alumno1.imprimir_atributos()
alumno1.mostrar_resultado()

print("\n--- Información de Alumno 2 ---")
alumno2.imprimir_atributos()
alumno2.mostrar_resultado()

#2
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        try:
            area_valor = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
            return area_valor
        except ValueError:
            return "No se puede calcular el área de un triángulo con estas medidas."

    def forma(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Irregular"

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
triangulo1 = Triangulo(5, 5, 5)  
triangulo2 = Triangulo(3, 4, 5) 
print("--- Información de Triángulo 1 ---")
print(f"Lados: {triangulo1.lado1}, {triangulo1.lado2}, {triangulo1.lado3}")
print(f"Área: {triangulo1.area()}")
print(f"Forma: {triangulo1.forma()}")
print(f"Perímetro: {triangulo1.perimetro()}")

print("\n--- Información de Triángulo 2 ---")
print(f"Lados: {triangulo2.lado1}, {triangulo2.lado2}, {triangulo2.lado3}")
print(f"Área: {triangulo2.area()}")
print(f"Forma: {triangulo2.forma()}")
print(f"Perímetro: {triangulo2.perimetro()}")

#3
class Persona:
    def __init__(self, nombre=None, apellido=None, edad=0, dni=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    def esMayorDeEdad(self):
        return self.edad >= 18
persona1 = Persona("Juan", "Ramos", 30, "12345678")

print("--- Datos de la Persona 1 ---")
persona1.mostrar()
if persona1.esMayorDeEdad():
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

print("-" * 30)
persona2 = Persona("Franco", "Agüero", 19)

print("--- Datos de la Persona 2 ---")
persona2.mostrar()
if persona2.esMayorDeEdad():
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

#4
class Planeta:
    def __init__(self, nombre=None, satelites=0, masa_kg=0.0, volumen_km3=0.0,
                 diametro_km=0, distancia_sol_millones_km=0, tipo_planeta=None,
                 observable_a_vista_simple=False):

        self.nombre = nombre
        self.satelites = satelites
        self.masa_kg = masa_kg
        self.volumen_km3 = volumen_km3
        self.diametro_km = diametro_km
        self.distancia_sol_millones_km = distancia_sol_millones_km
        self.tipo_planeta = tipo_planeta
        self.observable_a_vista_simple = observable_a_vista_simple
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.satelites}")
        print(f"Masa: {self.masa_kg} kg")
        print(f"Volumen: {self.volumen_km3} km³")
        print(f"Diámetro: {self.diametro_km} km")
        print(f"Distancia media al Sol: {self.distancia_sol_millones_km} millones de km")
        print(f"Tipo de planeta: {self.tipo_planeta}")
        print(f"Observable a simple vista: {self.observable_a_vista_simple}")
    def calcular_densidad(self):
        if self.volumen_km3 > 0:
            return self.masa_kg / self.volumen_km3
        else:
            return 0
 
    def es_exterior(self):
        distancia_cinturon_en_millones_km = 508.632758
        return self.distancia_sol_millones_km > distancia_cinturon_en_millones_km
jupiter = Planeta("Júpiter", 95, 1.898e27, 1.431e15, 139822, 778.3, "Gigante gaseoso", True)
marte = Planeta("Marte", 2, 6.39e23, 1.6318e11, 6779, 227.9, "Terrestre", True)
print("--- Datos de Júpiter ---")
jupiter.mostrar_datos()
print(f"Densidad de Júpiter: {jupiter.calcular_densidad():.4f} kg/km³")
print(f"¿Es un planeta exterior?: {jupiter.es_exterior()}")

print("-" * 30)
print("--- Datos de Marte ---")
marte.mostrar_datos()
print(f"Densidad de Marte: {marte.calcular_densidad():.4f} kg/km³")
print(f"¿Es un planeta exterior?: {marte.es_exterior()}")

#5
class Vehiculo:
    def __init__(self, marca, modelo, patente, color):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Patente: {self.patente}, Color: {self.color}"
def main():
    vehiculos = [] 
    marcas_conteo = {}  

    print("Bienvenido al registro de vehículos familiares.")
    print("Ingresa 'salir' en la marca para terminar.")

    while True:
        marca = input("Ingresa la marca: ").strip()
        if marca.lower() == 'salir':
            break

        modelo = input("Ingresa el modelo: ").strip()
        patente = input("Ingresa la patente: ").strip().upper()
        color = input("Ingresa el color: ").strip().capitalize()
        nuevo_vehiculo = Vehiculo(marca, modelo, patente, color)
        vehiculos.append(nuevo_vehiculo)
        if marca in marcas_conteo:
            marcas_conteo[marca] += 1
        else:
            marcas_conteo[marca] = 1

        print("¡Vehículo agregado!\n")
    if not vehiculos:
        print("\nNo se registraron vehículos.")
        return
    print("\n--- Resumen de Vehículos ---")
    print(f"Total de vehículos registrados: {len(vehiculos)}")
    
    print("\nDetalle de vehículos:")
    for vehiculo in vehiculos:
        print(f" - {vehiculo}")

    print("\n--- Conteo de Marcas ---")
    for marca, cantidad in marcas_conteo.items():
        print(f"Marca '{marca}': {cantidad} vehículo(s)")
if __name__ == "__main__":
    main()

#6
class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calculo_salario(self):
        return self.horas_trabajadas * self.tarifa_hora
def main():
    empleados = [] 

    print("Bienvenido al sistema de liquidación de sueldos.")
    print("Ingresa 'salir' en el nombre del empleado para finalizar el ingreso.")

    while True:
        nombre = input("Ingresa el nombre del empleado: ").strip()
        if nombre.lower() == 'salir':
            break

        try:
            horas = float(input(f"Ingresa las horas trabajadas por {nombre}: "))
            tarifa = float(input(f"Ingresa la tarifa por hora para {nombre}: "))
        except ValueError:
            print("Por favor, ingresa un número válido para las horas y la tarifa.")
            continue 
        nuevo_empleado = Empleado(nombre, horas, tarifa)
        empleados.append(nuevo_empleado)
        print("¡Empleado agregado!\n")
    if not empleados:
        print("\nNo se registraron empleados. El programa ha finalizado.")
        return
    print("\n--- Liquidación de Sueldos ---")
    for empleado in empleados:
        sueldo = empleado.calculo_salario()
        print(f"El sueldo a pagar a {empleado.nombre} es: ${sueldo:.2f}")
if __name__ == "__main__":
    main()