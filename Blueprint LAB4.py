from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

auth_blueprint = Blueprint('auth', __name__)

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Oreo1234",
    database="Library"
)

# Route for member sign up
@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mno = request.form['mno']
        mname = request.form['mname']
        password = request.form['password']

        # Hash the password
        hashed_password = generate_password_hash(password)

        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO Member (mno, mname, password) VALUES (%s, %s, %s)", (mno, mname, hashed_password))
            db.commit()
            cursor.close()
            return redirect(url_for('auth.login'))
        except mysql.connector.Error as err:
            error_message = "Error: {}".format(err)
            return render_template('error.html', error_message=error_message)

    return render_template('signup.html')

# Route for member authentication
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mno = request.form['mno']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM Member WHERE mno = %s", (mno,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            login_user(User(user[0])) # to load the User class for authentication purpose, need to import user_loader from Database module or the main module because both have defined the class; -3 pts
            return redirect(url_for('auth.protected'))

        return redirect(url_for('auth.invalid'))

    return render_template('login.html')

# Protected route for authenticated users
@auth_blueprint.route('/protected')
@login_required
def protected():
    mno = current_user.mno

    cursor = db.cursor()
    cursor.execute("SELECT Bname FROM Bookrecord WHERE Bno IN (SELECT Bno FROM Issue WHERE Mno = %s)", (mno,))
    books = cursor.fetchall()

    return render_template('protected.html', books=books)

# Route for invalid login
@auth_blueprint.route('/invalid')
def invalid():
    return render_template('invalid.html')

# Route for logout
@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
