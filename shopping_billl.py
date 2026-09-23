items = {}

while True:
    name = input("Enter item name (or done): ")

    if name.lower() == "done":
        break

    price = float(input("Enter price: "))
    items[name] = price

total = sum(items.values())

print("\nShopping Bill")

for name, price in items.items():
    print(name, ":", price)

print("Total:", total)