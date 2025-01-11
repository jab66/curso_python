import usuarios.gestion
import usuarios.impuestos
from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios

pagar_impuestos()

print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)

print(usuarios.gestion.__name__)
print(usuarios.impuestos.__package__)
print(usuarios.gestion.__path__)
print(usuarios.impuestos.__file__)


# import usuarios.acciones
# usuarios.acciones.guardar()

# from usuarios import acciones
# acciones.guardar()


if __name__ == "__main__":
    print("Realizar alguna tarea")
