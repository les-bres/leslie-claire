from utils import confirmation
from flask import Flask, flash, render_template, request, redirect, url_for, session, escape
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.proj
users = db.users


def add_user(username,password,name,email):
    user = {
        'username' : username,
        'password' : password,
        'email' : email,
        'name' : name
    }
    return users.insert(user)

def authenticate( username, passw ):
    user = users.find_one({'username': username})
    #if username does not exist
    if user  == None:
        return "username does not exist"
    elif user['password'] != passw:
        return "password and username do not match"
        
    return "match"


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

#register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        print "dog"
        return render_template("register.html", msg = None)
       
    else:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        name = request.form["name"]

        msg = confirmation(username, password,email,name)
        print msg
        print "cat"
        if (msg == "good"):
            add_user(username,password,email)
            return render_template("index.html", msg="registration successful, please log in")
        else:
            return render_template("register.html", msg=msg)


@app.route("/profile")
def profile():
    return "you logged in"


if __name__=="__main__":
    app.debug = True
    app.run()

