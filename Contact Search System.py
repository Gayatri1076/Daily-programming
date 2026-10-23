contacts = {
    "Rahul": "9876543210",
    "Priya": "9123456780",
    "Amit": "9988776655"
}

name = input("Enter contact name: ").strip().title()

if name in contacts:
    print("Name:", name)
    print("Phone:", contacts[name])
else:
    print("Contact not found!")
    choice = input("Add this contact? (yes/no): ")

    if choice.lower() == "yes":
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

print("\nAll Contacts:")

for name, phone in contacts.items():
    print(name, ":", phone)