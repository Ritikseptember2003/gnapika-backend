from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"  # MongoDB URI
client = MongoClient(MONGO_URI)

# Create a database
db = client['gnapika_database']  # Replace with your database name

# Create collections
users_collection = db['users']  # For authentication
cart_collection = db['cart']      # For storing cart items
