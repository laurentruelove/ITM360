# Main script
from flask import Flask
from flask_login import LoginManager, UserMixin
import mysql.connector

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Connect to MySQL Database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Oreo1234",
        database="Library"
    )

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Define User class with UserMixin
    class User(UserMixin):
        def __init__(self, mno):
            self.mno = mno

    # Set up Flask-Login to load user from session
    @login_manager.user_loader
    def load_user(mno):
        return User(mno)

    from .blueprint import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)