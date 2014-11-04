from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__=="__main__":
    app.debug = True
    app.run()

