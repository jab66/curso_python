class Perro:

    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def ladra(cls):
        print("Guau!!!")

    # Factory method

    @classmethod
    def factory(cls):
        return cls("Rex", 8)


Perro.ladra()

perro1 = Perro("Kira", 4)
print(perro1.nombre, perro1.edad)
perro2 = Perro("Luna", 11)
print(perro2.nombre, perro2.edad)

perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)
