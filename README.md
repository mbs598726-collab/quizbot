# Quiz Master Bot v1.0

## 1. Project Description

Quiz Master Bot is a beginner-friendly Python quiz application that allows users to take quizzes, answer multiple-choice questions, receive a score, and view a leaderboard.

The project was created as part of the **Applied Agentic AI Foundation Programme — Beginner Track, Month 2**.

The program builds on basic Python concepts such as:

* Lists
* Dictionaries
* Loops
* Functions
* Conditional statements
* User input
* File handling
* JSON data
* Randomization

---

## 2. Features

### Quiz System

The bot asks a series of multiple-choice questions and checks the user's answers.

### Categories

Users can choose from different categories:

* Python
* AI
* General Knowledge
* All Categories

### Difficulty Levels

Users can select:

* Easy
* Medium
* Hard
* All Difficulties

### Score Calculation

The program keeps track of:

* Total questions
* Correct answers
* Wrong answers
* Final score
* Percentage

### Performance Feedback

After completing the quiz, the bot gives feedback based on the user's percentage.

| Percentage    | Feedback                       |
| ------------- | ------------------------------ |
| 90% and above | Outstanding performance        |
| 80%–89%       | Excellent work                 |
| 60%–79%       | Good job                       |
| 40%–59%       | Good attempt                   |
| Below 40%     | Encouragement to keep learning |

### Persistent Scores

The program saves quiz results in a file called:

```text
scores.json
```

This means scores remain available even after the program is closed.

### Leaderboard

The program displays the top three players based on their quiz performance:

```text
1st Rank
2nd Rank
3rd Rank
```

### Random Questions

Questions are shuffled before the quiz begins, so they do not always appear in the same order.

### Input Validation

The program checks user input and prevents invalid options such as entering numbers outside the available range.

---

## 3. Technologies Used

* Python 3
* JSON
* VS Code
* Windows Terminal

Python libraries used:

```python
json
random
os
```

These are built-in Python modules, so no external packages are required.

---

## 4. Project Structure

```text
quizbot/
│
├── quiz.py
│
└── scores.json
```

### quiz.py

Contains the complete Quiz Master Bot program, including:

* Quiz questions
* Category selection
* Difficulty selection
* Quiz logic
* Score calculation
* Performance feedback
* Leaderboard
* File handling

### scores.json

Stores the scores of players who have completed quizzes.

Example:

```json
[
    {
        "name": "Deekshitha",
        "category": "All",
        "difficulty": "All",
        "score": 11,
        "total": 12
    }
]
```

---

## 5. Requirements

Before running the project, make sure Python is installed.

Check Python using:

```text
python --version
```

If Python is installed correctly, you should see something similar to:

```text
Python 3.x.x
```

No additional Python packages are required.

---

## 6. How to Run

### Step 1: Open the Project

Open the `quizbot` folder in VS Code.

### Step 2: Open the Terminal

In VS Code, open:

```text
Terminal → New Terminal
```

### Step 3: Run the Program

Type:

```text
python quiz.py
```

Press Enter.

---

## 7. Main Menu

When the program starts, it displays:

```text
============================================================
QUIZ MASTER BOT v1.0
============================================================
1. Start Quiz
2. View Leaderboard
3. Exit

Enter your choice:
```

### Option 1 — Start Quiz

The user enters their name and selects:

* Category
* Difficulty

The quiz then begins.

### Option 2 — View Leaderboard

Displays the current top players.

### Option 3 — Exit

Closes the program.

---

## 8. Example Quiz

Example:

```text
Question 1:
Which extension is used for Python files?

1. .java
2. .cpp
3. .py
4. .html

Your answer (1-4):
```

If the answer is correct:

```text
Correct!
```

If the answer is incorrect:

```text
Wrong!
Correct answer: .py
```

---

## 9. Example Performance Result

After the quiz:

```text
============================================================
QUIZ COMPLETE
============================================================

Player: Poornima
Questions answered: 10
Correct answers: 8
Wrong answers: 2

============================================================
PERFORMANCE
============================================================

Score: 8/10
Percentage: 80.0%

Excellent work!
You have performed very well.
Keep practicing and continue doing great!
```

---

## 10. Example Ranking

After scores are saved, the program displays the current ranking:

```text
============================================================
CURRENT RANKING
============================================================

1st Rank : Deekshitha - 9/10 (90.0%)
2nd Rank : Poornima - 8/10 (80.0%)
3rd Rank : Rahul - 7/10 (70.0%)
```

The ranking is calculated using the percentage score.

---

## 11. How Score Storage Works

When a player completes the quiz, the program creates a dictionary containing information about the result.

Example:

```python
new_score = {
    "name": "Poornima",
    "category": "AI",
    "difficulty": "Easy",
    "score": 8,
    "total": 10
}
```

This information is stored in `scores.json`.

When the program starts again, it reads the file and loads the previous scores.

Therefore, the leaderboard can survive between program runs.

---

## 12. Python Concepts Demonstrated

### Lists

Questions are stored using a list.

```python
questions = [
    {...},
    {...},
    {...}
]
```

### Dictionaries

Each question contains information stored as key-value pairs.

```python
{
    "question": "What is 2+2?",
    "options": ["3", "4", "5", "6"],
    "answer": 2
}
```

### Loops

Loops are used to go through questions and options.

```python
for question in questions:
    print(question)
```

### Functions

The program is divided into functions such as:

```python
load_scores()
save_score()
choose_category()
choose_difficulty()
run_quiz()
show_performance()
show_ranking()
main()
```

### Conditional Statements

Conditions are used for:

* Checking answers
* Selecting categories
* Selecting difficulty
* Providing performance feedback
* Processing menu choices

### File Handling

The program reads and writes the `scores.json` file.

### JSON

JSON is used to store player results in a structured format.

### Randomization

The `random` module is used to shuffle quiz questions.

---

## 13. Learning Outcomes

By completing this project, the following programming concepts are practiced:

1. How to store information using lists.
2. How to organize information using dictionaries.
3. How to use loops for repeated tasks.
4. How to create and use functions.
5. How to handle user input.
6. How to validate user input.
7. How to calculate scores.
8. How to read and write files.
9. How to use JSON for data storage.
10. How to build a simple interactive application.
11. How to create a persistent leaderboard.
12. How to organize a Python project into reusable functions.

---

## 14. Future Improvements

Possible improvements for future versions include:

* Add more quiz categories.
* Add more questions.
* Allow users to choose the number of questions.
* Add a timer for each question.
* Add negative marking.
* Add a username/profile system.
* Prevent duplicate leaderboard entries.
* Create separate leaderboards for each category.
* Add daily quizzes.
* Add hints.
* Add lifelines.
* Add a graphical user interface.
* Store scores using a database instead of JSON.
* Add an AI-based question generator.
* Allow users to add their own questions.
* Create a web-based version of the Quiz Master Bot.

---

## 15. Version

```text
Version: 1.0
Project: Quiz Master Bot
Track: Beginner Track
Programme: Applied Agentic AI Foundation Programme
Month: 2
Platform: Windows
Language: Python
```

---

## 16. Author

**Poornima**

This project was developed as part of the Applied Agentic AI Foundation Programme Beginner Track.

---

## 17. Conclusion

Quiz Master Bot is a simple but practical Python project that demonstrates how basic programming concepts can be combined to create a useful interactive application.

The project starts with simple lists and dictionaries and extends them into a complete quiz system with scoring, performance feedback, file-based score storage, categories, difficulty levels, and a leaderboard.

It provides a foundation for developing more advanced applications and future AI-powered quiz features.
