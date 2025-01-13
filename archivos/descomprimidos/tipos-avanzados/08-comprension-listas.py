# generar una lista solo con los nombres
usuarios = [[1, "Jorge"], [5, "Roberto"], [3, "Daniel"]]

# metodo 1
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])

# print(nombres)

# metodo 2
nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] == "Jorge"]
print(nombres)

# map
nombres = list(map(lambda usuario: usuario[1], usuarios))
print(nombres)

# filter
unnombre = list(filter(lambda usuario: usuario[1] == "Jorge", usuarios))
print(unnombre)
