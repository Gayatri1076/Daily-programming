file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    print("\n===== FILE ANALYSIS =====")
    print("Lines      :", len(lines))
    print("Words      :", len(words))
    print("Characters :", characters)

except FileNotFoundError:
    print("File not found!")