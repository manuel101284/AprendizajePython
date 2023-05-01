### Error Types ###

"""
Veremos como capturar diferentes tipos de error y comunicarlo para dar solución a ello
"""
"""
TIP:
Las líneas comentadas muestran el error, al quitar el comentario, se podrá ver el error
"""

# SyntaxError

# La siguiente instrucción muestra qu falta algo en el print, los parentesis
# print "BIenvenidos todos"

# Corregida
print("¡Bienvenidos todos!")



# NameError

# La siguiente instrucción pretende mostrar la variable var_01, pero dicha variable no existe aún
# print(var_01)

# Corregida
var_02 = "Aprendiendo Python"
print(var_02)



# indexError 

list_01 = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
# La siguiente instrucción pretende mostrar un indice que está por fuera o excee los que existen en la variable
#print(list_01[5]) # El indice 5 no existe en la lista list_01

# Corregida
print(list_01[0])
print(list_01[4])
print(list_01[-5])
print(list_01[-1])



# ModuleNotFounderError

# La siguiente línea muestra un error al importa un módulo que no existe
#import maths # El moduló maths no existe

#Corregida
import math



# AttributeError

# La siguiente línea muestra el atributo PI, que no existe en el módulo math
# print(math.PI)

# Corregida
print(math.pi)



# KeyError
my_dict_01 = {"Nombre": "Manuel", "Apellido": "Castellanos", "Edad": 38, 1: "Python"}

# Las siguientes líneas pretenden acceder a una clave que no existe en la estructura
# print(my_dict_01["Apelido"])
# print(my_dict_01["Alias"])

# Corregida
print(my_dict_01["Apellido"])



# TypeError

# La siguiente línea pretende acceder a un indice dando un tipo erróneo en el parámetro
#print(list_01["Nombre"]) # El inidice "Nombre" no existe en list_01
#print(list_01["1"]) # El indice "1" no existe en la lista

#Corregida
print(list_01[1])



# ImportError

# La siguiente línea pretende importar sqrtt  desde el modulo math
# from math import sqrtt as raiz # No existe un componente sqrtt
# print(raiz(16))


# Corregida
from math import sqrt as raiz
print(raiz(16))



#ValueError
my_int = "10 años"

# La siguiente línea pretende transformar una variable a un tipo que no es posible
# print(int(my_int)) # my_int es una cadena, que no puede ser convertida en entero

# Corregida
print(my_int)



# ZeroDivisionError

# La siguiente línea pretende hacer una división entre 0
# print(17/0)

# Alternativas
print(0/17)
print(17/0.000001)