from flask import Flask, request
import auth
from auth import User

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def login():
    user_id = request.form['user_id']
    password = request.form['password']

    return auth.is_valid_user(username, password)
        # return {"status": "Success", "message": "User Successfully Logged In", "token": create_token()}

    # return {"status": "Success", "message": "Login Failed", "token": ""}

    
@app.route("/register",methods=["POST"])    
def regiseter():
    print("regiseter method called")
    form = request.form  
    user = User(form['firstname'], form['lastname'], form['upi_id'], form['user_id'],form['password'])

    print("fistname:", user.firstname)

    # chech if the user is already registered
    if auth.is_user_already_registered(user) :
        return {"status": "Success", "message": "User Already Exists", "token": ""}

    # create new entery in the table
    if auth.add_new_user(user):
        return {"status": "Success", "message": "User Successfully Registered", "token": auth.create_token()}
    