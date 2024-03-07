from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="APIs tarea",
    version="0.0.1"
)

# Diccionarios para simular la base de datos
users = {}
tasks = {}

@app.post("/register/", status_code=status.HTTP_201_CREATED)
async def register_user(username: str, email: str, password: str):
    user_id = str(uuid.uuid4())
    users[user_id] = {"username": username, "email": email, "password": password}
    return {"message": "User registered successfully", "user_id": user_id}

@app.get("/user/{user_id}/")
async def get_user(user_id: str):
    user = users.get(user_id)
    if user:
        return JSONResponse(content=user, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"message": "User not found"}, status_code=status.HTTP_404_NOT_FOUND)