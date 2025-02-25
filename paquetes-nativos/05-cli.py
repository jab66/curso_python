import os
from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("no se pasaron argumentos")
        return
    if (len(args) != 3):
        print("se necesitan dos argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino ya existe, no se puede renomabrar")
        return

    os.rename(str(origen), str(destino))
    print("el archivo fue renombrado con exito")


cli(sys.argv)
