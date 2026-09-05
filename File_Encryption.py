import base64

text = input("Enter text: ")

encoded = base64.b64encode(text.encode()).decode()

print("Encrypted text:", encoded)

decoded = base64.b64decode(encoded).decode()

print("Decrypted text:", decoded)