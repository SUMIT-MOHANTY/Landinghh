from flask_login import LoginManager
from .models import USERS, User

login_manager = LoginManager()

def init_auth(app):
    """Initialize Flask-Login with the app."""
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        """Load user by ID."""
        for user_data in USERS.values():
            if user_data['id'] == int(user_id):
                return User(user_data['id'], user_data['username'])
        return None
