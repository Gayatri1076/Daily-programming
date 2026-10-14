inventory = {
    "pen": 20,
    "notebook": 15,
    "pencil": 30,
    "eraser": 10
}

item = input("Enter item name: ").lower()

if item in inventory:
    print("Available stock:", inventory[item])

    quantity = int(input("Enter quantity to sell: "))

    if 0 < quantity <= inventory[item]:
        inventory[item] -= quantity
        print("Sale successful!")
        print("Remaining stock:", inventory[item])
    else:
        print("Invalid quantity or insufficient stock.")
else:
    print("Item not found.")