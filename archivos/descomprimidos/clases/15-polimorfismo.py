from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en la base de datos")


class Session(Model):
    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


# el objetivo no es llamar a el metodo guardar de cada una de las clases
# esto es polimorfismo
usuario = Usuario()
sesion = Session()
guardar([usuario, sesion])
