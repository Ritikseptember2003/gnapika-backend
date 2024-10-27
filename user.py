from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
