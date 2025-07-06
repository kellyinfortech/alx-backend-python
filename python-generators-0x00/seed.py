#!/usr/bin/python3
import mysql.connector
import csv
import uuid

DB_NAME = "ALX_prodev"

def connect_db():
    """Connects to the MySQL server (not a specific database)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Update this if you have a password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Creates the ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    except mysql.connector.Error as err:
        print(f"Database creation failed: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connects directly to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Update if needed
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Creates the user_data table if it doesn't exist."""
    query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    )
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Table creation failed: {err}")
    finally:
        cursor.close()

def insert_data(connection, csv_file):
    """Reads data from CSV and inserts it into user_data table."""
    cursor = connection.cursor()
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']

                # Check if record already exists to avoid duplicates
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                exists = cursor.fetchone()
                if not exists:
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )
        connection.commit()
        print("Data inserted successfully")
    except Exception as e:
        print(f"Failed to insert data: {e}")
    finally:
        cursor.close()
