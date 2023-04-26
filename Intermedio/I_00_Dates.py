### Dates ###

# Importamos datetime desde el módulo datetime (fecha y hora)
from datetime import datetime

# Una fecha es un tipo de date que representa una ubicación temporal
# Crear una fecha actual
fecha_actual = datetime.now()

# A partir del objeto fecha_actual, llamamos algunas de sus características
print("año", fecha_actual.year)
print("mes", fecha_actual.month)
print("día", fecha_actual.day)
print("hora", fecha_actual.hour)
print("minuto", fecha_actual.minute)
print("segundo", fecha_actual.second)

# Con timestamp tenemos el formato único de una fecha particular universal desde 1970*
timestamp = fecha_actual.timestamp()
print(timestamp)

