class Perro:

    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo
    def ladra(self):
        print(f"{self.nombre} dice Guau!!!")


# instancia
mi_perro = Perro("Luna", 3)

print(mi_perro.nombre)
print(mi_perro.edad)
mi_perro.ladra()
