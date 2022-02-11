from flask import render_template, request, redirect, session 
# link the app routes
from users_app import app
# import the burger class
from users_app.models.user import User 

@app.route("/")
def create():
    # users = User.get_all()
    # call the get all classmethod to get all friends
    return render_template('create.html')

@app.route('/add_user', methods = ['POST'])
def create_user():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.create_user(data)
    return redirect('/users')

@app.route('/users')
def displayall():
    users = User.get_all()
    return render_template('read.html', users = users)