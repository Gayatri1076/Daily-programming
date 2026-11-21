trains = {
    "Express": 50,
    "Passenger": 80,
    "Superfast": 30
}

print("Available Trains:")

for train, seats in trains.items():
    print(train, "- Available Seats:", seats)

name = input("\nEnter passenger name: ")
choice = input("Choose train: ").title()
tickets = int(input("Enter number of tickets: "))

if choice in trains:
    if 0 < tickets <= trains[choice]:
        trains[choice] -= tickets

        print("\nTicket Booking Successful!")
        print("Passenger:", name)
        print("Train:", choice)
        print("Tickets:", tickets)
        print("Remaining Seats:", trains[choice])
    else:
        print("Not enough seats available!")
else:
    print("Invalid train selection!")