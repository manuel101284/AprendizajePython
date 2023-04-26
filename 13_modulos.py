### Modulos ###
"""
Un modulo es un archivo de código que puede ser utilizado por muchos otros archivos muchas veces.
Puede contener funciones, métodos, clases, etc.
"""
"""
TIP:
Si queremos llamar un archivo como modulo, el nombre del archivo NO puede empezar por números
"""
# Es posible accceder a otros ficheros  con la palabra import
import modulo

# Para llamar una función del modulo, llamamos el modulo, luego punto y la funcion requerida
modulo.suma_tres_numeros(100, 200, 300)

modulo.mostrarValor("Hola gente")

"""
Es posible importar solo una función o partes determinados de otro fichero. así:

from modulo import suma_tres_numeros
"""
from modulo import suma_tres_numeros, mostrarValor

suma_tres_numeros(-52, 45, -96)
mostrarValor("Importamos solo lo que se va a utilizar")

"""
Existen módulos propios del sistema para llamar y utilizar dentro de nuestro código
"""

# Ejemplo: el módulo math contiene funciones matemáticas más específicas
import math

# la constate pi
print(math.pi)

# la función pow(), potencia, eleva el primer valor al segundo valor
print(math.pow(2, 10))

from math import pi
print(pi)

# es posible darle un nombre o alias o lo que se importa:
from  math import pi as VALOR_PI
print(VALOR_PI)