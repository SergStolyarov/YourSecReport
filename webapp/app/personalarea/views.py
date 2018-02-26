from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from .models import User
from .forms import LoginForm, SignUpForm
from flask_login import login_user, logout_user, login_required, current_user

personalarea = Blueprint('personalarea', __name__)

@personalarea.route("/", methods=['GET'])
def main():
    #return "Hello"
    return render_template("index.html")


@personalarea.route("/personal", methods=['POST', 'GET'])
def personal():

    form = AddServiceForm()
    services = user_data[current_user._name].setdefault('services', [])
    if form.validate_on_submit():
        new_service_ip = form.ip.data
        user_data[current_user._name]['services'].append(new_service_ip)
        store_database()
        return redirect(url_for('personal'))

    return render_template("personal.html", form=form, services=services)

@personalarea.route("/signup", methods=['POST', 'GET'])
def sign_up():

    form = SignUpForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            users = mongo
            name = form.name.data
            email = form.email.data
            password = form.password.data

            user_email[name] = email
            user_credentials[name] = password
            user_data[name] = {}
        store_database()

        return redirect(url_for('login', name=request.form.get("name"),
            password=request.form.get("password")), code=307)
    else:
        return render_template("signup.html", form=form)

@personalarea.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect("/personal")
    form = LoginForm()
    if form.validate_on_submit(): 
        login_user(User(form.name.data))
        return redirect("/")
    else:

        return render_template("login.html", form=form)

@personalarea.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")