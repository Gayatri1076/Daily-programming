products = {}

while True:
    name = input("Enter product name (or done): ").strip()

    if name.lower() == "done":
        break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    products[name] = price * quantity

print("\n========== SHOPPING BILL ==========")

total = 0

for name, amount in products.items():
    print(name, ":", "₹", amount)
    total += amount

print("-----------------------------------")
print("Total Amount: ₹", round(total, 2))

if total >= 1000:
    discount = total * 0.10
    print("Discount: ₹", round(discount, 2))
    total -= discount

print("Final Bill: ₹", round(total, 2))
print("Thank you for shopping!")