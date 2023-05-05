from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el servidor con: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Manuel", surname="Castellanos", url="http://manuel.com", age=38),
            User(name="Juan", surname="Castellanos", url="http://juan.com", age=35),
            User(name="Cesar", surname="Castellanos", url="http://cesar.com", age=33),
            User(name="Paul", surname="Scholes", url="http:/paulscholes.com", age=48),
            User(name="Ryan", surname="Giggs", url="http://rgiggs.com", age=49)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Manuel", "surname": "Castellanos", "url": "http://manuel.com", "age": 38},
                {"name": "Juan", "surname": "Castellanos", "url": "http://juan.com", "age": 35},
                {"name": "Cesar", "surname": "Castellanos", "url": "http://cesar.com", "age": 33},
                {"name": "Paul", "surname": "Scholes", "url": "http://paulscholes.com", "age": 48},
                {"name": "Ryan", "surname": "Giggs", "url": "http://rgiggs.com", "age": 49}]

@app.get("/users")
async def users():
    return users_list
