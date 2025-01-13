marcas = ["Ford", "Porsche", "Ferrari", "McLaren", "Pontiac", "Ferrari"]

marcas.insert(1, "Chevrolet")
print(marcas)

# lo agrega al final
marcas.append("Citroen")
print(marcas)

# borrar un elemento
# si esta mas de una vez, solo borra el primero
marcas.remove("Ferrari")
print(marcas)
# eliminar el ultimo elemento de la lista
marcas.pop()
print(marcas)
marcas.pop(1)
print(marcas)
# metodo para eliminar elemento
del marcas[0]
print(marcas)

# limpiar la lista completa
marcas.clear()
print(marcas)
