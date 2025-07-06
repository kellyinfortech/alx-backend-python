# Task 0: Getting Started with Python Generators

## Objective

Create a Python script (`seed.py`) that:

- Sets up a MySQL database called `ALX_prodev`
- Creates a `user_data` table with the following schema:
  - `user_id` (Primary Key, UUID, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Populates the table using data from a CSV file (`user_data.csv`)

---

## Files

- `seed.py` – Handles database connection, creation, table setup, and data population
- `user_data.csv` – Sample user data to be inserted into the database
- `0-main.py` – Provided for testing and validation

---

## Function Prototypes

- `connect_db()`  
  Connects to the MySQL server (no database specified yet).

- `create_database(connection)`  
  Creates the `ALX_prodev` database if it doesn't already exist.

- `connect_to_prodev()`  
  Connects specifically to the `ALX_prodev` database.

- `create_table(connection)`  
  Creates the `user_data` table with appropriate schema.

- `insert_data(connection, data)`  
  Populates the `user_data` table from a CSV file.

---

## Sample Output

```bash
$ ./0-main.py
connection successful
Table user_data created successfully
Database ALX_prodev is present 
[('...', '...', '...', ...), ...]
