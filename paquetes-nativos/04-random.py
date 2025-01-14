import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(random.random(),
      random.randint(1, 10),
      lista,
      random.choice(lista2),
      random.choices(lista2, k=2),
      random.choices("abcdefgh", k=2),
      "".join(random.choices("abcdefgh", k=2))
      )

chars = string.ascii_letters
digitos = string.digits
puntuacion = string.punctuation
seleccion = random.choices(chars + digitos + puntuacion, k=16)
print(seleccion)


password = "".join(seleccion)
print(password)
