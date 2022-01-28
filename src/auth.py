import string, random
from db_api import db


class User:
    def __init__(self, firstname, lastname, upi_id, user_id, password):
        self.firstname = firstname 
        self.lastname = lastname 
        self.upi_id = upi_id
        self.user_id = user_id
        self.password = password
        

def is_user_already_registered(user):
    print("is-user_already_regisertered with :", user)
    collection =  db.users
    return collection.find_one({"user_id": user.user_id})
        
def add_new_user(user):
    collection = db.users
    return collection.insert_one({"firstname": user.firstname, "lastname": user.lastname, "upi_id": user.upi_id, "user_id": user.user_id, "password": user.password})   

def create_token():
    return "".join(random.choice(string.hexdigits) for _ in range(15))
    