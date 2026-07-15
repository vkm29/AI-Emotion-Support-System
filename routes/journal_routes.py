"""
journal_routes.py
"""

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from services.journal_engine import JournalEngine

journal = Blueprint(
    "journal",
    __name__
)

engine = JournalEngine()


@journal.route("/journal")

@login_required
def journal_page():

    prompt = engine.get_prompt(
        "neutral"
    )

    return render_template(
        "journal.html",
        prompt=prompt
    )


@journal.route(
    "/save_journal",
    methods=["POST"]
)

@login_required
def save_journal():

    emotion = request.form.get("emotion")

    text = request.form.get("journal")

    result = engine.analyze(
        text,
        emotion
    )

    flash(
        "Journal Saved Successfully",
        "success"
    )

    return render_template(

        "journal.html",

        result=result,

        prompt=engine.get_prompt(emotion)

    )   