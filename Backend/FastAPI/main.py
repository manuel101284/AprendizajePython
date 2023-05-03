# Importamos el módulo fastapi que recien instalamos

from fastapi import FastAPI

# En una variable vamos a guardar la clase que usaremos
app = FastAPI()

"""
Para abrir el servidor, tecleamos: uvicorn main:app --reload
"""

# Declaramos la instacia para hacer una petición al servidor, con get, y una función asincrona
@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/url")
async def urlrepositorio():
    return { "url_repositorio": "https://github.com/manuel101284/AprendizajePython"}

"""
FastAPI genera documentación en swagger automáticamente
Para consultarla, tecleamos en nuestro navegador:
http://127.0.0.1:8000/docs

Otra opción para la documentación es:
http://127.0.0.1:8000/redoc
"""

