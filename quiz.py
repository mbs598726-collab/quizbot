import json
import random
import os

SCORE_FILE = "scores.json"


# ============================================================
# QUIZ QUESTIONS
# ============================================================

questions = [

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which symbol is used to write a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": 2
    },

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which extension is used for Python files?",
        "options": [".java", ".cpp", ".py", ".html"],
        "answer": 3
    },

    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": 3
    },

    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "Which data type is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": 4
    },

    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "What does AI stand for?",
        "options": [
            "Automated Internet",
            "Artificial Intelligence",
            "Advanced Information",
            "Artificial Internet"
        ],
        "answer": 2
    },

    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "Which of these is an example of AI?",
        "options": [
            "Calculator",
            "Voice assistant",
            "Keyboard",
            "USB cable"
        ],
        "answer": 2
    },

    {
        "category": "AI",
        "difficulty": "Medium",
        "question": "What is Machine Learning?",
        "options": [
            "A type of hardware",
            "A method where computers learn from data",
            "A programming language",
            "A computer game"
        ],
        "answer": 2
    },

    {
        "category": "AI",
        "difficulty": "Hard",
        "question": "Which type of learning uses labelled data?",
        "options": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Random Learning",
            "Manual Learning"
        ],
        "answer": 1
    },

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "What is the capital of India?",
        "options": [
            "Mumbai",
            "New Delhi",
            "Bengaluru",
            "Chennai"
        ],
        "answer": 2
    },

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": 3
    },

    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which planet is known as the Red Planet?",
        "options": [
            "Earth",
            "Mars",
            "Jupiter",
            "Venus"
        ],
        "answer": 2
    },

    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "Which is the largest ocean on Earth?",
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Arctic Ocean",
            "Pacific Ocean"
        ],
        "answer": 4
    }
]


# ============================================================
# LOAD SCORES
# ============================================================

def load_scores():

    if os.path.exists(SCORE_FILE):

        try:

            with open(SCORE_FILE, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):

            return []

    return []


# ============================================================
# SAVE SCORE
# ============================================================

def save_score(name, category, difficulty, score, total):

    scores = load_scores()

    player_score = {
        "name": name,
        "category": category,
        "difficulty": difficulty,
        "score": score,
        "total": total
    }

    scores.append(player_score)

    with open(SCORE_FILE, "w") as file:

        json.dump(scores, file, indent=4)


# ============================================================
# SHOW TOP 3 RANKS
# ============================================================

def show_top_three():

    scores = load_scores()

    if not scores:

        print("\nNo scores available yet.")
        return

    scores.sort(
        key=lambda x: (x["score"] / x["total"]),
        reverse=True
    )

    print("\n")
    print("=" * 60)
    print("TOP 3 RANKS")
    print("=" * 60)

    top_three = scores[:3]

    for i, player in enumerate(top_three, start=1):

        percentage = (
            player["score"] / player["total"]
        ) * 100

        if i == 1:
            rank = "1st"

        elif i == 2:
            rank = "2nd"

        else:
            rank = "3rd"

        print(
            f"{rank} Rank: {player['name']} - "
            f"{player['score']}/{player['total']} "
            f"({percentage:.1f}%)"
        )


# ============================================================
# SHOW FULL LEADERBOARD
# ============================================================

def show_leaderboard():

    scores = load_scores()

    print("\n")
    print("=" * 60)
    print("LEADERBOARD")
    print("=" * 60)

    if not scores:

        print("No scores recorded yet.")
        return

    scores.sort(
        key=lambda x: (x["score"] / x["total"]),
        reverse=True
    )

    for i, player in enumerate(scores, start=1):

        percentage = (
            player["score"] / player["total"]
        ) * 100

        print(
            f"{i}. {player['name']} - "
            f"{player['score']}/{player['total']} "
            f"({percentage:.1f}%) - "
            f"{player['category']} - "
            f"{player['difficulty']}"
        )

    show_top_three()


# ============================================================
# CHOOSE CATEGORY
# ============================================================

