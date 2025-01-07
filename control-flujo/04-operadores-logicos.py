# and or not

gas = True
encendido = True

if gas and encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")


encendido = False
if gas and encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")

if gas or encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")

if gas or not encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")
