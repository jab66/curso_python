import csv
import os

# escribir
# with open("archivos/archivo.csv", "w", encoding='utf-8', newline='') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["id", "name"])
#     writer.writerow([1, "Jorge"])
#     writer.writerow([2, "Daniel"])

# leer
# with open("archivos/archivo.csv", "r", encoding='utf-8') as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)


# actualizar
with open("archivos/archivo.csv", "r", encoding='utf-8') as r, open("archivos/temp.csv", "w", encoding='utf-8', newline='') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1":
            writer.writerow([1, "Alejandro"])
        else:
            writer.writerow(linea)
os.remove("archivos/archivo.csv")
os.rename("archivos/temp.csv", "archivos/archivo.csv")
