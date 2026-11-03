amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 15
elif amount >= 1000:
    discount = 10
else:
    discount = 0

saved = amount * discount / 100
final_amount = amount - saved

print("Original Amount: ₹", amount)
print("Discount:", discount, "%")
print("You Saved: ₹", saved)
print("Final Amount: ₹", final_amount)