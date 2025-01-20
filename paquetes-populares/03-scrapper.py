import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path

# una sola pagina

# url = "https://stackoverflow.com/questions"
# respuesta = requests.get(url)
# texto = respuesta.text
# soup = BeautifulSoup(texto, "html.parser")

# preguntas = soup.select(".s-post-summary")
# print(preguntas[0])
# print(preguntas[0]["data-post-id"])

# for pregunta in preguntas:
#     titulo = pregunta.select_one(".s-link").get_text()
#     usuario = pregunta.select_one(".s-user-card--link").get_text()
#     print(f"({usuario.strip()}) - \n{titulo.strip()}")


# multiples paginas

url = ""
rango = 1
paged = "/questions"

for numero in range(rango):

    preguntas_pagina = 0

    url = f"https://stackoverflow.com{paged}"
    respuesta = requests.get(url).text
    soup = BeautifulSoup(respuesta, "html.parser")
    preguntas = soup.select(".s-post-summary")

    datos = []

    for pregunta in preguntas:

        # Este codigo permite obtener el nombre de la pregunta y el usuario que la hizo
        titulo = pregunta.select_one(".s-link").get_text().strip()
        usuario = pregunta.select_one(".s-user-card--link").get_text().strip()

        item = {
            "usuario": usuario,
            "titulo": titulo
        }

        datos.append(item)

    with open("paquetes-populares/stackoverflow1.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    if rango > 1:
        next = soup.select(".s-pagination--item")
        for proximo in next:
            try:
                if (''.join(proximo["rel"])) == 'next':
                    paged = proximo["href"]
            except:
                pass
