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

year_2023 = datetime(2023, 1, 1)

def mostrar_fecha(date):
    print("año", date.year)
    print("mes", date.month)
    print("día", date.day)
    print("hora", date.hour)
    print("minuto", date.minute)
    print(date.timestamp())

mostrar_fecha(year_2023)

# tIme ofrece otras funciones del modulo datetime
# Es un objeto vacío, que no se asocia a nada, sirve para encapsular tiempos
# Debe ser llenado con algún dato
from datetime import time

tiempo_actual = time()
print(tiempo_actual)
print(tiempo_actual.hour)
print(tiempo_actual.minute)
print(tiempo_actual.second)

# Inicializado con datos
tiempo_actual = time(15, 25, 8)
print(tiempo_actual)
print(tiempo_actual.hour)
print(tiempo_actual.minute)
print(tiempo_actual.second)

# date ofrece otras funciones del modulo datetime
# Debe ser inicializado siempre, con datos que deseemos o con algun dato automático
from datetime import date

# Al iniciar con la fecha del día de hoy
fecha_ahora = date.today()
print(fecha_ahora)
print(fecha_ahora.year)
print(fecha_ahora.month)
print(fecha_ahora.day)

# Al iniciar con datos que queremos 
fecha_ahora = date(2020, 5, 14)
print(fecha_ahora)
print(fecha_ahora.year)
print(fecha_ahora.month)
print(fecha_ahora.day)

# Operaciones con Fechas (SOLO SI ESTÁN DEFINIDAS DE LA MISMA FORMA)
diff = year_2023 - fecha_actual
print(diff)

# El timedelta se usa sobretodo para trabajar con FRANJAS DE FECHAS
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10 )
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)