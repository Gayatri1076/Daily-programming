items = {}

while True:
    print("\n1. Report Lost Item")
    print("2. Search Item")
    print("3. View All Items")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter item name: ").lower()
        location = input("Enter lost location: ")

        items[name] = location
        print("Item reported successfully!")

    elif choice == "2":
        name = input("Search item: ").lower()

        if name in items:
            print("Item found!")
            print("Last seen at:", items[name])
        else:
            print("Item not found!")

    elif choice == "3":
        for name, location in items.items():
            print(name, ":", location)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")