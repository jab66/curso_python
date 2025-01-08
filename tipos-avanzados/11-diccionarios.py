punto = {"x": 25, "y": 10}
print(punto)
print(punto["x"])

# agregar una nueva llave
punto["z"] = 66
print(punto)

# si no existe una llave cuando se accede al diccionario, da error
# posibles soluciones (if)
# usar get
if "r" in punto:
    print(punto["r"])

print(punto.get("z"))
print(punto.get("r", 99))

# eliminar un llave
del punto["z"]
print(punto)

# itenar las llaves
for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# uso real de los diccionarios
# la variable usuarios contendrá un json
usuarios = [
    {"id": 1, "nombre": "Jorge"},
    {"id": 2, "nombre": "Daniel"},
    {"id": 3, "nombre": "Roberto"}
]
for usuario in usuarios:
    print(usuario["nombre"])
