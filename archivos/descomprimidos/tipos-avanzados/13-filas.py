# FIFO First in First Out
# usar: deque, append() y popleft()

from collections import deque

# en una lista, el primero de la misma es el que sale
# si se borra el primer elemento, hay que cambiar la posicion del resto de los elementos
# El problema es cuando se tiene muchos elementos.
lista = [1, 2, 3, 4]

# se crea la fila a partir de deque
fila = deque(lista)

# se agregan mas elementos a la fila
fila.append(5)
fila.append(6)

# imprimo la fila
print(fila)

# elimino elemento de la izquierda
fila.popleft()
print(fila)

# Borrar elementos de la fila para
# chequear si la fila está vacia
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
if not fila:
    print("La fila está vacía")
else:
    print(fila)
