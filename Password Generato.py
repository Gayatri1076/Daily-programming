import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%&*"

length = int(input("Enter password length: "))

characters = letters + digits + symbols

if length < 1:
    print("Enter a valid length.")
else:
    password = "".join(
        random.choice(characters) for _ in range(length)
    )
    print("Generated Password:", password)