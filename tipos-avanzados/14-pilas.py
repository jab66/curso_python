# LIFO  Last in First out
# el comportamiento es como el de una lista pero para que se comporte como
# una pila, solo hay que usar los metodos append() y pop()

# historial de navegacion
pila = ["Inicio", "Productos", "Seleccionar producto"]

# agrego elementos a la pila
pila.append("Ir al carrito")
pila.append("Comprar")

print(pila)

# eliminar un elemento dentro de la pila
# usar lista.pop()
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)

# ultimo elemento de la pila
print(pila[-1])

# eliminar el resto de los elementos de la pila
# chequear si la pila est+a vacía
pila.pop()
pila.pop()
pila.pop()
pila.pop()
if not pila:
    print("La pila está vacía")
else:
    print(pila)
