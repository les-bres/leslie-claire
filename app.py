from flask import Flask, render_template, request, redirect
from utils import add_user, emailconfirmation

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

#register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html", message = "")
    else:
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        email = request.form["email"]
        if (emailconfirmation(email) == True):
            add_user(username,password,name,email)
            return redirect(url_for("register"))
        else:
            return render_template("register.html", message = "invalid email, please try again.")


if __name__=="__main__":
    app.debug = True
    app.run()

