### Operadores  aritméticos ###
print(3 + 5)
print(2 - 15)
print(4 * -8)
print(48 / 6)

# El operador % (modulo) indica el resto o residuo de la división entre dos números
print(5 % 2)
print(2 % 5)
print(3 % 3)

# El operador // (división) muestra la aproximación al entero más cercano por debajo
print(10 // 4)
print(10 // 3)

# El operador ** (potencia) realiza la potencia indicada
print(2 ** 3)
print(1 ** 10)
print(5 ** 4)

# Es posible utilizar operadores entre cadenas de texto, se pueden "sumar cadenas" o "multiplicar cadenas"
print("Hola " + "gente "+"seguimos avanzando con Python")

print("Bienvenido " * 3)


### Operadores de comparación ###
print(3 > 5)
print(3 < 5)
print(8 <= 15)
print(8 >= 15)
print(5 == 9)
print( 5 != 9)

# Es posible comparar dos cadenas, de acuerdo a el orden alfabético de sus letras
print("Hola" > "Bienvenido")
print("Hola" < "Bienvenido")

print("abc" < "aaa")
print("a" > "A")


### Operadores lógicos ###
# Se aplica la lógica de Boole, para determinar el valor de verdad de una sentencia o grupo de sentencias
"""
La conjunción Y: and (aplica entre dos o más sentencias)
La disyunción O: or (aplica entre dos o más sentencias)
La negación NO: not (aplica para una única sentencia)
"""

print(3 > 5 and "Hola" < "Bienvenido")
print(3 > 5 or "Hola" < "Bienvenido")
print(not 3 > 5 and "Hola" < "Bienvenido")
print(not 3 > 5 and not "Hola" < "Bienvenido")