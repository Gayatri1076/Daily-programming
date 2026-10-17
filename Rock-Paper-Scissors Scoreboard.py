import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

for round_num in range(1, 6):
    print("\nRound", round_num)
    user = input("Choose rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print("Computer:", computer)

    if user == computer:
        print("Draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("\nYour Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("You won the game!")
elif user_score < computer_score:
    print("Computer won the game!")
else:
    print("The game is a draw!")