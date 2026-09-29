import random

while True:
    choice = input("Roll the dice? (yes/no): ")

    if choice.lower() == "yes":
        print("You got:", random.randint(1, 6))
    else:
        print("Game Over")
        break