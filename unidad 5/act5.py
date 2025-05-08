#1
multiplos_de_4 = [num for num in range(1, 101) if num % 4 == 0]
print(multiplos_de_4)

#2
frutas = ["banana", "manzana", "pera", "uva", "melón"]
print(frutas[-2])

#3
lista_vacia = []
lista_vacia.append("python")
lista_vacia.append("javascript")
lista_vacia.append("c#")
print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
""" Este programa toma el número máximo (max) y lo elimina con remove """

#6
numeros_salto = list(range(10, 35, 5))
print(numeros_salto[0:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "peugeot"
autos[2] = "ferrari"
print(autos)

#8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a)
compras[2].append("jugo")
# b)
compras[1][1] = "tallarines"
# c)
compras[0].remove("pan")
# d)
print(compras)

#10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)