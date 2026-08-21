expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expenses.append({
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses available.")
        else:
            print("\n----- Expenses -----")

            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['category']} - ₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"\nTotal Expense: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")