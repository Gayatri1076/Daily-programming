email = input("Enter your email: ").strip()

if "@" in email and "." in email.split("@")[-1] and " " not in email:
    print("Email format is valid")
else:
    print("Invalid email format")