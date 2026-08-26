import math

num = int(input("Enter a number: "))

print("\n===== NUMBER ANALYZER =====")

# Positive / Negative / Zero
if num > 0:
    print("Type: Positive")
elif num < 0:
    print("Type: Negative")
else:
    print("Type: Zero")

# Even / Odd
if num % 2 == 0:
    print("Number: Even")
else:
    print("Number: Odd")

# Prime Check
if num < 2:
    print("Prime: No")
else:
    prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime: Yes")
    else:
        print("Prime: No")

# Number of digits
digits = len(str(abs(num)))
print("Number of Digits:", digits)