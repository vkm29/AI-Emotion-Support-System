"""
dashboard_routes.py

AI Student Emotional Support System
Dashboard Routes
"""

from flask import Blueprint
from flask import render_template

from flask_login import login_required
from flask_login import current_user

from models.chat import Chat
from services.analytics_engine import AnalyticsEngine

dashboard = Blueprint("dashboard", __name__)

analytics = AnalyticsEngine()


# ------------------------------------
# Dashboard
# ------------------------------------

@dashboard.route("/dashboard")

@login_required
def student_dashboard():

    chats = Chat.query.filter_by(
        user_id=current_user.id
    ).all()

    emotions = []

    for chat in chats:
        emotions.append(chat.emotion)

    report = analytics.generate_report(
        emotions
    )

    return render_template(

        "dashboard.html",

        user=current_user,

        chats=len(chats),

        report=report

    )
    
# ------------------------------------
# Analytics Page
# ------------------------------------

@dashboard.route("/analytics")
@login_required
def analytics_page():

    chats = Chat.query.filter_by(
        user_id=current_user.id
    ).all()

    emotions = [chat.emotion for chat in chats]

    report = analytics.generate_report(emotions)

    return render_template(
        "analytics.html",
        report=report,
        chats=chats
    )