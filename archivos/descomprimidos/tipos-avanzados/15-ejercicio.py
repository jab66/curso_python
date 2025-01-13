# Funcion que retorna un string sin espacios en blanco

# Contar en un diccionario cuanto se repiten los caracteres de un string

# Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista
# que contiene tuplas

# De un listado de tuplas, devolver las tuplas que tengan el mayor valor

# Crear un mensaje que diga "Los caracteres que mas se repiten con 4 repeticiones son:"

from pprint import pprint

string = "Hola mundo este es mi string"


def quitar_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    retorno = {}
    for char in lista:
        if char in retorno:
            retorno[char] = retorno[char] + 1
        else:
            retorno[char] = 1
    return retorno


def ordenar(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crear_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje = mensaje + f"- {key} con {valor} repeticiones \n"
    return mensaje


sinEspacios = quitar_espacios(string)
contados = cuenta_caracteres(sinEspacios)
ordenados = ordenar(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crear_mensaje(mayores)

print(string, sinEspacios)
pprint(contados, width=1)
print(ordenados)
print(mayores)
print(mensaje)
