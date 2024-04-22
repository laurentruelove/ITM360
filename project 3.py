import mysql.connector

# Connect to MySQL Database and create the 'Library' database if it doesn't exist
DataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Oreo1234"
)

# Create a cursor object to interact with the database
cursor = DataBase.cursor()

# Create the 'Library' database, comment out the execute
cursor.execute("CREATE DATABASE IF NOT EXISTS Library")

# Close the cursor
cursor.close()

# Close the connection to the MySQL server
DataBase.close()

# Reconnect to MySQL Database with the 'Library' database
DataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Oreo1234",
    database="Library"
)

# Create a cursor object to interact with the database
cur = DataBase.cursor()

# Create Member table
cur.execute('''CREATE TABLE IF NOT EXISTS Member (
                mno INTEGER PRIMARY KEY,
                mname VARCHAR(20),
                date_of_membership DATE,
                addr VARCHAR(24),
                mob VARCHAR(10)
            )''')

# Create Bookrecord table
cur.execute('''CREATE TABLE IF NOT EXISTS Bookrecord (
                bno INTEGER PRIMARY KEY,
                bname VARCHAR(20),
                auth VARCHAR(20),
                price INTEGER,
                publ VARCHAR(20),
                Qty INTEGER,
                Date_of_purchase DATE
            )''')

# Create Issue table
cur.execute('''CREATE TABLE IF NOT EXISTS Issue (
                bno INTEGER,
                mno INTEGER,
                d_o_issue DATE,
                d_o_ret DATE
            )''')

# Commit changes and close connection
#DataBase.commit() 
cur.close()
DataBase.close()

# - 4pts *3, the attributes that are checked/updated in addBook(), searchBook() and updateBook() are not the same as the attributes created in 
# the respective tables. The queries won't be passed along.
def addBook():
    try:
        # Connect to MySQL Database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Oreo1234",
            database="Library"
        )
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Prompt user for book information
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        publication_year = input("Enter publication year: ")

        # Insert book information into Bookrecord table
        cursor.execute('''INSERT INTO Bookrecord (title, author, genre, publication_year) 
                          VALUES (%s, %s, %s, %s)''', (title, author, genre, publication_year))

        # Commit changes and close cursor
        connection.commit()
        cursor.close()

        print("Book added successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()

def deleteBook():
    try:
        # Connect to MySQL Database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Oreo1234",
            database="Library"
        )
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Prompt user for book number to delete
        book_no = input("Enter the book number to delete: ")

        # Check if the book number exists in the Bookrecord table
        cursor.execute("SELECT * FROM Bookrecord WHERE bno = %s", (book_no,))
        book = cursor.fetchone()

        if not book:
            raise ValueError("Book number does not exist.")

        # Delete the book from Bookrecord table
        cursor.execute("DELETE FROM Bookrecord WHERE bno = %s", (book_no,))

        # Commit changes and close cursor
        connection.commit()
        cursor.close()

        print("Book deleted successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    except ValueError as ve:
        print("Error:", ve)

    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()

def searchBook():
    try:
        # Connect to MySQL Database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Oreo1234",
            database="Library"
        )
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Prompt user for book number to search
        book_no = input("Enter the book number to search: ")

        # Check if the book number exists in the Bookrecord table
        cursor.execute("SELECT * FROM Bookrecord WHERE bno = %s", (book_no,))
        book = cursor.fetchone()

        if not book:
            raise ValueError("Book number does not exist.")

        # Output book information
        print("Book information:")
        print("Book Number:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Genre:", book[3])
        print("Publication Year:", book[4])

    except mysql.connector.Error as err:
        print("Error:", err)

    except ValueError as ve:
        print("Error:", ve)

    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()

def updateBook():
    try:
        # Connect to MySQL Database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Oreo1234",
            database="Library"
        )
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Prompt user for book number to update
        book_no = input("Enter the book number to update: ")

        # Check if the book number exists in the Bookrecord table
        cursor.execute("SELECT * FROM Bookrecord WHERE bno = %s", (book_no,))
        book = cursor.fetchone()

        if not book:
            raise ValueError("Book number does not exist.")

        # Prompt user for updated book information
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        genre = input("Enter new genre: ")
        publication_year = input("Enter new publication year: ")

        # Update book information in Bookrecord table
        cursor.execute('''UPDATE Bookrecord 
                          SET title = %s, author = %s, genre = %s, publication_year = %s 
                          WHERE bno = %s''', (title, author, genre, publication_year, book_no))

        # Commit changes and close cursor
        connection.commit()
        cursor.close()

        print("Book updated successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    except ValueError as ve:
        print("Error:", ve)

    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()


# Call functions
addBook()
deleteBook()
searchBook()
updateBook()
