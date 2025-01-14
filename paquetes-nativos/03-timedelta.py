from datetime import datetime, timedelta

fecha1 = datetime(2024, 1, 1)
fecha2 = datetime(2024, 3, 1)

delta = fecha2 - fecha1
print(delta)
print("dias ", delta.days)
print("segundos ", delta.seconds)
print("total segundos", delta.total_seconds())

fecha1 = datetime(2024, 1, 1) + timedelta(weeks=1)
print(fecha1)
