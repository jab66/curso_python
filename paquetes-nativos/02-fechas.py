import time
from datetime import datetime

print(time.time())

fecha = datetime(2024, 7, 6)
ahora = datetime.now()

fechaStr = datetime.strptime("15/02/1967", "%d/%m/%Y")
fecha_dt = fecha.strftime("%d %m %Y")

print(fecha)
print(ahora)
print(fechaStr)
print(fecha_dt)

print(fecha > ahora)
