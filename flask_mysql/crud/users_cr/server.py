from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def view_users():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route('/users/new')
def new_user():
    return render_template("index1.html")

@app.route('/users/add', methods = ["POST"])
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)