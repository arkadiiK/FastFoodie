from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from models import Base, Restaurant, User, Review
from auth import register, login_user
from security import hash_password, verify_password

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


fake_user_db = {}


@app.post("/register")
async def register_user(user: User):
    if user.username in fake_user_db:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = hash_password(user.password)
    fake_user_db[user.username] = hashed_password
    return {"message": "User created successfully"}


@app.post("/login")
async def login_user(user: User):
    if user.username not in fake_user_db:
        raise HTTPException(status_code=404, detail="Username not found")

    stored_password = fake_user_db[user.username]
    if not verify_password(stored_password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": "User logged in"}
