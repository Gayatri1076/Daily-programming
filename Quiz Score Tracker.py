questions = {
    "What is the capital of India? ": "delhi",
    "What is 5 + 7? ": "12",
    "Which language uses print()? ": "python",
    "How many days are in a week? ": "7",
    "What is the opposite of hot? ": "cold"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).strip().lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer:", answer)

print("\nYour Score:", score, "/", len(questions))
print("Percentage:", score / len(questions) * 100, "%")