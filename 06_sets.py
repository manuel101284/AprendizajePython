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
Al agregar un vlaor que ya existe en los valores del set, no lo agrega
Por tanto UN SET NO ADMITE VALORES REPETIDOS EN SUS ELEMENTOS
"""
mi_set_02.add("Castellanos") # "Castellanos" ya existe, por tanto NO SERÁ AÑADIDO
print(mi_set_02)




