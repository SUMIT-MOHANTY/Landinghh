from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def __repr__(self):
        return f'<User {self.username}>'

# Mock user database for demonstration
# In production, use a real database
USERS = {
    'admin': {
        'id': 1,
        'username': 'admin',
        'password': 'scrypt:32768:8:1$ZTvWiFrOBbT86uF7$7e22f6d2bf705e25c2bcf70364c879e7c2443923dadda6b2c3ec7d5a23c9ba3b'
    },
    'user1': {
        'id': 2,
        'username': 'user1',
        'password': 'scrypt:32768:8:1$ZTvWiFrOBbT86uF7$7e22f6d2bf705e25c2bcf70364c879e7c2443923dadda6b2c3ec7d5a23c9ba3b'
    }
}
