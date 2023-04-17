# Variables
"""
Se sigue la convención snake_case, es decir,
las variables van en minúsculas y si son varias palabras, se separan con guión bajo: _
"""

mi_variable = "Esta cadena de texto es una variable"
print(mi_variable)

numero_01 = 1984
print(numero_01)

real_01 = 3.1415926
print(real_01)

variable_booleana = True
print(variable_booleana)

# CONCATENACIÓN DE VARIABLES
print(mi_variable, numero_01, real_01, variable_booleana)
print(type(print(mi_variable, numero_01, real_01, variable_booleana)))

variable_entero_a_texto = str(numero_01)
print(variable_entero_a_texto)
print(type(variable_entero_a_texto))

# La función len() muestra la longitud de una variable
variable_texto = "Esta es una cadena de texto"
len(variable_texto)
print(len(variable_texto))

# Es posible nombrar y asginar varias variables al mismo tiempo en una sola línea
nombre, apellido, mote, edad = "Manuel", "Castellanos", "Caillou", 99
print(nombre)
print(apellido)
print(mote)
print(edad)
print ("Mi nombre es ",nombre, apellido, "tengo ", edad, "años, y a veces me dicen ", mote)

# Es posible esperar datos del usuario
usuario_nombre = input("Ingrese su nombre: ")
usuario_edad = input("ingrese su edad: ")
print(usuario_nombre)
print(usuario_edad)
print("Bienvenido ",usuario_nombre,", podemos ver que tienes ",usuario_edad,"años")

"""
Puesto que Python no tienen un tipado fuerte,
es decir, es posible cambiar durante el código el tipo de una variable,
se recomienda tener cuidado al momento de manipular las variables.
O forzar el tipo de las variables
"""

# Indicar  el tipado o tipo de una variable
mi_email: str = "manuel101284@gmail.com"
print(mi_email)
mi_email = 84
print(type(mi_email))
