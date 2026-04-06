# 🗄️ Database Integration with SQLite (Built-in with Python)

import sqlite3

# 1. Connect to a database (or create it if it doesn't exist)
conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# 2. Create a Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
""")

# 3. Insert Data
# Important: Use ? placeholder to prevent SQL injection!
cursor.execute("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", 
               ("Chayan", 18, "chayan@example.com"))

# 4. Save (Commit) Changes
conn.commit()

# 5. Read Data (SELECT)
cursor.execute("SELECT * FROM Users")
all_users = cursor.fetchall() # Returns list of tuples

print("List of Users:")
for user in all_users:
    print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")

# 6. Update Data
cursor.execute("UPDATE Users SET age = ? WHERE name = ?", (19, "Chayan"))
conn.commit()

# 7. Delete Data
# cursor.execute("DELETE FROM Users WHERE name = ?", ("Chayan",))
# conn.commit()

# Always close the connection when done
# conn.close()

# Summary Table
"""
| Method            | Purpose                                           |
|-------------------|---------------------------------------------------|
| sqlite3.connect() | Create/Open database file                         |
| cursor.execute()  | Run a SQL command                                 |
| conn.commit()     | Permanently save changes to disk                  |
| cursor.fetchone() | Get one row of the results                        |
| cursor.fetchall() | Get all rows of the results                       |
| conn.close()      | Close connection (Free up resources)              |
"""
