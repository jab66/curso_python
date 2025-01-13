from pathlib import Path


# en windows
# Path(r"c:\temp\curso de python")

# para linux
# Path("/usr/bin")

# ruta relativa
path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

# cambiar el nombre
p = path.with_name("hello.py")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
