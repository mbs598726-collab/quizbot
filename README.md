# 🧠 Quiz Master Bot — Advanced GUI Edition

A polished, dark-themed desktop quiz application built with Python and CustomTkinter. This is a full GUI upgrade of an original console-based Quiz Master Bot project — all the original logic (categories, difficulty levels, scoring, and a persistent leaderboard) is preserved, wrapped in a modern, professional, glowing interface.

Everything lives in a **single file** (`quiz.py`) for easy sharing and running.

## Description

Quiz Master Bot lets a player pick a category and difficulty, answer a set of multiple-choice questions, and see their results with performance feedback — all inside a sleek, black-and-electric-blue desktop application with soft neon glow effects. Scores are saved to a local JSON file, so the leaderboard persists across sessions.

## Features

- 🖥️ Modern desktop GUI (CustomTkinter) — no terminal required
- 🎨 Premium "neon aurora" dark theme: black, deep navy, electric blue, violet, and cyan accents
- ✨ Real layered glow effects on cards, a glossy sheen highlight, and a soft "bloom" behind the title text
- 💫 Subtle breathing pulse animation on the primary Start Quiz buttons
- 📚 Multiple categories: Python, AI, General Knowledge (easy to extend)
- 🎚️ Three difficulty levels: Easy, Medium, Hard
- 🔀 Randomized question order and randomized answer option order
- ✅ Instant, color-coded answer feedback (correct/incorrect highlighting with glowing borders)
- 📊 Live score, correct/wrong tracking, and a glowing gradient progress bar during the quiz
- 🏆 Persistent leaderboard (JSON-based), sorted fairly by percentage then score
- 🥇 Top-3 highlighting on the leaderboard (gold / silver / bronze glow)
- 🛡️ Safe error handling for missing/corrupted score files, empty names, and invalid settings
- 📖 Built-in "How to Play" screen
- 🧩 Clean, beginner-readable code organized into clearly labeled sections/classes

## Technologies Used

- Python 3.9+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the GUI
- Standard library: `json`, `random`, `os`, `tkinter`, `tkinter.messagebox`

## Installation

1. Make sure Python 3.9 or newer is installed (check with `python --version`).
2. (Optional but recommended) create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install the only external dependency:

   ```bash
   pip install customtkinter
   ```

> **Linux users:** if you get a `tkinter` import error, install it via your
> package manager first, e.g. `sudo apt install python3-tk` on Ubuntu/Debian.

## How to Run

From the folder containing `quiz.py`, run:

```bash
python quiz.py
```

The application window opens at 1200x750 and can be resized.

## Project Structure

```
quizbot/
│
├── quiz.py          # The entire application: questions, logic, and GUI
└── scores.json       # Created automatically after your first quiz
```

Everything is intentionally kept in one file — the question database, the
`QuestionManager`, `ScoreManager`, and `LeaderboardManager` classes, and the
full `QuizApp` GUI — organized into clearly labeled sections at the top of
`quiz.py`, so it's simple to read top-to-bottom or drop into a single-file
portfolio project.

## How Scoring Works

- Each correct answer adds **1 point** to your score.
- Your final **percentage** = `(correct answers / total questions) × 100`.
- The **leaderboard** ranks players by **percentage first**, and by **raw
  score** as a tiebreaker. Both score and percentage are always shown
  together, so quizzes of different lengths stay easy to compare fairly.

## Adding New Questions

Open `quiz.py` and find the `QUESTIONS` list near the top of the file. Add a
new dictionary like this:

```python
{
    "category": "Python",
    "difficulty": "Easy",
    "question": "Which symbol is used for comments?",
    "options": ["//", "#", "/*", "--"],
    "answer": 1,   # index of the correct option (starts at 0)
}
```

New categories are picked up automatically — no other code changes needed.

## Customizing the Look

All colors live in one place near the top of the GUI section (search for
`THEME v2` in `quiz.py`) as simple hex constants like `COLOR_GLOW`,
`COLOR_GLOW_2`, and `COLOR_BG`. Changing these values re-themes the whole
app, since every screen and widget pulls from these constants rather than
hardcoding its own colors.

## Future Improvements

These are intentionally **not implemented** yet, so the app never claims to
be "AI-powered" without an actual connected AI service:

- AI-generated questions
- AI explanations for wrong answers
- Adaptive/AI-based difficulty adjustment
- Personalized quizzes based on player history
- AI study recommendations
- Topic weakness analysis

The code is structured so these can be added later without a rewrite.

## What Changed From the Original Console Version

- Replaced all `input()`/`print()` interaction with a full CustomTkinter GUI
  organized into swappable screens (Home, Setup, Quiz, Results, Leaderboard,
  Categories, How to Play) inside a single window.
- Added a dashboard-style Home screen with live statistics and a glowing
  neon title.
- Added a dedicated Player Setup screen with dropdowns and radio buttons
  instead of typed console prompts.
- Added visual answer feedback (color-coded correct/incorrect highlighting
  with glowing borders) and a glowing gradient progress bar.
- Added a "Next Question" flow that prevents double-answering.
- Kept the original scoring, category/difficulty filtering, question
  randomization, and JSON-based leaderboard persistence fully intact.
- Added defensive error handling throughout so common mistakes (empty name,
  missing/corrupted `scores.json`, no matching questions) show a friendly
  message instead of crashing.

## Security & Data

The app only ever stores the player's chosen display name and quiz results
in `scores.json`. No passwords, emails, or other personal information are
collected or transmitted anywher.

## Author

Poornima M S ,Github profile link -mbs598726-collab