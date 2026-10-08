text = input("Enter a sentence: ")

words = text.split()

reversed_words = words[::-1]

print("Reversed sentence:", " ".join(reversed_words))