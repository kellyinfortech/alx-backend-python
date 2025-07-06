import mysql.connector
from mysql.connector import Error

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # replace with your MySQL root password
            database='ALX_prodev'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches from the user_data table."""
    connection = connect_to_prodev()
    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute(
            "SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset)
        )
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Process each batch and yield users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
