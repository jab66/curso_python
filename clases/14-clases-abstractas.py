from abc import ABC, abstractmethod

# hereda de ABC para que no se puedan crear instancias de la clase Model


class Model(ABC):
    # tabla = False

    # def __init__(self):
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")

    @property
    @abstractmethod
    # se tiene que implementar en la clase que hereda
    def tabla(self):
        pass

    @abstractmethod
    # se tiene que implementar en la clase que hereda
    def mensaje(self):
        pass

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def mensaje(self):
        print("Mensaje desde la clase Usuario")


usuario = Usuario()
usuario.guardar()
usuario.mensaje()

Usuario.buscar_por_id(123)
