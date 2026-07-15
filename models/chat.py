from datetime import datetime

from models import db


class Chat(db.Model):

    __tablename__ = "chats"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    user_message = db.Column(
        db.Text,
        nullable=False
    )

    ai_response = db.Column(
        db.Text,
        nullable=False
    )

    emotion = db.Column(
        db.String(50),
        default="Neutral"
    )

    sentiment = db.Column(
        db.String(50),
        default="Neutral"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "chats",
            lazy=True,
            cascade="all, delete-orphan"
        )
    )

    def __repr__(self):
        return f"<Chat {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_message": self.user_message,
            "ai_response": self.ai_response,
            "emotion": self.emotion,
            "sentiment": self.sentiment,
            "created_at": self.created_at.strftime("%d-%m-%Y %H:%M")
        }