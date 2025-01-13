class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: nombre: {self.nombre} - precio {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


pelota = Producto("Pelota de Futbol", 350)
kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)

deportes = Categoria("Deportes", [pelota, kayak])
deportes.agregar(bicicleta)

deportes.imprimir()
