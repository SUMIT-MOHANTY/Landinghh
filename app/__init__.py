from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.settings')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to register them
    from app.models import user

    return app
