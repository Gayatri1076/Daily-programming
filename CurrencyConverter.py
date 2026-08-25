rates = {
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0,
    "JPY": 0.58
}

print("===== CURRENCY CONVERTER =====")
print("1. USD to INR")
print("2. EUR to INR")
print("3. GBP to INR")
print("4. JPY to INR")

choice = int(input("Enter choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    result = amount * rates["USD"]
    print(f"USD {amount} = INR {result:.2f}")

elif choice == 2:
    result = amount * rates["EUR"]
    print(f"EUR {amount} = INR {result:.2f}")

elif choice == 3:
    result = amount * rates["GBP"]
    print(f"GBP {amount} = INR {result:.2f}")

elif choice == 4:
    result = amount * rates["JPY"]
    print(f"JPY {amount} = INR {result:.2f}")

else:
    print("Invalid choice!")