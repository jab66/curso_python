class Perro:

    # constructor
    def __init__(self, nombre):
        # se define la propiedad nombre como privada
        self.nombre = nombre

    @property
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Kira")
print(perro.nombre)
