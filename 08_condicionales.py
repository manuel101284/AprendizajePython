### Condicionales ###

# Un condicional  evalua el valor de verdad de una comparación, una sentencia o una variable (TRUE o FALSE)
mi_condicion = True

if mi_condicion: # Es equivalente escribir if mi_condicion == True
    print("Este mensaje se muestra porque la variable es verdadera")

print("Aquí continua la ejecución del código")

"""
Aquellas instrucciones que se ejecutan al interior del condicionla van indentadas a la derecha.
Las instrucciones que NO ESTÉN indentadas, se ejecutan por fuera del condicional
"""

# Veamos como se comporta comparando una variable con un valor
variable_01 = 5*7

if variable_01 == 10:
    print("Este if se ejecuta porque variable_01 es igual a 10")
if variable_01 > 10 and variable_01<30:
    print("Este if se ejecuta porque variable_01 es mayor que 10")
elif variable_01 > 30 or (variable_01<10 and variable_01 > 1):
    print("Este if se ejecuta porque variable_01 es mayor que 30 o menor que 10 pero mayor que 1")
elif variable_01 ==1 :
    print("Este if se ejecuta porque variable_01 es igual a 1")
else:
    print("Este if se ejecuta porque variable_01 es menor que 1")

print("La ejecución sigue acá")


"""
RECORDATORIO:
-   La conjunción o and o y (and) es verdadera cuando cada sentencia (de dos o más) son verdaderas.
-   Si una de la sentencias es false, toda la conjunción resulta falsa

-   La Disyunción o el o (or) es verdadera cuando al menos una se las sentencias (de dos o más) es verdadera.
-   Para resultar falsa, se require que TODAS las sentenias sean falsas
"""

# Veamos como se comporta el condicional con cadenas
#Lo primero que hará el condicional es verificar si tiene algo guardado la cadena, que no sea vacía.

mi_string_01 = ""

if mi_string_01:
    print("Cadena vacía")

"""
RECORDATORIO:
-   La negación cambia el valor de verdad de una sentencia o variable
"""
# Si negamos el if, resulta verdadera la sentencia
if not mi_string_01:
    print("Cadena Vacía, pero resultado del if es verdadero")

mi_string_02 = "Hola gente"
if mi_string_02:
    print("Cadena NO vacía")