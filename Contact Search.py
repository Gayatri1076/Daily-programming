contacts = {
    "Rahul": "9876543210",
    "Priya": "8765432109",
    "Amit": "7654321098",
    "Sneha": "9876501234"
}

name = input("Enter contact name: ").strip().title()

if name in contacts:
    print("Name:", name)
    print("Phone Number:", contacts[name])
else:
    print("Contact not found!")