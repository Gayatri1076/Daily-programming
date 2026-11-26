weather = input("Enter weather (sunny/rainy/cold/windy): ").lower()
temperature = float(input("Enter temperature in Celsius: "))

if weather == "rainy":
    print("Suggestion: Carry an umbrella and wear a raincoat!")

elif weather == "sunny":
    print("Suggestion: Wear light clothes and carry sunglasses!")

elif weather == "cold":
    print("Suggestion: Wear warm clothes!")

elif weather == "windy":
    print("Suggestion: Wear a jacket!")

else:
    print("Weather condition not recognized!")

if temperature < 10:
    print("Extra Advice: Wear warm layers.")
elif temperature > 30:
    print("Extra Advice: Stay hydrated.")
else:
    print("Extra Advice: Enjoy your day!")