# con listas

numeros = [1, 2, 3]
print(numeros)

print(*numeros)


def n(n1, n2, n3):
    print(n1, n2, n3)


n(*numeros)

numeros2 = [4, 5, 6]
combinada = [*numeros, *numeros2]
print(combinada)

# con diccionarios
# caso 1 - ver que pasa con "y":3
punto1 = {"x": 1, "y": 3}
punto2 = {"y": 2}

nuevopunto = {**punto1, **punto2, "a": 0}
print(nuevopunto)

# caso 2 - ver que pasa con "z":3
punto1 = {"x": 1, "z": 3}
punto2 = {"y": 2}

nuevopunto = {**punto1, **punto2, "a": 0}
print(nuevopunto)
