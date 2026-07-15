"""
chat_routes.py

AI Student Emotional Support System
"""

from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

from flask_login import login_required
from flask_login import current_user

from services.chatbot_engine import ChatbotEngine
from services.emotion_engine import EmotionEngine
from services.safety_engine import SafetyEngine
from services.recommendation_engine import RecommendationEngine
from services.motivation_engine import MotivationEngine
from services.breathing_engine import BreathingEngine

from models import db
from models.chat import Chat


chat = Blueprint("chat", __name__)

chatbot = ChatbotEngine()
emotion_engine = EmotionEngine()
safety_engine = SafetyEngine()
recommendation_engine = RecommendationEngine()
motivation_engine = MotivationEngine()
breathing_engine = BreathingEngine()


# -----------------------------------------
# Chat Page
# -----------------------------------------

@chat.route("/chat")
@login_required
def chat_page():

    return render_template(
        "chat.html",
        user=current_user
    )


# -----------------------------------------
# Send Message
# -----------------------------------------

@chat.route("/send_message", methods=["POST"])
@login_required
def send_message():

    data = request.get_json()

    message = data.get("message")

    if not message:

        return jsonify({

            "success": False,

            "message": "Empty message."

        })

    # ---------------------------------

    emotion = emotion_engine.predict(message)

    safety = safety_engine.detect(message)

    recommendation = recommendation_engine.get_recommendations(

        emotion["emotion"],

        safety["risk"]

    )

    quote = motivation_engine.get_quote(

        emotion["emotion"]

    )

    breathing = breathing_engine.get_exercise(

        emotion["emotion"]

    )

    chatbot_reply = chatbot.get_response(message)

    final_response = f"""

{chatbot_reply}

-----------------------------------

Detected Emotion

{emotion['emotion'].title()}

Confidence

{emotion['confidence']}

-----------------------------------

Risk Level

{safety['risk']}

-----------------------------------

Recommendation

{recommendation['title']}

{recommendation['description']}

-----------------------------------

Motivation

{quote}

-----------------------------------

Breathing Exercise

{breathing['exercise']}

Duration : {breathing['duration']}

Instructions

{breathing['instructions']}

"""

    chat = Chat(

        user_id=current_user.id,

        user_message=message,

        ai_response=final_response,

        emotion=emotion["emotion"],

        sentiment="Neutral"

    )

    db.session.add(chat)

    db.session.commit()

    return jsonify({

        "success": True,

        "response": final_response,

        "emotion": emotion["emotion"],

        "risk": safety["risk"]

    })


# -----------------------------------------
# Chat History
# -----------------------------------------

@chat.route("/history")
@login_required
def history():

    chats = Chat.query.filter_by(

        user_id=current_user.id

    ).order_by(

        Chat.created_at.desc()

    ).all()

    return render_template(

        "history.html",

        chats=chats

    )