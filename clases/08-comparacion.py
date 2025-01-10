class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # iguales
    def __eq__(self, otraInstancia):
        return self.lat == otraInstancia.lat and self.lon == otraInstancia.lon

    # distintos
    # no es necesario hacerlo ya que python con __eq__ detecta la desigualdad
    def __ne__(self, otraInstancia):
        return self.lat != otraInstancia.lat or self.lon != otraInstancia.lon

    # menor
    def __lt__(self, otraInstancia):
        return self.lat+self.lon < otraInstancia.lat+otraInstancia.lon

    # menor o igual
    def __le__(self, otraInstancia):
        return self.lat+self.lon <= otraInstancia.lat+otraInstancia.lon


coords1 = Coordenadas(25, 27)
coords2 = Coordenadas(25, 27)

# verificar sin son iguales
# apuntan a una posicion distinta cada una de estas instancias (por eso es FALSE)
print(coords1 == coords2)

print(coords1 != coords2)

print(coords1 < coords2)

print(coords1 <= coords2)
