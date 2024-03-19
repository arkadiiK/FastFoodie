from datetime import timedelta

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from main import app
from .models import User
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base, db
import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/register")
async def register(username: str, email: str, password: str):
    if db.query(User).filter(User.username == username).first is not None:
        raise HTTPException(status_code=400, detail="Username already exists")
    if db.query(User).filter(User.email == email).first is not None:
        raise HTTPException(status_code=400, detail="Email already in use")

    password_hash = hash_password(password)

    new_user = User(username=username, email=email, password_hash=password_hash)
    db.add(new_user)
    db.commit()

    return {"massage": "User created successfully"}


@app.post("/login")
async def login_user(username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if user is None or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
