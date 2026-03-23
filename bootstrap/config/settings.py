import os

class Config:
    """Configuration settings for Flask app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    PORT = int(os.environ.get('PORT', 8000))

    # Additional common settings
    JSONIFY_PRETTYPRINT_REGULAR = True
    TEMPLATES_AUTO_RELOAD = DEBUG
