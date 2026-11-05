import random

options = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

for round_no in range(1, 6):
    print("\nRound", round_no)

    user = input("Choose Rock, Paper or Scissors: ").title()

    if user not in options:
        print("Invalid choice!")
        continue

    computer = random.choice(options)

    print("Computer:", computer)

    if user == computer:
        print("Draw!")

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):

        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

print("\nFinal Score")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Congratulations! You won!")
elif user_score < computer_score:
    print("Computer won!")
else:
    print("Tournament Draw!")