def choose_category():

    categories = sorted(
        set(question["category"] for question in questions)
    )

    print("\nChoose a category:")

    for i, category in enumerate(categories, start=1):

        print(f"{i}. {category}")

    print("0. All Categories")

    while True:

        choice = input("Enter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if choice == 0:

                return "All"

            if 1 <= choice <= len(categories):

                return categories[choice - 1]

        print("Invalid choice. Please try again.")


# ============================================================
# CHOOSE DIFFICULTY
# ============================================================

def choose_difficulty():

    difficulties = [
        "Easy",
        "Medium",
        "Hard"
    ]

    print("\nChoose difficulty:")

    for i, difficulty in enumerate(difficulties, start=1):

        print(f"{i}. {difficulty}")

    print("0. All Difficulties")

    while True:

        choice = input("Enter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if choice == 0:

                return "All"

            if 1 <= choice <= len(difficulties):

                return difficulties[choice - 1]

        print("Invalid choice. Please try again.")


# ============================================================
# SHOW PERFORMANCE MESSAGE
# ============================================================

def show_performance(score, total):

    percentage = (score / total) * 100

    print("\n")
    print("=" * 60)
    print("YOUR PERFORMANCE")
    print("=" * 60)

    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 90:

        print("Outstanding performance!")
        print("You have done an excellent job. Keep it up!")

    elif percentage >= 80:

        print("Excellent work!")
        print("You have a very good understanding of the topic.")

    elif percentage >= 60:

        print("Good job!")
        print("You are doing well. Keep practicing to improve further.")

    elif percentage >= 40:

        print("Good attempt!")
        print("You can improve with a little more practice. Do not give up!")

    else:

        print("Keep learning and keep trying!")
        print("Every attempt helps you improve. Practice and try again!")


# ============================================================
# RUN QUIZ
# ============================================================

def run_quiz(name, category, difficulty):

    selected_questions = []

    for question in questions:

        category_match = (
            category == "All"
            or question["category"] == category
        )

        difficulty_match = (
            difficulty == "All"
            or question["difficulty"] == difficulty
        )

        if category_match and difficulty_match:

            selected_questions.append(question)

    if not selected_questions:

        print("\nNo questions available for this selection.")
        return

    random.shuffle(selected_questions)

    print("\n")
    print("=" * 60)
    print("QUIZ STARTED")
    print("=" * 60)

    print(f"Player: {name}")
    print(f"Category: {category}")
    print(f"Difficulty: {difficulty}")
    print(f"Number of questions: {len(selected_questions)}")

    score = 0

    for number, question in enumerate(
        selected_questions,
        start=1
    ):

        print("\n")
        print("-" * 60)

        print(f"Question {number}:")
        print(question["question"])

        print()

        for i, option in enumerate(
            question["options"],
            start=1
        ):

            print(f"{i}. {option}")

        while True:

            answer = input("\nYour answer (1-4): ")

            if answer.isdigit():

                answer = int(answer)

                if 1 <= answer <= 4:

                    break

            print("Please enter a number between 1 and 4.")

        if answer == question["answer"]:

            print("Correct!")
            score += 1

        else:

            correct_option = question["options"][
                question["answer"] - 1
            ]

            print("Wrong!")
            print(f"Correct answer: {correct_option}")

    total = len(selected_questions)

    print("\n")
    print("=" * 60)
    print("QUIZ COMPLETE")
    print("=" * 60)

    print(f"Player: {name}")
    print(f"Questions answered: {total}")
    print(f"Correct answers: {score}")
    print(f"Wrong answers: {total - score}")

    show_performance(score, total)

    save_score(
        name,
        category,
        difficulty,
        score,
        total
    )

    print("\nYour score has been saved.")

    show_top_three()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("QUIZ MASTER BOT v1.0")
        print("=" * 60)

        print("1. Start Quiz")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            name = input("\nEnter your name: ").strip()

            if name == "":

                name = "Player"

            category = choose_category()

            difficulty = choose_difficulty()

            run_quiz(
                name,
                category,
                difficulty
            )

        elif choice == "2":

            show_leaderboard()

        elif choice == "3":

            print("\nThanks for playing Quiz Master Bot!")

            break

        else:

            print("Invalid choice. Please select 1, 2 or 3.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()