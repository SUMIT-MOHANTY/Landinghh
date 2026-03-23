from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

def seed_admin():
    with app.app_context():
        # Check if admin already exists
        if User.query.filter_by(username='admin').first():
            print("Admin user already exists")
            return

        # Create admin user
        admin = User(
            username='admin',
            email='admin@example.com',
            is_admin=True
        )
        admin.set_password('adminpassword')  # Change this in production!

        # Add to database
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully")

if __name__ == '__main__':
    seed_admin()
