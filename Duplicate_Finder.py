numbers = list(map(int, input("Enter numbers: ").split()))

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate numbers:", duplicates)