import random #oara ejercicio 5

# 1
for numero in range(101):  
    print(numero)

# 2
numero = int(input("Ingresa un número entero: "))
numero_absoluto = abs(numero)  
contador_digitos = 1  


if numero_absoluto == 0:
    contador_digitos = 1
else:
    while numero_absoluto >= 10:
        numero_absoluto = numero_absoluto // 10
        contador_digitos += 1

print(f"El número que ingresaste {numero} tiene {contador_digitos} dígito(s).")

# 3
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))


if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for numero in range(inicio + 1, fin):  
    suma += numero

print(f"La suma de los números entre {inicio} y {fin} (excluyendo ambos) es: {suma}")

# 4
print("Ingresa números para sumar. Ingresa 0 para terminar y mostrar el resultado.")
suma = 0
while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break  
    suma += numero

print(f"La suma total es: {suma}")

# 5
numero_secreto = random.randint(0, 9) 
intentos = 0

print("Adivina un número entre 0 y 9")

while True:
    intento = int(input("Escribe un número del 0 al 9: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! El número era {numero_secreto}")
        print(f"Adiviniste en {intentos} intento(s)")
        break
    elif intento < numero_secreto:
        print("Incorrecto! El número es mayor. Intenta de nuevo.")
    else:
        print("Incorrecto! El número es menor. Intenta de nuevo.")

# 6
for numero in range(100, -1, -2): 
    print(numero)

# 7
n = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(n + 1): 
    suma += i

print(f"La suma de los números de 0 hasta {n} es: {suma}")

# 8
cantidad_numeros = 100  

contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

print(f"Ingresa {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    numero = 5
    
    # par o impar
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    
    # positivo o negativo
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1


print("\nResultados:")
print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")
print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")


#9 
cantidad_numeros = 100  # Cantidad de números a procesar

suma = 0
print(f"Ingresa {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    suma += numero

media = suma / cantidad_numeros
print(f"La media de los {cantidad_numeros} números ingresados es: {media}")

#10
numero = int(input("Ingresa un número entero: "))
numero_original = numero
numero_invertido = 0


signo = 1
if numero < 0:
    signo = -1
    numero = abs(numero)


while numero > 0:
    digito = numero % 10  
    numero_invertido = numero_invertido * 10 + digito  
    numero = numero // 10  #


numero_invertido *= signo

print(f"El número {numero_original} invertido es: {numero_invertido}")

