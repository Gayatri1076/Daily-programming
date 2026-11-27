import difflib

words = ["python", "programming", "computer", "database",
         "software", "developer", "algorithm", "technology"]

word = input("Enter a word: ").lower()

if word in words:
    print("Correct spelling!")
else:
    suggestions = difflib.get_close_matches(word, words, n=3)

    if suggestions:
        print("Did you mean:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("No suggestions found!")