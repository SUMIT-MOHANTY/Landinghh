"""
Landing-flask: minimal, production-ready scaffold.
Serves only / and /health per API CONTRACT.
"""

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# App factory pattern for clean startup
app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-not-for-prod')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bootstrap extensions
db = SQLAlchemy(app)

# Delayed import to prevent circular refs
from models.user import User

# Register blueprints could go here, but contract says only / and /health
@app.route('/')
def landing_root():
    """Root greeting endpoint."""
    return jsonify(message="Landing page works")

@app.route('/health')
def health():
    """Service health check."""
    return jsonify(status="ok")

@app.errorhandler(404)
def not_found(_):
    """Minimal 404 compliant with spec."""
    return jsonify(error="Not Found"), 404

# CLI hook to create tables on first run
@app.cli.command('init-db')
def init_db():
    """Initialize SQLite tables."""
    db.create_all()
    print("[] Database initialized.")

if __name__ == '__main__':
    # Quick test harness for dev; production uses gunicorn
    app.run()
