from pathlib import Path

path = Path("rutas")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("nuevo_nombre")

for p in path.iterdir():
    print(p)

archvos = [p for p in path.iterdir() if not p.is_dir()]
print(archvos)

archvos = [p for p in path.glob("01*.py")]
print(archvos)

# recursivo
archvos = [p for p in path.rglob("*.py")]
print(archvos)
# archvos = [p for p in path.glob("**/*.py")]
# print(archvos)
