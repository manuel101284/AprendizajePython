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