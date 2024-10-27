from fastapi import APIRouter, HTTPException
from database import db
from models.cart import CartItem, Cart
from bson import ObjectId

router = APIRouter()

@router.post("/cart/add")
async def add_to_cart(cart_item: CartItem, user_id: str):
    cart = db.carts.find_one({"user_id": user_id})
    if cart:
        db.carts.update_one(
            {"user_id": user_id},
            {"$push": {"items": cart_item.dict()}}
        )
    else:
        db.carts.insert_one({"user_id": user_id, "items": [cart_item.dict()]})
    return {"message": "Item added to cart"}

@router.get("/cart/{user_id}")
async def get_cart(user_id: str):
    cart = db.carts.find_one({"user_id": user_id})
    if cart:
        return cart
    raise HTTPException(status_code=404, detail="Cart not found")

@router.delete("/cart/remove")
async def remove_from_cart(user_id: str, product_id: str):
    result = db.carts.update_one(
        {"user_id": user_id},
        {"$pull": {"items": {"product_id": product_id}}}
    )
    if result.modified_count:
        return {"message": "Item removed from cart"}
    raise HTTPException(status_code=404, detail="Item not found in cart")
