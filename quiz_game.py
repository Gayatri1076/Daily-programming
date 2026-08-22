questions = [
    {
        "question": "Which language is used for data analysis?",
        "options": ["1. Python", "2. HTML", "3. CSS", "4. SQL"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1. function", "2. def", "3. fun", "4. define"],
        "answer": 2
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["1. int", "2. string", "3. bool", "4. list"],
        "answer": 3
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["1. //", "2. #", "3. /*", "4. --"],
        "answer": 2
    },
    {
        "question": "Which function is used to display output?",
        "options": ["1. print()", "2. display()", "3. show()", "4. output()"],
        "answer": 1
    }
]

score = 0

print("===== PYTHON QUIZ GAME =====")

for i, q in enumerate(questions, start=1):

    print(f"\nQ{i}. {q['question']}")

    for option in q["options"]:
        print(option)

    answer = int(input("Enter your answer: "))

    if answer == q["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")

print("\n===== RESULT =====")
print(f"Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent! 🎉")
elif percentage >= 50:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 💪")