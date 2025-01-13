import json
from pathlib import Path

# escribir json
productos = [
    {"id": 1, "name": "Leche"},
    {"id": 2, "name": "Verdura"},
    {"id": 3, "name": "Gaseosa"}
]

# crear json
# data = json.dumps(productos)
# print(data)
# Path("archivos/archivo.json").write_text(data, encoding="utf-8")


# leer json
# data = Path("archivos/archivo.json").read_text(encoding="utf-8")
# productos = json.loads(data)
# print(productos)

# modificar json
productos[0]["name"] = "Galletita"
Path("archivos/archivo.json").write_text(json.dumps(productos))
