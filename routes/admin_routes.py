"""
admin_routes.py
"""

from flask import Blueprint
from flask import render_template

from flask_login import login_required

from models.user import User
from models.chat import Chat

admin = Blueprint(
    "admin",
    __name__
)


@admin.route("/admin")

@login_required
def admin_dashboard():

    total_users = User.query.count()

    total_chats = Chat.query.count()

    latest_chats = Chat.query.order_by(
        Chat.created_at.desc()
    ).limit(10)

    return render_template(

        "admin.html",

        users=total_users,

        chats=total_chats,

        latest=latest_chats

    )