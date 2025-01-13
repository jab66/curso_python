try:

    numero = int(input("Ingresa un número: "))

except ValueError as ve:
    print(f"ValueError: {ve}")

except Exception as e:
    print(f"Exception: {type(e)} {e}")

# no existen errores
else:
    print("No ocurrio ningun error")

# se ejecuta siempre
finally:
    print("Se ejecutó finally!!")
