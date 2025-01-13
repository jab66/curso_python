try:
    numero = int(input("Ingresa un número: "))
    # cualquier cosa que no compilec (descomentar para que falle por excepcion)
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"Exception: {type(e)} {e}")
