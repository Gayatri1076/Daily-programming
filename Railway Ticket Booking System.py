trains = {
    "Pune Express": 120,
    "Mumbai Express": 150,
    "Delhi Express": 450,
    "Chennai Express": 600
}

print("AVAILABLE TRAINS")

for train, fare in trains.items():
    print(train, "- ₹", fare)

choice = input("\nEnter train name: ").title()

if choice in trains:
    passengers = int(input("Number of passengers: "))

    if passengers > 0:
        total = trains[choice] * passengers

        print("\nTICKET CONFIRMED!")
        print("Train:", choice)
        print("Passengers:", passengers)
        print("Total Fare: ₹", total)
    else:
        print("Invalid passenger count!")
else:
    print("Train not found!")