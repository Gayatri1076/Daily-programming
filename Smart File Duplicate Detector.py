import os
import hashlib

folder = input("Enter folder path: ")

files = {}

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    if os.path.isfile(path):
        with open(path, "rb") as file:
            file_hash = hashlib.md5(file.read()).hexdigest()

        if file_hash in files:
            print("Duplicate:", filename)
            print("Original:", files[file_hash])
        else:
            files[file_hash] = filename

print("Scan Completed!")