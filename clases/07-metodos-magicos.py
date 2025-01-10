# los metodos magicos comienzan con __ y terminan con __

class Perro:

    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chau perro {self.nombre}")

    def __str__(self):
        return f"Clase Perro(): nombre: {self.nombre}, edad: {self.edad}"


perro = Perro("Kira", 7)
print(perro)
nombre = str(perro)
print(perro)

del perro
