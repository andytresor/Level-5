from flask import render_template, request, redirect# type:ignore
from config import db
from models.users import Utilisateur

def index():
    users = Utilisateur.query.all()
    return render_template('display.html', title="Display Page", users=users)

def add_user():
    return render_template('add_user.html', title="Add User")

def view(id):
    users = Utilisateur.query.get(id)
    return render_template('user_detail.html', title="User Detail Page", users=users)

def newUser():
    form = request.form
    name = form['name']
    email = form['email']
    phone = form['phone']

    user = Utilisateur(name=name, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()

    return redirect('/display')

def delete_user(id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            users = Utilisateur.query.get(id)
            db.session.delete(users)
            db.session.commit()
            return redirect('/display')
    

def update_user(id):
    users = Utilisateur.query.filter_by(id = id).first()
    if users is None:
        return redirect('/display')
    if request.method == "GET":
        return  render_template('user_update.html', title="Update Page", users=users)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        phone = form['phone']
        users.name = name
        users.email = email
        users.phone = phone
        db.session.commit()
        return redirect('/display')
    return render_template('user_update.html', title="Update Page", users=users)
