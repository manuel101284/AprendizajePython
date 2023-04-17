### Cadenas de texto (Strings) ###
# Se pueden usar comillas dobles o comillas sencillas

cadena_de_texto_1 = "Esta es una cadena"
cadena_de_texto_2 = 'Esta es otra cadena de texto'

# Con len() sabemos la longitud de cada cadena de texto
print(len(cadena_de_texto_1))
print(len(cadena_de_texto_2))

# + añade o concatena dos o más cadenas de texto
print(cadena_de_texto_1 + " " + cadena_de_texto_2)

# \n da un salto de línea
nueva_cadena = "Esto es un String\ncon un salto de línea incrustado"
print(nueva_cadena)

# \t da una tabulación 
otra_cadena = "Una nueva cadena\tcon tabulación incrustada"
print(otra_cadena)

# Dar formato a una cadena
nombre = "Manuel"
apellido = "Castellanos"
edad = 99

# print("Mi nombre es ", nombre, apellido, "y tengo ", edad)
print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido, edad))
print("Mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad))

# Inferencia de datos
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

# Desempaquetar caracteres
lenguaje = "Python"
letra_1, letra_2, letra_3, letra_4, letra_5, letra_6 = lenguaje
print(letra_1) 
print(letra_2)
print(letra_3)
print(letra_4)
print(letra_5)
print(letra_6)

# División
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[:4]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2]
print(lenguaje_slice)

# Reverse
reverse_lenguaje = lenguaje[::-1]
print(reverse_lenguaje)

# Funciones
print(lenguaje.capitalize())    # La pirmera letra la pone en mayúscula
print(lenguaje.upper())     # Todas las letras las pone en mayúscula    
print(lenguaje.count("t"))      # Cuenta cuantas veces aparece un caracter o letra
print(lenguaje.isnumeric())     # Verifica si la cadena es un número o no
print("1".isnumeric())      # Verifica si la cadena es un número o no
print(lenguaje.lower())     # Todas las letras las pone en minúscula
print(lenguaje.upper().isupper())       # Primero pone todo en mayúscula, luego verifica si todo está en mayúscula
print(lenguaje.startswith("Jy"))     # Verifica si la cadena empieza por una letra o cadena determinada