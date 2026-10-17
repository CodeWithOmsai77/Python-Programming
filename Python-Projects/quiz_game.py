"""A small multiple-choice quiz using lists and dictionaries."""

QUESTIONS = [
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": 3,
    },
    {
        "question": "Which keyword defines a function?",
        "options": ["func", "def", "function", "make"],
        "answer": 2,
    },
    {
        "question": "Which loop is useful when you know the items to visit?",
        "options": ["for", "switch", "try", "class"],
        "answer": 1,
    },
    {
        "question": "Which keyword creates a class in Python?",
        "options": ["object", "new", "struct", "class"],
        "answer": 4,
    },
    {
        "question": "Which mode opens a file for appending text?",
        "options": ["r", "w", "a", "x"],
        "answer": 3,
    },
]


def ask_question(number, question):
    print(f"\nQ{number}. {question['question']}")
    for option_number, option in enumerate(question["options"], start=1):
        print(f"  {option_number}. {option}")

    while True:
        answer = input("Your answer (1-4): ").strip()
        if answer in {"1", "2", "3", "4"}:
            return int(answer)
        print("Please enter 1, 2, 3, or 4.")


def main():
    score = 0
    print("===== Python Basics Quiz =====")

    for number, question in enumerate(QUESTIONS, start=1):
        answer = ask_question(number, question)
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            correct = question["options"][question["answer"] - 1]
            print(f"Not quite. Correct answer: {correct}")

    print(f"\nFinal score: {score}/{len(QUESTIONS)}")
    percentage = score / len(QUESTIONS) * 100
    print(f"Result: {percentage:.0f}%")


if __name__ == "__main__":
    main()
