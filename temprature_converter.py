temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    print("Fahrenheit:", (temp * 9 / 5) + 32)
elif unit == "F":
    print("Celsius:", (temp - 32) * 5 / 9)
else:
    print("Invalid unit")