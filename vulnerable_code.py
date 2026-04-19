# Example of insecure Python code

username = input("Enter username: ")
password = input("Enter password: ")

# Hardcoded credentials (bad practice)
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

# SQL Injection Example (vulnerable)
query = "SELECT * FROM users WHERE username = '" + username + "'"
print("Executing Query:", query)
