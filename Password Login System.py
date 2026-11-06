users = {
    "admin": "admin123",
    "student": "python456",
    "guest": "guest789"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful!")
    print("Welcome,", username)
else:
    print("Invalid Username or Password!")