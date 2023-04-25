### Excepciones ###
"""
Vamos a ver como es el manejo de errores en Python

Para controlar errores, pondremos esto dentro de un bloque: try - except - else - finally
"""

# Veamos un ejemplo
num_01 = 2
num_02 = 7

print(num_01 + num_02)

num_03 = "2"
num_04 = 7

# Al ejecutae la siguiente instrucción, tendremos un error y se para el programa por completo
# print(num_03 + num_04)

# Usando try - except, "captura" el error y continua la ejecución del código
try:
    print(num_03 + num_04)
    print("Todo ha ido bien")
except:
    # El except se ejecuta si se encuentra una excepción o error
    print("Se ha producido un error")

# try - except - else
num_05 = 2
num_06 = 45

try:
    print(num_05 + num_06)
    print("Todo ha ido bien")
except:
    print("Ha sucedido algo inesperado")
else:
    # El else se ejecuta si no se encuentra excepcion o error
    print("La ejecucon continua :)")

# try - except - else - finally
num_07 = 87
num_08 = 25

try:
    print(num_07 + num_08)
    print("Hemos tenido exito")
except:
    print("Se ha presentado una EXCEPCION")
else:
    print("El programa se sigue ejecutando")
finally:
    # finally se ejecuta sea que se presente una excepcion o no
    print("Continuamos con la ejecucion")

""" 
TIP:
Al usar try siempre debe ir except, mientras que else y finally son opcionales
"""

# Captura de excepciones por tipo o por valor

num_09 = "2" 
num_10 = 73

try:
    print(num_09 + num_10)
    print("Todo bien")
except ValueError:
    print("se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

"""
TIP:
Existen diferentes tipos de excepciones o errores, en el try- except, podemos definir cual controlar
"""

# Captura dela información de la excepción
num_11 = 54
num_12 = "Ricardo"

try:
    print(num_11 + num_12)
    print("Okey")
except ValueError as error: # error captura la información del error si es ValueError
    print(error)
except Exception as excepcion: # excepcion captura la información de un error general
    print(excepcion)
