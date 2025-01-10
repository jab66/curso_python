class Perro:

    # constructor
    def __init__(self, nombre, edad):
        # se define la propiedad nombre como privada
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    # metodo privado
    def __set_nombre(self, nombre):
        self.__nombre = nombre

    def ladra(self):
        print(f"{self.__nombre} dice Guau!!!")

    # Factory method
    @classmethod
    def factory(cls):
        return cls("Rex", 8)


perro1 = Perro.factory()
perro1.ladra()

print(perro1.get_nombre())

# diccionario que contiene todas las propiedades de una instancia
print(perro1.__dict__)
print(perro1._Perro__nombre)
