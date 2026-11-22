
from questions import questions

def start_quiz():
    score = 0
    total = len(questions)

    print("=" * 40)
    print("       PYTHON QUIZ GAME")
    print("=" * 40)

    name = input("Enter your name: ")
    print("\nWelcome,", name)
    print("Select the correct option (A/B/C/D).\n")

    for number, q in enumerate(questions, start=1):
        print(f"Question {number}: {q['question']}")

        for option in q["options"]:
            print(option)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid choice. Enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", q["answer"], "\n")

    percentage = (score / total) * 100

    print("=" * 40)
    print("          QUIZ RESULTS")
    print("=" * 40)
    print("Student Name:", name)
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Final Score:", f"{percentage:.2f}%")
    print("=" * 40)

    print("Thank you for playing!")

if __name__ == "__main__":
    start_quiz()
