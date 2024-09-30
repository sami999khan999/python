from main import connect_to_db

connection = connect_to_db()

cursor = connection.cursor()

cursor.execute(
    """
DELETE FROM users WHERE id = ?
""",
    (1,),
)

connection.commit()
