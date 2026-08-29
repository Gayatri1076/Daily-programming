import time

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    minutes = seconds // 60
    remaining_seconds = seconds % 60

    print(
        f"\rTime Left: {minutes:02d}:{remaining_seconds:02d}",
        end=""
    )

    time.sleep(1)
    seconds -= 1

print("\nTime's Up! ⏰")