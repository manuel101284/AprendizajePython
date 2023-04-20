### Tuplas ###

mi_tupla_01 = tuple()
mi_tupla_02 = ()

mi_tupla_01 = (38, 1.65, "Ricardo", "Castellanos")
print(mi_tupla_01)
print(type(mi_tupla_01))

# Se puede recorrer una tupla de la misma forma que una lista
# En sentido ascendete desde (0) hasta (N-1)
# En sentido descendente desde (-1) hasta (-N)

print(mi_tupla_01[0])
print(mi_tupla_01[1])
print(mi_tupla_01[2])
print(mi_tupla_01[3])

print(mi_tupla_01[-1])
print(mi_tupla_01[-2])
print(mi_tupla_01[-3])
print(mi_tupla_01[-4])

# Se pueden contar cuantas veces aparece un valor en los elementos con count()
print(mi_tupla_01.count("Ricardo"))
print(mi_tupla_01.count("Manuel"))
print(mi_tupla_01.count(38))

# Es posible conocer el primer índice que contenga un valor determinado dentro de la tupla
print(mi_tupla_01.index("Ricardo"))

"""
Una Tupla se define con unos valores determinados y NO ES POSIBLE CAMBIARLOS
Estos valores serán fijos durante el código,
Tampoco es posible añadirlo índices o quitar índices de la Tupla
LA TUPLA ES INMUTABLE
"""

# Se puede crear una nueva tupla concatenando dos o más que ya existen
mi_tupla_02 = (1, 2, 3, 4, 5)
print(mi_tupla_02 + mi_tupla_01)

mi_tupla_03 = mi_tupla_01 + mi_tupla_02
print(mi_tupla_03)

# Es posible mostrar  u obtener fragementos de una tupla
print(mi_tupla_03[1:3])
print(mi_tupla_03[2:6])
print(mi_tupla_03[3:8])
print(mi_tupla_03[5:])
print(mi_tupla_03[:3])

"""
PARA CREAR UNA TUPLA MUTABLE, PODEMOS CREAR UNA LISTA A PARTIR DE LA TUPLA
"""
# Crear una lista a partir de una tupla
mi_tupla_mutable = list(mi_tupla_03)
print(mi_tupla_03)
print(type(mi_tupla_03))

print(mi_tupla_mutable)
print(type(mi_tupla_mutable))

mi_tupla_mutable.insert(2, "Blue")
print(mi_tupla_mutable)

# Es posible borrar una tupla, con todo su contenido, ya no existe la tupla (Contradictorio)
del mi_tupla_01

