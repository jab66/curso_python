from pathlib import Path
from zipfile import ZipFile

arc = "archivos/files.zip"

# generar un archivo comprimido
# with ZipFile(arc, "w") as zip:
#     # CURSO_PYTHON_UDEMY
#     for path in Path().rglob("*.py"):
#         if (not str(path).startswith("myenv")):
#             if (str(path) != arc):
#                 print(path)
#                 zip.write(path)


# leer de archivos comprimidos
# with ZipFile(arc) as zip:
#     # print(zip.namelist())
#     info = zip.getinfo("archivos/06-comprimidos.py")
#     print(
#         info.file_size,
#         info.compress_size
#     )

# extraer contenido del archivo comprimido
with ZipFile(arc) as zip:
    zip.extractall("archivos/descomprimidos")
