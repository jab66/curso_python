mensaje_titulo = "Bienvenidos a la calculadora"
mensaje_salida = "Para salir escribe 'salir'"
mensaje_operaciones = "Las operaciones son suma, multi, div y resta"
operacion = ""
condicion = True
operacion_valida = True

print(mensaje_titulo)
print(mensaje_salida)
print(mensaje_operaciones)

resultado = input("Ingresa numero: ")
if resultado.lower() == "salir":
    condicion = False

while condicion:

    operacion = input("Ingresa operacion: ")
    if operacion.lower() == "salir":
        break

    numero = input("Ingresa numero: ")
    if numero.lower() == "salir":
        break

    if operacion == "suma":
        resultado = int(resultado) + int(numero)
    elif operacion == "multi":
        resultado = int(resultado) * int(numero)
    elif operacion == "div":
        resultado = int(resultado) / int(numero)
    elif operacion == "resta":
        resultado = int(resultado) - int(numero)
    else:
        print("Operacion no valida")

    print(f"El resultado es: {resultado}")
