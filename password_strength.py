import string

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

print("\n===== PASSWORD ANALYSIS =====")

if score == 5:
    print("Strength: Strong")
elif score >= 3:
    print("Strength: Medium")
else:
    print("Strength: Weak")

print("Score:", score, "/ 5")