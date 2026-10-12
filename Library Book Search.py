books = [
    "Python Basics",
    "Data Science",
    "Web Development",
    "Machine Learning",
    "Artificial Intelligence"
]

search = input("Enter book name: ").lower()

found = False

for book in books:
    if search in book.lower():
        print("Book found:", book)
        found = True

if not found:
    print("Book not found")