from werkzeug.security import check_password_hash
from .models import USERS

def authenticate_user(username, password):
    """Authenticate user with username and password."""
    user_data = USERS.get(username)
    if user_data and check_password_hash(user_data['password'], password):
        from .models import User
        return User(user_data['id'], user_data['username'])
    return None
