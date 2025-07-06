import mysql.connector

def stream_users():
    """
    Generator function that yields rows from the user_data table one by one
    as dictionaries.
    """
    try:
        # Connect to ALX_prodev database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',        # change this if using a different user
            password='',        # add your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)  # fetch as dicts

        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
