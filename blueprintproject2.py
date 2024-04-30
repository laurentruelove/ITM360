from werkzeug.security import check_password_hash
from flask import Flask, request, redirect, url_for
import flask_login
import mysql.connector

# Server Development
app = Flask(__name__)

# Database
students = mysql.connector.connect(user='root', host='localhost', password='Oreo1234', database='Login')

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "super secret string"

# Initialize a LoginManager object to prepare for user login authentication
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User(flask_login.UserMixin):
    def __init__(self, email, password):
        self.email = email
        self.password = password


# Route for login page
@login_manager.user_loader
def user_finder(email):
    cursor = students.cursor()
    cursor.execute('SELECT StudentID, EMAIL from ADMIN_DATA where EMAIL = %s', (email,))
    user = cursor.fetchone()
    cursor.close()
    if user is not None:
        return User(user[0], user[1])
    else:
        return None


@app.route("/", methods=["GET"])
def home():
    return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        user = user_finder(email)
        if user is None:
            return 'Unauthorized', 401
        elif not check_password_hash(user.password, request.form.get("password")):
            return 'Invalid passcode', 402

        flask_login.login_user(user)
        return redirect(url_for("index"))
    else:
        return """
        <form method="post">
            <input type="text" name="id" placeholder="Enter your Email"><br>
            <input type="password" name="password" placeholder="Enter your password"><br>
            <button type="submit">Login</button>
        </form>
        """


@app.route("/index")
@flask_login.login_required
def index():
    return f"You are logged in. <br>Showing content that's only viewable by you.<br><a href='/logout'>Logout</a>"


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return "Logged out"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)



