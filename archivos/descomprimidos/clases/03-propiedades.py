class Perro:
    # propiedades de la clase
    patas = 4

    # constructor
    def __init__(self, nombre, edad):
        # propiedades de instancia
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

# mostrar el valor para todas las instancias de 'patas'
print(mi_perro.patas)

# se puede cambiar el valor de la propiedad de la clase para todas las clases
Perro.patas = 3
print(mi_perro.patas)

# se puede cambiar el valor de la propiedad de la clase solo para una instancia especifica
mi_perro.patas = 2
print(mi_perro.patas)
