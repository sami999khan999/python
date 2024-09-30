from main import connect_to_db

connection = connect_to_db()

cursor = connection.cursor()


cursor.execute(
    """
    SELECT * FROM users WHERE name = ?
""",
    ("Sami",),
)

user = cursor.fetchall()

print(user)
