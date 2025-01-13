def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    print(resultado)


suma(1, 2)
suma(3, 5, 10)
suma(10, 20, 30, 40, 50)
