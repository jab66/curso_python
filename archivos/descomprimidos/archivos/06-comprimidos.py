from pathlib import Path
from zipfile import ZipFile

arc = "archivos/files.zip"

# generar un archivo comprimido
with ZipFile(arc, "w") as zip:
    # CURSO_PYTHON_UDEMY
    for path in Path().rglob("*.py"):
        if (not str(path).startswith("myenv")):
            if (str(path) != arc):
                print(path)
                zip.write(path)


# leer de archivos comprimidos
with ZipFile(arc) as zip:
    print(zip.namelist)
