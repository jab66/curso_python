n1 = input("Ingresa primer numero = ")
n2 = input("Ingresa segundo numero = ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
la suma = {suma}
la resta = {resta}
la multiplicacion = {multi}
la division = {divi}
"""

print(mensaje)
