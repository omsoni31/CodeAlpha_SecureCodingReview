# Secure version of the code

import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

# Use parameterized query (safe)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))

print("Secure Query Executed")
