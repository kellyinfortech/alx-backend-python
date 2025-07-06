#!/usr/bin/python3
import seed

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()

def compute_average_age():
    """Compute average age using the stream_user_ages generator."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    average = total / count if count else 0
    print(f"Average age of users: {average:.2f}")
