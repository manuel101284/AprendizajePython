### Python Package Manager ###
"""
Gestor de paquetes para Python
usaremos: pip

Para instalar:
pip install pip

Para actualizar:
pip install --upgrade pip
"""

#PIP https://pypi.org
# pip install ...
# pip uninstall ...
# pip --version

import numpy # pip install numpy / pip uninstall numpy

print(numpy.version.version)

numpy_array_01 = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array_01))

print(numpy_array_01 * 3)
print(numpy_array_01 * 0.5)


import pandas # pip install pandas / pip uninstall pandas


import requests # pip install requests / pip uninstall requests

response_01 = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response_01)
print(response_01.status_code)
print(response_01.json())


# Arithmetics Package
from MyPackages import arithmetics
print(arithmetics.sum(5, 9))
