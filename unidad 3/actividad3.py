# Ejercicio 1


edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")


# Ejercicio 2


nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3


numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ejercicio 4


edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:  # Mayor o igual a 30
    print("Adulto/a")


# Ejercicio 5


contraseña = input("Ingrese una contraseña: ")
longitud = len(contraseña)
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6


import random
from statistics import mode, median, mean

# Generar lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except:
    # En caso de que no haya un valor que aparezca más veces que los demás
    print("No se pudo determinar la moda. Usando la mediana como valor de la moda.")
    moda = mediana

# Determinar el sesgo
if media > mediana and mediana > moda:
    print("Hay un sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay un sesgo negativo o a la izquierda")
else:
    print("No hay sesgo")

# Imprimir los valores
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")


# Ejercicio 7


texto = input("Ingrese una frase o palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

if texto[-1].lower() in vocales:
    print(texto + "!")
else:
    print(texto)


# Ejercicio 8


nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")


# Ejercicio 9


magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:  # >= 7
    print("Extremo (puede causar graves daños a gran escala)")


# Ejercicio 10


hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Determinar el periodo del año
if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:  # (mes == 9 and dia >= 21) or (mes <= 12 and (mes != 12 or dia <= 20))
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print(f"La estación actual es: {estacion}")