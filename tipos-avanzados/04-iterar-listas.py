marcas = ["Ford", "Porsche", "Ferrari", "McLaren", "Pontiac"]

for marca in marcas:
    print(marca)

# enumerate retorna una tupla
for marca in enumerate(marcas):
    print(marca)

for indice, marca in enumerate(marcas):
    print(indice, marca)
