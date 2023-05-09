from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Inicia el servidor con: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id= 1, name="Manuel", surname="Castellanos", url="http://manuel.com", age=38),
            User(id= 2, name="Juan", surname="Castellanos", url="http://juan.com", age=35),
            User(id=3, name="Cesar", surname="Castellanos", url="http://cesar.com", age=33),
            User(id=4, name="Paul", surname="Scholes", url="http:/paulscholes.com", age=48),
            User(id=5, name="Ryan", surname="Giggs", url="http://rgiggs.com", age=49)]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Manuel", "surname": "Castellanos", "url": "http://manuel.com", "age": 38},
                {"name": "Juan", "surname": "Castellanos", "url": "http://juan.com", "age": 35},
                {"name": "Cesar", "surname": "Castellanos", "url": "http://cesar.com", "age": 33},
                {"name": "Paul", "surname": "Scholes", "url": "http://paulscholes.com", "age": 48},
                {"name": "Ryan", "surname": "Giggs", "url": "http://rgiggs.com", "age": 49}]

@router.get("/users")
async def users():
    return users_list

# Path - Ruta
# @router.get("/user/{id}")
# async def user(id: int):
#     users = filter(lambda user: user.id == id, users_list)
    
#     try: 
#         return list(users)[0]
#     except:
#         return {"Error": "No existe el usuario"}

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


#Query - Consulta
# @router.get("/userquery/")
# async def user(id: int):
#     users = filter(lambda user: user.id == id, users_list)
#     try: 
#         return list(users)[0]
#     except:
#         return {"Error": "No existe el usuario"}

@router.get("/userquery")
async def user(id: int):
    return search_user(id)

@router.post("/user/", response_model = User, status_code = 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = 404, detail = "Este usuario ya existe en el registro")
        #return {"Error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user

@router.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if (saved_user.id == user.id):
            users_list[index] = user
            found = True

    if not found:
        return {"Error": "Usuario no actualizado"}
    else:
        return user

@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if (saved_user.id == id):
            del users_list[index]
            found = True
    
    if not found:
        return {"Erros": "No se ha eliminado ningún usuario"}



def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except:
        return {"Error": "No existe el usuario"}

"""
TIP:
Para la siguiente petición por query,
la consulta debe ser algo como: http://127.0.0.1:8000/userquery/?id=2
si son varios campos por filtrar: http://127.0.0.1:8000/userquery/?id=2&name="Manuel"
"""

