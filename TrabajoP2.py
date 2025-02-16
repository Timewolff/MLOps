from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

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