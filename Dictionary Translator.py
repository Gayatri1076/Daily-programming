translator = {
    "hello": "namaste",
    "thank you": "dhanyawad",
    "good morning": "suprabhat",
    "water": "paani",
    "friend": "dost",
    "book": "pustak",
    "school": "shala",
    "love": "prem"
}

word = input("Enter an English word: ").lower()

if word in translator:
    print("Meaning:", translator[word])
else:
    print("Word not found!")