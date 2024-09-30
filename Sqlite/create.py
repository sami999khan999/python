from main import connect_to_db
from create_table import create_table

connection = connect_to_db()

create_table(connection)

cursor = connection.cursor()
cursor.execute(
    """
INSERT INTO users (name, age) VALUES (?, ?)
""",
    ("Sami", 22),
)

connection.commit()

connection.close()
