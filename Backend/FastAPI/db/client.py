# Importat MongoClient desde pymongo, luego de instalar pymongo
# pip install pymongo
# Descargar la version Community de mongodb e instalarla (viene con mongo Compass)
# Crear la conecxión: mongodb://localhost


from pymongo import MongoClient

""" BASE DE DATOS LOCAL """
# Como parámetro podemos pasarle a MongoClient la url de nuestra base de datos remota
# db_client = MongoClient()
# db_client = MongoClient().local

""" BASE DE DATOS REMOTA """
db_client = MongoClient("mongodb+srv://manuel101284:manuel101284@cluster0.8ilzqui.mongodb.net/?retryWrites=true&w=majority").test

