import pytest
from users.web.auth.forms import LoginForm
from users.web.auth.utils import authenticate_user
from users.web.auth.models import User

def test_login_form_validation():
    """Test login form validation."""
    form = LoginForm(username='test', password='password')
    assert form.validate()  # Should pass

    form = LoginForm(username='t', password='pass')
    assert not form.validate()  # Should fail due to length constraints

def test_authenticate_user():
    """Test user authentication."""
    # Test with correct credentials
    user = authenticate_user('admin', 'password')
    assert user is not None
    assert user.username == 'admin'

    # Test with incorrect credentials
    user = authenticate_user('admin', 'wrong')
    assert user is None

    # Test with non-existent user
    user = authenticate_user('nonexistent', 'password')
    assert user is None

def test_user_model():
    """Test User model."""
    user = User(1, 'testuser')
    assert user.id == 1
    assert user.username == 'testuser'
    assert repr(user) == '<User testuser>'
