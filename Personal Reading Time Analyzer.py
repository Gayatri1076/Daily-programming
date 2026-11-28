reading = {}

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    minutes = int(input(f"Enter reading minutes for {day}: "))
    reading[day] = minutes

total = sum(reading.values())
average = total / 7

best_day = max(reading, key=reading.get)

print("\n----- Reading Report -----")
print("Total Reading Time:", total, "minutes")
print("Average Per Day:", round(average, 2), "minutes")
print("Most Active Day:", best_day)
print("Total Hours:", round(total / 60, 2))

print("\nDaily Reading:")
for day, minutes in reading.items():
    print(day, ":", minutes, "minutes")