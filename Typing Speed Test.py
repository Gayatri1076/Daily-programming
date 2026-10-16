password = "python123"

entered = input("Enter password: ")

if entered == password:
    note = input("Write your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")

    with open("notes.txt", "r") as file:
        print("\nYour Notes:")
        print(file.read())
else:
    print("Incorrect password!")