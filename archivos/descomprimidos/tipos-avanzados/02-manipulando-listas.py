autos = ["Ford", "Fiat", "Mercedes", "BMW"]

# mostrar un elemento
print(autos[1])

# cambiar un elemento
autos[2] = "Porsche"
print(autos)

# obtener elementos parciales de una lista
print(autos[2:4])

# indice negativo
print(autos[-2])

# elementos pares de una lista
print(autos[::2])
# elementos impares de una lista
print(autos[1::2])

numeros = list(range(21))
# numeros impares (debe iniciar en el indice 1 para no considerar el cero)
print(numeros[1::2])
# otra forma de hacer esto es al range indicarle la posicion 1:
# numeros = list(range(1, 21))
# print(numeros[::2])
# numeros pares (debe iniciar en el indice 0)
print(numeros[::2])
