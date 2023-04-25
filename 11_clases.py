### Clases ###
"""
Una clase agrupa funciones y objetos que tienes unas características comunes.
Todo lo que encierre una clase va a cumplir con la misma lógica

Tip: Para nombrar las clases seguimos la convención CamelCase.
Es decir, la primera letra de cada palabra va en mayúscula
"""


class MiPersona:
        # Con la instrucción pass, el código omite que la clase no tenga nada a su interior
    pass 


print(MiPersona)
print(MiPersona())

# Es posible enviar parámetros a la clase y crear un objeto con esos mismos parámetros
class Persona01:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

mi_persona01 = Persona01("Manuel", "Castellanos")
print(mi_persona01.nombre)
print(mi_persona01.apellido)
print(f"{mi_persona01.nombre} {mi_persona01.apellido}")

# También se puede enviar los parámetros y crear un objeto con un solo parámetro en su interior
class Persona02:
    def __init__(self, nombre, apellido, alias = "Sin alias"):
        self.nombre_completo = f"{nombre} {apellido} ({alias})"

    def caminar(self):
        print(f"{self.nombre_completo} Esta caminando")

mi_persona02 = Persona02("Ricardo", "Castellanos")
print(mi_persona02.nombre_completo)
mi_persona02.caminar()

mi_persona03 = Persona02("James", "Bond", "007")
print(mi_persona03.nombre_completo)
mi_persona03.caminar()

# Luego de crear el objeto es posible cambiarlo por completo. Así
mi_persona03.nombre_completo = "Jon Doe Desconocido"
print(mi_persona03.nombre_completo)
mi_persona03.caminar()

# Al declarar el objeto con self.__caracteristica, esto será privado y no es posible acceder a él
# Para acceder a él, usamos el método get, sin embargo, el objeto NO se dejará modificar
class Persona03:
    def __init__(self, nombre, apellido, alias = "No tiene"):
        self.__nombre_completo = f"{nombre} {apellido} ({alias})"

    def comer (self):
        print(f"{self.__nombre_completo} come en restaurante")

    def get_nombre_completo(self):
        return self.__nombre_completo

mi_persona04 = Persona03("Leonel", "Messi", "La Pulga")
print(mi_persona04.get_nombre_completo())
