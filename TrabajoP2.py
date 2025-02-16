from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

# Obtener el primer usuario (GET)
@app.get("/users/", status_code=status.HTTP_200_OK)
def get_first_user():
    if not users:
        raise HTTPException(status_code=404, detail="No ti@, no he visto ese usuario")
    return users[0]