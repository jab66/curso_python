from pathlib import Path
import os


path = Path("rutas")
paths = [p for p in path.iterdir() if p.is_dir()]
separador = os.sep

dependencias = {
    "db": "User",
    "usuario": "root",
    "api": "app de compras"
}


def load(p):
    print(p)
    paquete = str(p).replace(path.name+separador, "")
    paquete = __import__(str(paquete))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene metodo init")


list(map(load, paths))
