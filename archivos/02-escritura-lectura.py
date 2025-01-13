from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")

texto = archivo.read_text()
print(texto)

texto = archivo.read_text("utf-8").split("\n")
print(texto[0])

texto.insert(0, "Hola Mundo!!")
archivo.write_text("\n".join(texto), "utf-8")
