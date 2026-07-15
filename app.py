from flask import Flask, render_template
from flask_login import LoginManager
from config import Config
from models import db
from models.user import User
from models.chat import Chat
from routes.chat_routes import chat
# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)
app.config.from_object(Config)

# -----------------------------
# Initialize Database
# -----------------------------
db.init_app(app)

# -----------------------------
# Login Manager
# -----------------------------
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Please login first."
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -----------------------------
# Register Blueprints
# -----------------------------
from routes.auth_routes import auth
from routes.dashboard_routes import dashboard
from routes.journal_routes import journal
from routes.admin_routes import admin


app.register_blueprint(auth)

app.register_blueprint(chat)



app.register_blueprint(dashboard)


app.register_blueprint(journal)


app.register_blueprint(admin)
# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Create Database
# -----------------------------
with app.app_context():
    db.create_all()


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)