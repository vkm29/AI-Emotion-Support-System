from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from models import db
from models.user import User

auth = Blueprint("auth", __name__)


# -----------------------------------
# Register
# -----------------------------------

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("auth.register"))

        existing = User.query.filter_by(email=email).first()

        if existing:
            flash("Email already exists.", "warning")
            return redirect(url_for("auth.register"))

        user = User(
            name=name,
            email=email
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful. Please Login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


# -----------------------------------
# Login
# -----------------------------------

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            login_user(user)

            flash("Login Successful", "success")

            return redirect(url_for("auth.dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


# -----------------------------------
# Dashboard
# -----------------------------------

@auth.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        user=current_user
    )


# -----------------------------------
# Logout
# -----------------------------------

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged Out Successfully.", "success")

    return redirect(url_for("home"))