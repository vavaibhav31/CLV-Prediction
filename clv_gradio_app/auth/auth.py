
from pymongo import MongoClient
import bcrypt
import os
client = MongoClient(os.getenv("MONGODB_URI")))
db = client['Retail']
users = db['users']

def signup_user(email, password):
    if users.find_one({"email": email}):
        return "User already exists."
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users.insert_one({"email": email, "password": hashed})
    return "User signed up successfully!"

def login_user(email, password):
    user = users.find_one({"email": email})
    if not user:
        return False
    return bcrypt.checkpw(password.encode(), user['password'])
