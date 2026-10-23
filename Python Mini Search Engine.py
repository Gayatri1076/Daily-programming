documents = {
    "Python": "Python is a programming language",
    "Java": "Java is used for application development",
    "HTML": "HTML is used to create web pages",
    "AI": "Artificial Intelligence helps machines learn"
}

search = input("Search topic: ").lower()

found = False

for title, content in documents.items():
    if search in title.lower() or search in content.lower():
        print("\nTitle:", title)
        print("Content:", content)
        found = True

if not found:
    print("No results found")