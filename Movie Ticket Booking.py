seats = 10
price = 150

print("Welcome to Movie Ticket Booking!")

print("Available seats:", seats)

tickets = int(input("Enter number of tickets: "))

if 1 <= tickets <= seats:
    total = tickets * price
    seats -= tickets

    print("\nBooking Successful!")
    print("Tickets:", tickets)
    print("Total Amount: ₹", total)
    print("Remaining Seats:", seats)

else:
    print("Sorry! Seats not available.")