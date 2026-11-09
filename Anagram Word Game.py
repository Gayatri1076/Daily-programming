import random

words = ["python", "computer", "science", "program", "keyboard"]

word = random.choice(words)
jumbled = "".join(random.sample(word, len(word)))

print("Guess the correct word!")
print("Jumbled word:", jumbled)

answer = input("Your answer: ").lower()

if answer == word:
    print("Correct! You won!")
else:
    print("Wrong answer!")
    print("Correct word:", word)