from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from database import db
from models.user import User
from bson import ObjectId

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
async def register(user: User):
    # Hash the password
    hashed_password = pwd_context.hash(user.password)
    # Save user to MongoDB
    result = db.users.insert_one({"username": user.username, "password": hashed_password})
    if result.inserted_id:
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=400, detail="User registration failed")

@router.post("/login")
async def login(user: User):
    db_user = db.users.find_one({"username": user.username})
    if db_user and pwd_context.verify(user.password, db_user["password"]):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
