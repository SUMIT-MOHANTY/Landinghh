import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User

def init_cli(app):
    @app.cli.command("seed-admin")
    @click.argument("username")
    @click.argument("email")
    @click.argument("password")
    @with_appcontext
    def seed_admin(username, email, password):
        """Seed the database with an admin user."""
        user = User.query.filter_by(username=username).first()
        if user is not None:
            click.echo(f"User {username} already exists.")
            return

        user = User(
            username=username,
            email=email,
            is_admin=True
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        click.echo(f"Created admin user: {username}")
