class Animal:
    def comer(self):
        print("comiendo")

# herencia


class Perro(Animal):
    def pasear(self):
        print("paseando")

# herencia multi nivel


class Gato(Perro):
    def trepar(self):
        print("trepando")


perro = Perro()
perro.comer()

gato = Gato()
gato.pasear()
