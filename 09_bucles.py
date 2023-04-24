### Bubles, Ciclos, Loops ###

"""
WHILE
Este ciclo o bucle se cumple mientras la condición o sentencia cumpla un valor determinado
"""

mi_condicion_01 = 0

"""
El ciclo queda infinito, va a ejecutarse infiintas veces.
Este ciclo siempre es verdadero si no alteramos el valor de la variable.
Por tanto modificamos el ciclo para que la variable cambie cada vez que ingrese al ciclo.
"""

while (mi_condicion_01 <= 10):
    print(mi_condicion_01)
    mi_condicion_01 += 1
else:
    print("Ahora mi variable ya no ucmple la condición del While, es ", mi_condicion_01)

print("Este se ejecuta después del ciclo While")


# Es posible interrumpir un ciclo en un momento determinado con la instrucción break
mi_condicion_02 = 0

while (mi_condicion_02 < 20):
    mi_condicion_02 += 1
    print(mi_condicion_02)
    if (mi_condicion_02 == 6):
        print("Mi variable o condicion es igual a 15")
        break

    print("Mi variable o condicion es menor que 20")


"""
FOR
Este ciclo sirve para iterar cobre un listado de elementos.
También es posible que sea más libre, pero se debe dar un inicio, una comparación y un cambio
"""

mi_lista_01 = [35, 24, 62, 52, 30, 30, 17]

# La variable del for con la cual itera, puede tener cualquier nombre, por ejemplo elemento o la letra i
for element in mi_lista_01:
    print(element)

for i in mi_lista_01:
    print(i)

# Ciclo for para una tupla
mi_tupla_01 = (38, 1.65, "Manuel", "Castellanos", "Don Ricardo")
for element in mi_tupla_01:
    print(element)

# Ciclo for para un set
mi_set_01 = {"Manuel", "Castellanos", 38}
for element in mi_set_01:
    print(element)

# Ciclo for par aun diccionario (MOSTRARÁ LAS CLAVES PERO NO LOS VALORES)
mi_dicc_01 = {"Nombre": "Ricardo", "Apellido": "Castellanos", "Edad": 38, 1: "Python"}
for element in mi_dicc_01:
    print(element)

# Es posible iterar en los valores del diccionario así
for element in mi_dicc_01.values():
    print(element)

# Es posible detener el ciclo en un momento determinado con break
for element in mi_dicc_01:
    print(element)
    if (element == "Apellido"):
        break    