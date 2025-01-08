numeros = [1, 2, 3]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

primero, *otros = numeros
print(primero, otros)

numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros2)

first, second, *otros, last = numeros2
print(first, second, otros, last)
