from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.leslie_claire
users = db.users

def authenticate( username, passw ):
    user = users.find_one({'username': username})
    #if username does not exist
    if user  == None:
        return "username does not exist"
    elif user['password'] != passw:
        return "password and username do not match"
        
    return "match"

def add_user( username, passw, email ):
    user = {
        'username' : username,
        'password' : passw,
        'email' : email
    }
    return users.insert(user)


@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("index.html", msg=None)
    else:
        username = request.form["name"]
        password = request.form["password"]
        
        msg = authenticate( username, password )
        
        if (msg == "match"):
            return redirect(url_for('profile'))
        else:
            return render_template("index.html", msg=msg)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile")
def profile():
    return "you logged in"

if __name__=="__main__":
    app.debug = True
    app.run()

