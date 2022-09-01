from flask import Flask, render_template, redirect, session, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read_users():
    users = User.read_user()
    return render_template("user.html", users = users)

@app.route('/users/add')
def add_users():
    return render_template("newuser.html")

@app.route('/users/create', methods = ['POST'])
def create_users():
    User.create_user(request.form)
    return redirect("/users")

@app.route('/users/delete/<int:id>')
def delete_users(id):
    data = {'id' : id}
    User.delete_user(data)
    return redirect('/users')

@app.route('/users/edit/<int:id>')
def read(id):
    data ={ "id":id }
    return render_template("edit.html",user=User.read_one(data))

@app.route('/users/update', methods = ['POST'])
def update_users():
    User.update_user(request.form)
    return redirect("/users")

@app.route('/users/show/<int:id>')
def show_users(id):
    data ={ "id":id }
    return render_template("profile.html",user=User.read_one(data))

if __name__ == '__main__':
    app.run(debug=True)
