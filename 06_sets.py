### Sets (Conjuntos) ###
# Es un "array" en se esencia

mi_set_01 = set()
mi_set_02 = {}

print(type(mi_set_01))
print(type(mi_set_02)) # En un comienzo es un diccionario, porque no está inicializado

mi_set_02 = {"Manuel", "Castellanos", 38}
print(type(mi_set_02)) # Al inicializarlo, será un set

# Podemos conocer la longitud de un set
print(len(mi_set_02))

"""
UN SET NO ES UNA ESTRUCTURA ORDENADA
"""
# Podemos añadir valores a un set
mi_set_02.add("Caillou")
print(mi_set_02)

"""
Al agregar un valor que ya existe en los valores del set, no lo agrega
Por tanto UN SET NO ADMITE VALORES REPETIDOS EN SUS ELEMENTOS
"""
mi_set_02.add("Castellanos") # "Castellanos" ya existe, por tanto NO SERÁ AÑADIDO
print(mi_set_02)

# Es posible probar si existe un valor o elemento dentro del set
print("Manuel" in mi_set_02)
print("Ricardo" in mi_set_02)

# Es posible eliminar un elemento de un set
mi_set_02.remove("Manuel")
print(mi_set_02)

# Con clear() es posible limpiar todo el set, es decir, borrar todos los elementos del set
mi_set_02.clear()
print(mi_set_02)

# Con del eliminamos por completo el set, deja de existir (ni siquiera está definido como vacío)
mi_set_99 = {}
mi_set_99 = {"Blue", 3.14, "Red", 2.71, "White", 10}
print(mi_set_99)
del  mi_set_99 # El set indicado deja de existir

# Es posible crear una lista a partir de un set
mi_set_01 = {"Ricardo", "Castellanos", 38, 1.65}
mi_lista_01 = list(mi_set_01)
print(mi_set_01)
print(type(mi_set_01))

print(mi_lista_01)
print(type(mi_lista_01))

# Es posible concatenar o unir dos sets con union
mi_set_03 = {"HTML", "CSS", "JavaScript", "Python"}
mi_set_04 = mi_set_01.union(mi_set_03)
print(mi_set_04)

"""
ACLARACIÓN: al momento de utilizar union() se concatenan los sets, no se repiten elementos.
Es decir que no se guardan elementos repetidos.
"""
mi_set_05 = {"Python", 2023}
mi_set_06 = mi_set_05.union(mi_set_04)
print(mi_set_06)

# Se puede calcular o encontrar la "diferencia" entre elementos de dos sets
print(mi_set_06.difference(mi_set_01))
print(mi_set_06.difference(mi_set_04))
print(mi_set_03.difference(mi_set_01))
print(mi_set_01.difference(mi_set_03))
print(mi_set_01.difference(mi_set_01))

# Es posible saber que elementos se repiten entre dos sets
print(mi_set_01.intersection(mi_set_01))
print(mi_set_01.intersection(mi_set_03))
print(mi_set_04.intersection(mi_set_05))
print(mi_set_01.intersection(mi_set_06))