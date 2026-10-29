tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter task: ")
        priority = input("Priority (High/Medium/Low): ").title()
        tasks.append({"task": name, "priority": priority})
        print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(i, task["task"], "-", task["priority"])

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(i, task["task"])

        try:
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task removed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Enter a valid number!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")