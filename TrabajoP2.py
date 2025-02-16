from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

# Probar API localmente http://127.0.0.1:8000/docs

app = FastAPI()

class User(BaseModel):
    id: str
    name: str
    email: str

# Almacenar usuarios temporalmente
users = []

# Crear un usuario (POST)
@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return user

# Obtener el primer usuario (GET)
@app.get("/users/", status_code=status.HTTP_200_OK)
def get_first_user():
    if not users:
        raise HTTPException(status_code=404, detail="No ti@, no he visto ese usuario")
    return users[0]