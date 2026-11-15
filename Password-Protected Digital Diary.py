from datetime import datetime

password = "diary123"

entered = input("Enter diary password: ")

if entered == password:
    print("\n1. Write Diary")
    print("2. Read Diary")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Write your thoughts: ")
        date = datetime.now().strftime("%d-%m-%Y %H:%M")

        with open("diary.txt", "a") as file:
            file.write(date + "\n" + note + "\n\n")

        print("Diary saved successfully!")

    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                print("\nYour Diary:\n")
                print(file.read())
        except FileNotFoundError:
            print("No diary entries found!")

    else:
        print("Invalid choice!")

else:
    print("Wrong password!")