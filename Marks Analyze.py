marks = list(map(int, input("Enter marks of 5 subjects: ").split()))

total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")