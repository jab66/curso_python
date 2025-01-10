# para hacer herencia multiple, se aconseja que no hay nombres de metodos que se llamen igual

class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando con correa")


class Perro():
    def pasear(self):
        print("paseando")

# la herencia multiple se aplica de izquierda a derecha


class Gato(Perro, Animal):
    def trepar(self):
        print("trepando")


gato = Gato()
gato.comer()
gato.pasear()
gato.trepar()

perro = Perro()
perro.pasear()
