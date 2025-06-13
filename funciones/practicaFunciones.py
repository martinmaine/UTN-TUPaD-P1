import math

# Ejercicio 1: Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' por pantalla"""
    print("Hola Mundo!")

# Ejercicio 2: Función que saluda a un usuario
def saludar_usuario(nombre):
    """Recibe un nombre y devuelve un saludo personalizado"""
    return f"Hola {nombre}!"

# Ejercicio 3: Función que muestra información personal
def informacion_personal(nombre, apellido, edad, residencia):
    """Recibe datos personales e imprime la información"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4: Funciones para calcular área y perímetro de un círculo
def calcular_area_circulo(radio):
    """Calcula y devuelve el área de un círculo dado su radio"""
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Calcula y devuelve el perímetro de un círculo dado su radio"""
    return 2 * math.pi * radio

# Ejercicio 5: Función para convertir segundos a horas
def segundos_a_horas(segundos):
    """Convierte segundos a horas"""
    return segundos / 3600

# Ejercicio 6: Función para mostrar tabla de multiplicar
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del número dado del 1 al 10"""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ejercicio 7: Función para operaciones básicas
def operaciones_basicas(a, b):
    """Realiza las cuatro operaciones básicas y devuelve una tupla con los resultados"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# Ejercicio 8: Función para calcular IMC
def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)"""
    return peso / (altura ** 2)

# Ejercicio 9: Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """Convierte temperatura de Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# Ejercicio 10: Función para calcular promedio
def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números"""
    return (a + b + c) / 3

# PROGRAMA PRINCIPAL
def main():
    print("=== PRÁCTICO 2: FUNCIONES EN PYTHON ===\n")
    
    # Ejercicio 1
    print("--- Ejercicio 1 ---")
    imprimir_hola_mundo()
    print()
    
    # Ejercicio 2
    print("--- Ejercicio 2 ---")
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
    print()
    
    # Ejercicio 3
    print("--- Ejercicio 3 ---")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))
    residencia = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()
    
    # Ejercicio 4
    print("--- Ejercicio 4 ---")
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    print()
    
    # Ejercicio 5
    print("--- Ejercicio 5 ---")
    segundos = int(input("Ingresá la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    print()
    
    # Ejercicio 6
    print("--- Ejercicio 6 ---")
    numero_tabla = int(input("Ingresá el número para mostrar tu tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)
    print()
    
    # Ejercicio 7
    print("--- Ejercicio 7 ---")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {a} + {b} = {suma}")
    print(f"Resta: {a} - {b} = {resta}")
    print(f"Multiplicación: {a} * {b} = {multiplicacion}")
    print(f"División: {a} / {b} = {division}")
    print()
    
    # Ejercicio 8
    print("--- Ejercicio 8 ---")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresá tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    print()
    
    # Ejercicio 9
    print("--- Ejercicio 9 ---")
    celsius = float(input("Ingresá la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    print()
    
    # Ejercicio 10
    print("--- Ejercicio 10 ---")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()