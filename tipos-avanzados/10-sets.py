# no se puede repetir
# no están ordenados
# no se puede acceder a un elemento del set

# se remueven automaticamente los duplicados
primer = {1, 2, 2, 2, 3, 4, 5, 6}
print(primer)

segundo = [4, 6, 7, 8]
segundo = set(segundo)
print(segundo)

# union de los sets
print(primer | segundo)

# interseccion
print(primer & segundo)

# diferencia
print(primer - segundo)
print(segundo - primer)

# diferencia simetrica (elimina los elementos que están en ambos set)
print(primer ^ segundo)

if 5 in primer:
    print("Existe el numero 5")
