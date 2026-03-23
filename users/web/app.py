from flask import Flask
from users.web.auth import init_auth
from users.web.app.routes import main_bp
from users.web.auth.routes import auth_bp

def create_app():
    """Application factory."""
    app = Flask(__name__)

    # Secret key for session management and CSRF protection
    app.config['SECRET_KEY'] = 'dev-secret-key-change-this-in-production'

    # Initialize Flask-Login
    init_auth(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
