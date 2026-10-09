import random

choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice")
elif user == computer:
    print("It's a Draw!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You Win!")
else:
    print("Computer Wins!")