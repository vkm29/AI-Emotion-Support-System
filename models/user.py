from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from models import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # -------------------
    # Password Hash
    # -------------------

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # -------------------
    # Verify Password
    # -------------------

    def check_password(self, password):
        return check_password_hash(
            self.password,
            password
        )

    # -------------------
    # String Representation
    # -------------------

    def __repr__(self):
        return f"<User {self.email}>"