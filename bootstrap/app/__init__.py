import os
from flask import Flask
from config.settings import Config

def create_app():
    """Application factory pattern"""
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(Config)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
