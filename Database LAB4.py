#Lab 4, base

import mysql.connector
import flask_login
from werkzeug.security import generate_password_hash

# Establish database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Oreo1234',
    database='Library'
)

# Initialize Flask-Login
login_manager = flask_login.LoginManager()

# Define User class for Flask-Login
class User(flask_login.UserMixin):
    def __init__(self, mno):
        self.id = mno

# Cursor for database operations
cursor = db.cursor()

# Create Member table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Member (
                mno INTEGER PRIMARY KEY,
                mname VARCHAR(20),
                date_of_membership DATE,
                addr VARCHAR(24),
                mob VARCHAR(10),
                password_hash VARCHAR(128)  -- Add column for hashed password
            )''')

# Create Issue table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Issue (
                bno INTEGER,
                mno INTEGER,
                d_o_issue DATE,
                d_o_ret DATE,
                FOREIGN KEY (mno) REFERENCES Member(mno)  -- Add foreign key constraint
            )''')

# Create Bookrecord table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Bookrecord (
                bno INTEGER PRIMARY KEY,
                bname VARCHAR(20),
                auth VARCHAR(20),
                price INTEGER,
                publ VARCHAR(20),
                Qty INTEGER,
                Date_of_purchase DATE
            )''')

# Commit database changes
db.commit()

# Function to load user from database
@login_manager.user_loader
def load_user(user_id):
    cursor.execute('SELECT * FROM Member WHERE mno = %s', (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        return User(user_data[0])  # Return User object with member number as ID
    return None

# Close cursor and database connection
cursor.close()
db.close()
