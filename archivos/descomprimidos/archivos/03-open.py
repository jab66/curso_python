from io import open

# escritura
# texto = "Hola Mundo!"

# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# con with nos evitamos de tener que cerra el archivo
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     # carga todo el archivo en memoria
#     print(archivo.readlines())

#     # retornar a un caracter especifico
#     archivo.seek(0)

#     # carga las lineas del archivo de a una
#     for linea in archivo:
#         print(linea)


# agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("\nChau Mundo !")
# archivo.close()


# lectura y escritura
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Open World!\n"
    archivo.writelines(texto)
