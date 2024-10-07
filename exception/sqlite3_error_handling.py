import sqlite3

# ---------------------------
# SQLite3 Exception Handling
# ---------------------------
# The sqlite3 module in Python raises several exceptions specific to SQLite database operations.
# Understanding these exceptions helps in writing robust error handling for database interactions.

# The sqlite3 module raises several exceptions that are specific to SQLite database operations.
# Common exceptions include:

# - sqlite3.DatabaseError: Raised for errors that are related to the database.

# - sqlite3.OperationalError: Raised for operational errors like a database file not found or locked.

# - sqlite3.IntegrityError: Raised when an integrity constraint (like a UNIQUE constraint) fails.

# - sqlite3.ProgrammingError: Raised when an operation is not allowed, such as using a method on a closed connection.

# - sqlite3.DataError: Raised when a problem occurs with the data provided to the database.

# ---------------------------
# sqlite3.DatabaseError
# ---------------------------
# This is the base class for all SQLite database-related errors.
# It can be raised for a variety of database-related issues.

# Example Use Case:
# Attempting to execute a SQL command on a non-existent database may raise this error.

# Example:
try:
    connection = sqlite3.connect(
        "non_existent.db"
    )  # Trying to connect to a non-existent database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM some_table")  # This might raise a DatabaseError
except sqlite3.DatabaseError as e:
    print("Database Error:", e)  # Catch all database-related errors

# ---------------------------
# sqlite3.OperationalError
# ---------------------------
# This error is raised for operational problems that occur during database operations, such as:
# - Database file not found
# - Database locked
# - Disk full
#
# Example Use Case:
# If an attempt is made to connect to a database that is currently locked, an OperationalError will be raised.

# Example:
try:
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM some_locked_table"
    )  # This could raise an OperationalError
except sqlite3.OperationalError as e:
    print("Operational Error:", e)  # Output operational errors

# ---------------------------
# IntegrityError
# ---------------------------
# This error occurs when an integrity constraint (like UNIQUE or NOT NULL) is violated.
#
# Example Use Case:
# Inserting a row with a duplicate primary key or violating a foreign key constraint will raise this error.

# Example:
try:
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'Alice')")
    cursor.execute(
        "INSERT INTO users (id, name) VALUES (1, 'Bob')"
    )  # This will raise an IntegrityError
except sqlite3.IntegrityError as e:
    print("Integrity Error:", e)  # Output integrity constraint violations

# ---------------------------
# sqlite3.ProgrammingError
# ---------------------------
# This error occurs when a programming error is detected, such as:
# - Using invalid SQL syntax
# - Calling methods on closed connections or cursors
#
# Example Use Case:
# Attempting to execute a SQL statement on a cursor that has been closed will raise this error.

# Example:
try:
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.close()  # Close the cursor
    cursor.execute("SELECT * FROM users")  # This will raise a ProgrammingError
except sqlite3.ProgrammingError as e:
    print("Programming Error:", e)  # Output programming errors

# ---------------------------
# sqlite3.DataError
# ---------------------------
# This error occurs when there is a problem with the data provided to the database, such as:
# - Invalid data types
# - Data that cannot be processed (e.g., trying to insert a string into an integer column)
#
# Example Use Case:
# Attempting to insert a string value into an integer column will raise this error.

# Example:
try:
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, price REAL)")
    cursor.execute(
        "INSERT INTO products (id, price) VALUES (1, 'not_a_number')"
    )  # This will raise a DataError
except sqlite3.DataError as e:
    print("Data Error:", e)  # Output data processing errors

# ---------------------------
# sqlite3.InterfaceError
# ---------------------------
# This error occurs when there is an interface-related issue, such as:
# - Trying to use a cursor that is not properly connected to a database.
#
# Example Use Case:
# Using a cursor that was created from a closed connection will raise this error.

# Example:
try:
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    connection.close()  # Close the connection
    cursor.execute("SELECT * FROM users")  # This will raise an InterfaceError
except sqlite3.InterfaceError as e:
    print("Interface Error:", e)  # Output interface-related errors

# ---------------------------
# sqlite3.OperationalError
# ---------------------------
# Similar to above, but can also refer to errors related to the database’s operational state,
# such as unexpected database corruption.
#
# Example Use Case:
# Attempting to perform operations on a corrupted database can raise this error.

# Example:
try:
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    # Simulate a corrupted database operation
    cursor.execute("INVALID SQL COMMAND")  # This will raise an OperationalError
except sqlite3.OperationalError as e:
    print("Operational Error:", e)  # Output operational errors
