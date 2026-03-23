from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.settings')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Import models to register them
    from app.models import user
    from app import routes

    return app
