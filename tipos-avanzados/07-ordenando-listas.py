marcas = ["Ford", "Porsche", "Ferrari", "McLaren", "Pontiac", "Ferrari"]

marcas.sort()
print(marcas)

marcas.sort(reverse=True)
print(marcas)

# funcion sorted -->> devuelve una nueva lista
brands = sorted(marcas, reverse=True)
print(brands)

# ordenar sublistas
usuarios = [[1, "Jorge"], [5, "Roberto"], [3, "Daniel"]]
usuarios.sort()
print(usuarios)

# para ordenar por otro elemento que no sea el primero
# recomendacion: usar funcion lambda
# def ordena(elemento):
#     return elemento[1]
# usuarios.sort(key=ordena, reverse=False)
# print(usuarios)


# funcion lambda
usuarios.sort(key=lambda el: el[1], reverse=False)
print(usuarios)
