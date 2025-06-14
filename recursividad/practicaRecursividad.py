
# PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD
# Tecnicatura Universitaria en Programación - UTN

# ============================================================================
# EJERCICIO 1: Factorial recursivo
# ============================================================================

def factorial(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Caso recursivo

def mostrar_factoriales():
    """Muestra los factoriales desde 1 hasta el número indicado por el usuario."""
    try:
        numero = int(input("Ingrese un número para calcular factoriales desde 1 hasta ese número: "))
        if numero < 1:
            print("Por favor, ingrese un número positivo.")
            return
        
        print(f"\nFactoriales desde 1 hasta {numero}:")
        for i in range(1, numero + 1):
            resultado = factorial(i)
            print(f"{i}! = {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# ============================================================================
# EJERCICIO 2: Serie de Fibonacci
# ============================================================================

def fibonacci(n):
    """Calcula el valor de Fibonacci en la posición n."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    """Muestra la serie de Fibonacci hasta la posición especificada."""
    try:
        posicion = int(input("Ingrese la posición hasta donde mostrar la serie de Fibonacci: "))
        if posicion < 0:
            print("Por favor, ingrese un número no negativo.")
            return
        
        print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
        for i in range(posicion + 1):
            valor = fibonacci(i)
            print(f"F({i}) = {valor}")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# ============================================================================
# EJERCICIO 3: Potencia recursiva
# ============================================================================

def potencia(base, exponente):
    """Calcula la potencia de un número usando recursión."""
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)

def probar_potencia():
    """Prueba la función de potencia con valores ingresados por el usuario."""
    try:
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        
        if exponente < 0:
            print("Este algoritmo funciona solo con exponentes no negativos.")
            return
        
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")

# ============================================================================
# EJERCICIO 4: Conversión a binario
# ============================================================================

def decimal_a_binario(numero):
    """Convierte un número decimal a binario usando recursión."""
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

def probar_binario():
    """Prueba la conversión a binario."""
    try:
        numero = int(input("Ingrese un número decimal para convertir a binario: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
            return
        
        if numero == 0:
            print(f"El número {numero} en binario es: 0")
        else:
            binario = decimal_a_binario(numero)
            print(f"El número {numero} en binario es: {binario}")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# ============================================================================
# EJERCICIO 5: Palíndromo recursivo
# ============================================================================

def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo usando recursión."""
    # Convertir a minúsculas para comparación
    palabra = palabra.lower()
    
    # Caso base: palabra vacía o de un carácter
    if len(palabra) <= 1:
        return True
    
    # Verificar si el primer y último carácter son iguales
    if palabra[0] == palabra[-1]:
        # Llamada recursiva con la subcadena sin el primer y último carácter
        return es_palindromo(palabra[1:-1])
    else:
        return False

def probar_palindromo():
    """Prueba la función de palíndromo."""
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    if es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")

# ============================================================================
# EJERCICIO 6: Suma de dígitos
# ============================================================================

def suma_digitos(n):
    """Calcula la suma de los dígitos de un número usando recursión."""
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

def probar_suma_digitos():
    """Prueba la función suma de dígitos."""
    try:
        numero = int(input("Ingrese un número para sumar sus dígitos: "))
        numero = abs(numero)  # Trabajar con valor absoluto
        resultado = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# ============================================================================
# EJERCICIO 7: Contar bloques de pirámide
# ============================================================================

def contar_bloques(n):
    """Cuenta el total de bloques necesarios para construir una pirámide."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def probar_piramide():
    """Prueba la función de contar bloques."""
    try:
        niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
        if niveles < 1:
            print("El número debe ser positivo.")
            return
        
        total = contar_bloques(niveles)
        print(f"Para una pirámide con {niveles} bloques en la base se necesitan {total} bloques en total.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# ============================================================================
# EJERCICIO 8: Contar apariciones de un dígito
# ============================================================================

def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número."""
    if numero == 0:
        return 1 if digito == 0 else 0
    
    # Obtener el último dígito
    ultimo_digito = numero % 10
    
    # Contar si coincide con el dígito buscado
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

def probar_contar_digito():
    """Prueba la función de contar dígito."""
    try:
        numero = int(input("Ingrese un número: "))
        digito = int(input("Ingrese el dígito a buscar (0-9): "))
        
        if digito < 0 or digito > 9:
            print("El dígito debe estar entre 0 y 9.")
            return
        
        numero = abs(numero)  # Trabajar con valor absoluto
        cantidad = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
    except ValueError:
        print("Por favor, ingrese números válidos.")

# ============================================================================
# FUNCIÓN PRINCIPAL PARA PROBAR TODOS LOS EJERCICIOS
# ============================================================================

def menu_principal():
    """Menú principal para probar todos los ejercicios."""
    while True:
        print("\n" + "="*50)
        print("PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD")
        print("="*50)
        print("1. Factorial recursivo")
        print("2. Serie de Fibonacci")
        print("3. Potencia recursiva")
        print("4. Conversión decimal a binario")
        print("5. Verificar palíndromo")
        print("6. Suma de dígitos")
        print("7. Contar bloques de pirámide")
        print("8. Contar apariciones de dígito")
        print("0. Salir")
        print("="*50)
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                mostrar_factoriales()
            elif opcion == 2:
                mostrar_fibonacci()
            elif opcion == 3:
                probar_potencia()
            elif opcion == 4:
                probar_binario()
            elif opcion == 5:
                probar_palindromo()
            elif opcion == 6:
                probar_suma_digitos()
            elif opcion == 7:
                probar_piramide()
            elif opcion == 8:
                probar_contar_digito()
            elif opcion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        
        except ValueError:
            print("Por favor, ingrese un número válido.")



# ============================================================================
# EJEMPLOS DE USO Y PRUEBAS
# ============================================================================

if __name__ == "__main__":
    print("EJEMPLOS DE PRUEBA:")
    print("\n1. Factorial de 5:", factorial(5))
    print("2. Fibonacci en posición 6:", fibonacci(6))
    print("3. 2^8 =", potencia(2, 8))
    print("4. 10 en binario:", decimal_a_binario(10))
    print("5. ¿'radar' es palíndromo?", es_palindromo("radar"))
    print("6. Suma de dígitos de 1234:", suma_digitos(1234))
    print("7. Bloques para pirámide de 4 niveles:", contar_bloques(4))
    print("8. Veces que aparece '2' en 12233421:", contar_digito(12233421, 2))