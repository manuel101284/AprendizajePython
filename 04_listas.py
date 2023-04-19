### Listas ###

mi_lista_01 = list()
mi_lista_02 = []

print(len(mi_lista_01)) # Me muestra la longitud actual de la lista

mi_lista_01 = [35, 24, 62, 52, 30, 30, 17]

print(len(mi_lista_01)) # Me muestra la longitud actual de la lista
print(mi_lista_01) # Me muestra el contenido de la lista
print(type(mi_lista_01)) # Me muestra el tipo de dato que es mi_lista_01


mi_lista_02 = [38, 1.65, "Manuel", "Castellanos"]

print(len(mi_lista_02))
print(mi_lista_02)

print(type(mi_lista_02))

# Si la longitud de la lista es N, en sentido ascendente tenemos del índice (0) al (N-1)
# Si la longitud de la lista es N, en sentido descendente tenemos del índice (-1) al (-N)

# Imprime las posiciones de la lista del primer índice (0) al último (3)
print(mi_lista_02[0])
print(mi_lista_02[1])
print(mi_lista_02[2])
print(mi_lista_02[3])

# Imprime las posiciones de la lista del último índice (-1) al primero (-4)
print(mi_lista_02[-1])
print(mi_lista_02[-2])
print(mi_lista_02[-3])
print(mi_lista_02[-4])

# El método count() retorna cuantas veces está un elemento dentro de una misma lista
print(mi_lista_01.count(30))
print(mi_lista_02.count("Manuel"))

# Es posible guardar cada índice de una lista en variables separadas, debe coincidir el total de variables con el total de índices
edad, estatura, nombre, apellido = mi_lista_02
print(edad)
print(estatura)
print(nombre)
print(apellido)

num_1, num_2, num_3, num_4, num_5, num_6, num_7 = mi_lista_01[0], mi_lista_01[1], mi_lista_01[2], mi_lista_01[3], mi_lista_01[4], mi_lista_01[5], mi_lista_01[6]
print(num_1)
print(num_2)
print(num_3)
print(num_4)
print(num_5)
print(num_6)
print(num_7)

# Es posible mostrar el contenido de dos listas al tiempo
print(mi_lista_01 + mi_lista_02)

# Es posible concatenar listas, así
lista_concatenada_01 = mi_lista_01 + mi_lista_02 
print(lista_concatenada_01)

# El método append() agrega un elemento a la lista
mi_lista_02.append("Caillou")
print(mi_lista_02)

# El método insert() inserta un elemento en la lista en una posición específica (la lista aumenta su tamaño)
mi_lista_02.insert(1, "Blue")
print(mi_lista_02)

# Es posible modificar directamente un índice la lista, así
mi_lista_02[1] = "Red"
print(mi_lista_02)

# El método remove() elimina el primer elemento en la lista que tenga el valor indicado
mi_lista_02.remove("Red")
print(mi_lista_02)

# El método pop() elimina (desapila) el índice de la lista que se le indique, por defecto será el último
mi_lista_01.pop()
print(mi_lista_01)

mi_elemento_pop = mi_lista_01.pop(1)
print(mi_elemento_pop)
print(mi_lista_01)

# El método copy() copia la lista
mi_lista_03 = mi_lista_02.copy()
print("Lista 2: ", mi_lista_02)
print("Copia de Lista 2: ", mi_lista_03)

# Con del lista[indice] elimina el indice indicado de la lista
del mi_lista_01[2]
print(mi_lista_01)

# El método clear limpia la lista por completo
copia_lista_01 = mi_lista_01.copy()
mi_lista_01.clear()
print(mi_lista_01)
print(mi_lista_03)

# Es posible invertir la lista, con el método reverse()
mi_lista_03.reverse()
print(mi_lista_03)

# El método sort() permite ordenar de menor a mayor los valores de la lista
copia_lista_01.sort()
print(copia_lista_01)

# Es posible mostrar u obtener fragmentos de una lista indicando los índices de comienzo y fin
print(copia_lista_01[0:2])
print(copia_lista_01[0:1])
print(copia_lista_01[1:2])
print(copia_lista_01[2:3])
print(copia_lista_01[1:3])
print(copia_lista_01[0:3])
print(copia_lista_01[:2])
print(copia_lista_01[2:])
