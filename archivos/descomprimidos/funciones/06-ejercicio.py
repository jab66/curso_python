# def es_palindromo(texto: str):
#     invertido = ""
#     for letra in reversed(texto):
#         invertido = invertido + letra
#     invertido = invertido.replace(" ", "")

#     if invertido == texto.replace(" ", ""):
#         return True
#     else:
#         return False

def limpiar_espacios(texto):
    return texto.replace(" ", "")


def invertir_texto(texto):
    texto_invertido = ""
    for letra in texto:
        texto_invertido = letra+texto_invertido
    return texto_invertido


def es_palindromo(texto):
    texto_sin_espacios = limpiar_espacios(texto)
    texto_alreves = invertir_texto(texto_sin_espacios)
    return texto_sin_espacios.lower() == texto_alreves.lower()


print("abba", es_palindromo("abba"))
print("amo la paloma", es_palindromo("amo la paloma"))
print("hola mundo", es_palindromo("hola mundo"))
print("reconocer", es_palindromo("reconocer"))
print("AMO LA paloma", es_palindromo("AMO LA paloma"))
print("somos o no somos", es_palindromo("somos o no somos"))
