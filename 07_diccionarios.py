### Diccionarios ###

mi_dic_01 = dict()
print(type(mi_dic_01))

# Se estructura siguiendo la forma CLAVE -> VALOR
mi_dic_02 = {"Nombre": "Manuel", "Apellido": "Castellanos", "Edad": 38, 1: "Python"}
print(mi_dic_02)

mi_dic_01 = {
    "Nombre": "Manuel",
    "Apellido": "Castellanos",
    "Edad": 38,
    "Lenguajes": {
        "Python",
        "JavaScript"
    },
    1: 1.65,
}
print(mi_dic_01)

"""
La estructura de un diccionario es similar a un JSON
"""

# Es posible conocer la longitud o tamaño de un diccionario
print(len(mi_dic_02))
print(len(mi_dic_01))

# Es posbible conocer el valor de un clave llamando la clave del diccionario
print(mi_dic_01[1])
print(mi_dic_01["Nombre"])

# También es posible editar o cambiar el vlaor de una clave
mi_dic_01["Nombre"] = "Ricardo"
print(mi_dic_01["Nombre"])

# Se pueden agregar un nuevo campo (Clave) a un diccionario, de esta forma
mi_dic_01["Ciudad"] = "Bogotá"
print(mi_dic_01)

# Es posible eliminar un campo de un diccionario, de esta forma
del mi_dic_01["Ciudad"]
print(mi_dic_01)

# Se puede saber si una Clave existe dentro de un diccionario
print("Apellido" in mi_dic_01)
print("Color" in mi_dic_01)


### Algunas funciones o métodos ###

# Obtener cada item (CLAVE-VALOR) de un diccionario
print(mi_dic_01.items())

# Obtener solamente las CLAVES o Keys de un diccionario
print(mi_dic_01.keys())

# Obtener solamente los VALORES o values de un diccionario
print(mi_dic_01.values())

# Es posible crear un diccionario con unas CLAVES determinadas,así:
mi_dic_03 = dict.fromkeys(("Nombre", "Apellido", 1))
print(mi_dic_03)

# Es posible creear un diccionario a partir de una lista, los elementos de la lista serán las keys
mi_lista_01 = ["Nombre", 1, "Ciudad"]
mi_dic_04 = dict.fromkeys(mi_lista_01)
print(mi_dic_04)

#  Es posible crear un diccionario vacio a partir de uno existente
mi_dic_05 = dict.fromkeys(mi_dic_01)
print(mi_dic_05)
