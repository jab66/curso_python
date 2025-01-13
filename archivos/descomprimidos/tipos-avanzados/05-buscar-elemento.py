marcas = ["Ford", "Porsche", "Ferrari", "McLaren", "Pontiac"]

# retorna el indice donde se encuentra el texto que buscamos
# si lo que se busca no existe, da error (hay que revisar si el elemento se encuentra en el listado)
print(marcas.index("Ferrari"))

# no existe BMW en la lista, se hace primero el if para que no de error
if "BMW" in marcas:
    print(marcas.index("BMW"))
else:
    print("BMW no existe en la lista")
# lo agregamos en la lista
marcas.append("BMW")
if "BMW" in marcas:
    print(marcas.index("BMW"))
else:
    print("BMW no existe en la lista")

# cuantas veces aparece el mismo elemento en la lista
print(marcas.count("Ferrari"))
marcas.append("Ferrari")
print(marcas.count("Ferrari"))
