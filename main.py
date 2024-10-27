from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client['gnapika_database']  # Replace with your database name

class Item(BaseModel):
    name: str
    price: float

@app.post("/add-to-cart/")
async def add_to_cart(item: Item):
    cart_collection = db['cart']  # Replace with your cart collection name
    cart_collection.insert_one(item.dict())
    return {"message": "Item added to cart!"}

@app.get("/cart/")
async def get_cart():
    cart_collection = db['cart']  # Replace with your cart collection name
    items = list(cart_collection.find())
    return {"cart": items}
