### Funciones ###

# Para crear una función en Python, se usa la palabra reservada: def

# Acá se define la función
def mi_funcion_01 ():
    print("Esta es la funcion 01")

# Acá llamamos a la función mi_funcion_01
mi_funcion_01()

# La podemos llamar cuantas veces sea necesario:
mi_funcion_01()
mi_funcion_01()
mi_funcion_01()
mi_funcion_01()

# Una función puede recibir y devolver valores

# Función que suma dos valores
def suma_dos_valores(valor_01, valor_02):
    print("La suma es: ", valor_01 + valor_02)

suma_dos_valores(16, 56)
suma_dos_valores(-15, 20)
suma_dos_valores(-85, 48)

# Podemos concatenar dos cadenas, puesto que "sumar" dos cadenas es concatenarlas
suma_dos_valores("su", "ma")
suma_dos_valores("pala", "bra")

# Función que divide dos valores
def divide_dos_valores(valor_03, valor_04):
    print("El cociente es:", valor_03, valor_04)

divide_dos_valores(5, 8)
divide_dos_valores(9, 3)
divide_dos_valores(152.2, 45.6)

"""
IMPORTANTE: Si una función recibe una cantidad de parámetros en su definición,
al momento de llamar a la función, debemos enviar EXACTAMENTE esa cantidad de parámetros
"""

# Para retornar valores desde una función, tenemos
def suma_con_retorno(valor_05, valor_06):
    return (valor_05+valor_06)

# En una variable asignamos el valor que retorna la función
resultado_funcion_con_retorno = suma_con_retorno(125, 985)
print("El return de la función es: ", resultado_funcion_con_retorno)

# Veamos que pasa cuando la funcion no tiene return
resultado_funcion_sin_retorno = suma_dos_valores(125, 985)
print("El return de la función es: ", resultado_funcion_sin_retorno) 

#
def mostrar_nombre(nombre, apellido):
    print(f"{nombre} {apellido}")

# Por defect, el orden en que se envian los párametros es el orden en que la función los usa
mostrar_nombre("Manuel", "Castellanos")
mostrar_nombre("Castellanos", "Manuel")
mostrar_nombre("Ricardo", "Castellanos")

# Es posible indicar el orden específico que queramos o necesitemos
mostrar_nombre(nombre="Manuel", apellido="Castellanos")
mostrar_nombre(apellido="Messi", nombre="Leonel")

# Podemos enviar parámetros de forma dinámica
# Con el asterisco (*parametro), indicamos que se envian uno o más parámetros a la función
def mostrar_textos(*texto):
    print(texto)

mostrar_textos("Hola", "Gente", "Aprendamos", "Python")

# Otra prueba combinando conceptos
# La siguiente función imprime todos los parámetros que recibe en mayúscula
def texto_mayuscula(*texts):
    for text in texts:
        print(text.upper())

texto_mayuscula("Hola", "Gente", "CURSO", "python", "BiEmVenIdos")