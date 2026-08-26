"""
quiz.py
--------
QUIZ MASTER BOT - Advanced GUI Version (Single-File Edition)

A polished, dark-themed desktop quiz application built with CustomTkinter.
This upgrades the original console-based Quiz Master Bot into a modern
graphical application while preserving all of its original functionality:

    - Multiple-choice questions with categories and difficulty levels
    - Randomized question and answer order
    - Score, correct/wrong tracking, and percentage calculation
    - Performance feedback messages
    - JSON-based persistent leaderboard with safe error handling

Everything (question database, question filtering, score saving/loading,
leaderboard ranking, and the GUI itself) lives in this one file for easy
sharing and running.

Run with:
    python quiz.py

Install dependency first with:
    pip install -r requirements.txt
    (or simply: pip install customtkinter)
"""

import json
import os
import random
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk


# ============================================================
# SECTION 1: QUESTION DATABASE
# ============================================================
# Each question is a dictionary with this structure:
#
# {
#     "category": "Python",
#     "difficulty": "Easy",
#     "question": "Which symbol is used for comments?",
#     "options": ["//", "#", "/*", "--"],
#     "answer": 1   # index of the correct option in "options"
# }
#
# To add a new question, just append a new dictionary to QUESTIONS below.
# Make sure "answer" is the INDEX (starting at 0) of the correct option.

QUESTIONS = [
    # ---------------- PYTHON - EASY ----------------
    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which of these is a valid Python variable name?",
        "options": ["2value", "value_2", "value-2", "value 2"],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "What is the output of print(type(5))?",
        "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
        "answer": 0,
    },
    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which data type is used to store True or False in Python?",
        "options": ["int", "str", "bool", "float"],
        "answer": 2,
    },
    # ---------------- PYTHON - MEDIUM ----------------
    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "What does the len() function do?",
        "options": [
            "Returns the largest item",
            "Returns the length of an object",
            "Returns the type of an object",
            "Deletes an object",
        ],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which method adds an item to the end of a list?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".pt", ".pyt", ".python"],
        "answer": 0,
    },
    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which of these is used to handle exceptions in Python?",
        "options": ["try/except", "catch/throw", "if/else", "switch/case"],
        "answer": 0,
    },
    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "What does the 'json' module help you do?",
        "options": [
            "Draw graphics",
            "Work with JSON data",
            "Connect to databases",
            "Create GUIs",
        ],
        "answer": 1,
    },
    # ---------------- PYTHON - HARD ----------------
    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "What is a Python decorator primarily used for?",
        "options": [
            "Styling the console output",
            "Wrapping a function to extend its behavior",
            "Declaring global variables",
            "Importing modules faster",
        ],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "What does the 'yield' keyword do?",
        "options": [
            "Ends a loop immediately",
            "Turns a function into a generator",
            "Raises an exception",
            "Declares a constant",
        ],
        "answer": 1,
    },
    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "Which of these best describes Python's GIL?",
        "options": [
            "A tool for GUI design",
            "A lock that allows only one thread to execute Python bytecode at a time",
            "A garbage collector for images",
            "A library for graphs",
        ],
        "answer": 1,
    },
    # ---------------- AI - EASY ----------------
    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "What does AI stand for?",
        "options": ["Automated Internet", "Artificial Intelligence", "Advanced Integration", "Applied Informatics"],
        "answer": 1,
    },
    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "Which of these is an example of an AI application?",
        "options": ["Voice assistants", "A basic calculator", "A text editor", "A calendar app"],
        "answer": 0,
    },
    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "What is Machine Learning?",
        "options": [
            "A way for machines to learn patterns from data",
            "A type of computer hardware",
            "A programming language",
            "A method for storing files",
        ],
        "answer": 0,
    },
    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "Which term refers to data used to train an AI model?",
        "options": ["Output data", "Training data", "Cache data", "Static data"],
        "answer": 1,
    },
    {
        "category": "AI",
        "difficulty": "Easy",
        "question": "What is a chatbot?",
        "options": [
            "A program that simulates conversation",
            "A type of database",
            "A hardware chip",
            "A network cable",
        ],
        "answer": 0,
    },
    # ---------------- AI - MEDIUM ----------------
    {
        "category": "AI",
        "difficulty": "Medium",
        "question": "What is a neural network inspired by?",
        "options": ["The human brain", "Traffic systems", "Water pipelines", "Computer chips only"],
        "answer": 0,
    },
    {
        "category": "AI",
        "difficulty": "Medium",
        "question": "What does 'supervised learning' require?",
        "options": [
            "No data at all",
            "Labeled training data",
            "Only images",
            "Manual coding of every rule",
        ],
        "answer": 1,
    },
    {
        "category": "AI",
        "difficulty": "Medium",
        "question": "What is overfitting in machine learning?",
        "options": [
            "When a model performs well on training data but poorly on new data",
            "When a model uses too little memory",
            "When training happens too fast",
            "When a dataset has too few features",
        ],
        "answer": 0,
    },
    {
        "category": "AI",
        "difficulty": "Medium",
        "question": "Which of these is a popular machine learning library in Python?",
        "options": ["scikit-learn", "Photoshop", "AutoCAD", "Excel"],
        "answer": 0,
    },
    # ---------------- AI - HARD ----------------
    {
        "category": "AI",
        "difficulty": "Hard",
        "question": "What is the main idea behind 'reinforcement learning'?",
        "options": [
            "Learning from labeled examples only",
            "Learning by receiving rewards or penalties from actions",
            "Learning by memorizing a fixed dataset",
            "Learning without any feedback",
        ],
        "answer": 1,
    },
    {
        "category": "AI",
        "difficulty": "Hard",
        "question": "What does 'backpropagation' do in a neural network?",
        "options": [
            "Sends data backward through the internet",
            "Adjusts weights by propagating error gradients backward",
            "Deletes unused neurons",
            "Compresses the training dataset",
        ],
        "answer": 1,
    },
    {
        "category": "AI",
        "difficulty": "Hard",
        "question": "What is a transformer architecture primarily known for?",
        "options": [
            "Handling sequential data using self-attention",
            "Converting electricity voltages",
            "Compressing images losslessly",
            "Managing databases",
        ],
        "answer": 0,
    },
    # ---------------- GENERAL KNOWLEDGE - EASY ----------------
    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": 2,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": 1,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": 3,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "How many days are there in a leap year?",
        "options": ["364", "365", "366", "367"],
        "answer": 2,
    },
    # ---------------- GENERAL KNOWLEDGE - MEDIUM ----------------
    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "answer": 1,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": 2,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "What is the currency of Japan?",
        "options": ["Won", "Yuan", "Yen", "Ringgit"],
        "answer": 2,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["Liver", "Lungs", "Heart", "Kidney"],
        "answer": 2,
    },
    # ---------------- GENERAL KNOWLEDGE - HARD ----------------
    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "In which year did the first World War begin?",
        "options": ["1905", "1914", "1920", "1939"],
        "answer": 1,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 2,
    },
    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "Which element has the chemical symbol 'Au'?",
        "options": ["Silver", "Gold", "Aluminum", "Argon"],
        "answer": 1,
    },
]


# ============================================================
# SECTION 2: QUESTION MANAGER
# ============================================================
# Handles filtering, randomizing, and serving quiz questions.

class QuestionManager:
    """Responsible for filtering, randomizing, and serving quiz questions."""

    def __init__(self, all_questions=None):
        # Keep an internal copy so the original QUESTIONS list is never modified.
        self.all_questions = list(all_questions) if all_questions is not None else list(QUESTIONS)

    def get_categories(self):
        """Return a sorted list of unique categories found in the question bank."""
        categories = {q["category"] for q in self.all_questions}
        return sorted(categories)

    def get_difficulties(self):
        """Return the standard difficulty levels available."""
        return ["Easy", "Medium", "Hard"]

    def total_questions(self):
        """Return the total number of questions in the database."""
        return len(self.all_questions)

    def get_filtered_questions(self, category="All Categories", difficulty="All", num_questions=None):
        """
        Return a randomized, filtered list of questions ready for a quiz session.

        category: "All Categories" or a specific category name
        difficulty: "All" or a specific difficulty name
        num_questions: an integer, or None/"All Available" to use every matching question

        Each returned question dictionary is a fresh copy with its own shuffled
        options list, so the original QUESTIONS data is never mutated and
        answer indexes remain correct after shuffling.
        """
        filtered = []
        for q in self.all_questions:
            category_ok = (category == "All Categories") or (q["category"] == category)
            difficulty_ok = (difficulty == "All") or (q["difficulty"] == difficulty)
            if category_ok and difficulty_ok:
                filtered.append(q)

        # Shuffle the order of the questions themselves.
        random.shuffle(filtered)

        # Trim to the requested number of questions, if a specific number was given.
        if num_questions is not None and num_questions != "All Available":
            try:
                num_questions = int(num_questions)
                filtered = filtered[:num_questions]
            except (ValueError, TypeError):
                pass  # If conversion fails, just use all filtered questions.

        # Build fresh copies with shuffled answer options so the correct
        # answer index still points to the right option after shuffling.
        prepared = []
        for q in filtered:
            prepared.append(self._shuffle_options(q))

        return prepared

    @staticmethod
    def _shuffle_options(question):
        """
        Return a new question dictionary with the options shuffled and the
        'answer' index updated so it still points to the correct option.
        """
        options = list(question["options"])
        correct_text = options[question["answer"]]

        shuffled = list(options)
        random.shuffle(shuffled)
        new_answer_index = shuffled.index(correct_text)

        new_question = dict(question)
        new_question["options"] = shuffled
        new_question["answer"] = new_answer_index
        return new_question


# ============================================================
# SECTION 3: SCORE MANAGER
# ============================================================
# Handles loading and saving player scores to/from scores.json.
# Designed to fail safely: a missing or corrupted file never crashes the app.

class ScoreManager:
    """Responsible for persisting quiz results to a JSON file."""

    def __init__(self, filepath="scores.json"):
        self.filepath = filepath

    def load_scores(self):
        """
        Load all saved scores from disk.

        Returns a list of score dictionaries. If the file does not exist,
        is empty, or contains invalid JSON, an empty list is returned
        instead of raising an exception.
        """
        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                if isinstance(data, list):
                    return data
                return []  # Corrupted structure (e.g. a dict instead of a list).
        except (json.JSONDecodeError, OSError, ValueError):
            # Corrupted file or unreadable file -> treat as no scores saved.
            return []

    def save_score(self, player_name, score, total, percentage, category, difficulty):
        """
        Append a new score entry to scores.json and save it to disk.
        Returns True on success, False if saving failed for any reason.
        """
        scores = self.load_scores()

        new_entry = {
            "player": player_name,
            "score": score,
            "total": total,
            "percentage": round(percentage, 1),
            "category": category,
            "difficulty": difficulty,
        }
        scores.append(new_entry)

        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(scores, f, indent=4)
            return True
        except OSError:
            return False


# ============================================================
# SECTION 4: LEADERBOARD MANAGER
# ============================================================
# Fairness rule: players are ranked primarily by PERCENTAGE, not raw score,
# since quizzes can have different lengths (e.g. 5 vs 10 questions).
# If two players share the same percentage, the one with the higher raw
# score (i.e. the longer/harder quiz) is ranked higher, since achieving the
# same percentage on more questions is a stronger result.

class LeaderboardManager:
    """Responsible for sorting and ranking score entries."""

    def __init__(self, score_manager):
        self.score_manager = score_manager

    def get_ranked_scores(self):
        """
        Return all scores sorted by:
          1. Percentage (highest first)
          2. Raw score (highest first) as a tiebreaker
        """
        scores = self.score_manager.load_scores()

        def sort_key(entry):
            percentage = entry.get("percentage", 0)
            score = entry.get("score", 0)
            return (-percentage, -score)

        return sorted(scores, key=sort_key)

    def get_top_players(self, limit=None):
        """Return the top N ranked players (or all of them if limit is None)."""
        ranked = self.get_ranked_scores()
        if limit is not None:
            return ranked[:limit]
        return ranked

    def player_count(self):
        """Return the number of unique players who have played at least once."""
        scores = self.score_manager.load_scores()
        players = {entry.get("player", "").strip().lower() for entry in scores if entry.get("player")}
        return len(players)


# ============================================================
# SECTION 5: GUI APPLICATION
# ============================================================

# THEME v2 - Premium "Neon Aurora" palette: Black + Deep Navy + Electric
# Blue + a violet-cyan duotone glow, for a more advanced, shinier look.
# ============================================================

COLOR_BG = "#03040a"            # near-black background (slightly blue-black)
COLOR_BG_ALT = "#080b16"        # slightly lighter panel background
COLOR_CARD = "#0a0f1f"          # dark navy card background
COLOR_CARD_ALT = "#101832"      # secondary card shade (hover/active surfaces)
COLOR_CARD_RAISED = "#141d3c"   # raised surface (answer buttons, chips)
COLOR_BORDER = "#20305a"        # subtle border for cards
COLOR_BORDER_SOFT = "#141f3a"   # even softer border for nested elements

# Duotone glow: electric blue blended with a violet accent for a richer,
# more "AI premium" feel than a single flat blue.
COLOR_GLOW = "#2f8fff"          # electric blue - primary glow / accent
COLOR_GLOW_2 = "#7c5cff"        # violet - secondary glow, used for depth
COLOR_GLOW_CYAN = "#3fe0ff"     # cyan - used for sheen highlights & sparkle
COLOR_GLOW_SOFT = "#15335e"     # dim glow tone for outer falloff rings
COLOR_GLOW_DIM = "#0d1f3c"      # dimmest glow tone, closest to background
COLOR_ACCENT_LIGHT = "#a9d6ff"  # light blue for highlighted text
COLOR_ACCENT_LIGHT2 = "#d8ccff" # light violet for secondary highlighted text

COLOR_TEXT = "#f3f7ff"          # primary near-white text
COLOR_TEXT_DIM = "#7f8fb8"      # secondary/muted text
COLOR_SUCCESS = "#3ee08a"       # green for correct answers
COLOR_SUCCESS_DIM = "#0f3a26"
COLOR_ERROR = "#ff5f72"         # red/pink for wrong answers
COLOR_ERROR_DIM = "#3a0f18"
COLOR_GOLD = "#ffd15c"          # 1st place
COLOR_SILVER = "#d7e0f2"        # 2nd place
COLOR_BRONZE = "#e8a56a"        # 3rd place

FONT_FAMILY = "Segoe UI"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750


def make_font(size, weight="normal"):
    """Helper to build a CTkFont without repeating the family name everywhere."""
    return ctk.CTkFont(family=FONT_FAMILY, size=size, weight=weight)


def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*[max(0, min(255, int(c))) for c in rgb])


def blend(color_a, color_b, t):
    """Linearly blend two hex colors. t=0 -> color_a, t=1 -> color_b."""
    a = _hex_to_rgb(color_a)
    b = _hex_to_rgb(color_b)
    mixed = tuple(a[i] + (b[i] - a[i]) * t for i in range(3))
    return _rgb_to_hex(mixed)


class GlowCard(ctk.CTkFrame):
    """
    A reusable 'card' frame that simulates a soft, layered light glow
    (like a light source falling off behind glass) instead of a single
    flat-colored border. Built from several nested frames whose colors
    step from the bright glow color down toward the background, plus a
    thin brighter "sheen" strip along the top-inside edge of the card to
    mimic light catching the top of a glossy panel.
    """

    def __init__(self, parent, glow_color=COLOR_GLOW, border_width=2,
                 corner_radius=20, fg_color=COLOR_CARD, glow_layers=3,
                 sheen=True, **kwargs):
        # Outermost layer: the dimmest falloff ring, closest to the background.
        outer_color = blend(COLOR_BG, glow_color, 0.35)
        super().__init__(
            parent,
            fg_color=outer_color,
            corner_radius=corner_radius,
            **kwargs,
        )

        # Middle layer: a mid-brightness ring for a soft falloff step.
        mid_color = blend(COLOR_BG, glow_color, 0.65)
        self._mid = ctk.CTkFrame(
            self, fg_color=mid_color, corner_radius=max(corner_radius - 2, 2)
        )
        self._mid.pack(fill="both", expand=True, padx=1, pady=1)

        # Bright inner ring: this is the crisp glowing edge right against the card.
        self._bright = ctk.CTkFrame(
            self._mid, fg_color=glow_color, corner_radius=max(corner_radius - 3, 2)
        )
        self._bright.pack(fill="both", expand=True, padx=1, pady=1)

        # The actual card surface content sits on top of all glow layers.
        self.inner = ctk.CTkFrame(
            self._bright,
            fg_color=fg_color,
            corner_radius=max(corner_radius - 4, 2) if corner_radius > 4 else corner_radius,
        )
        self.inner.pack(fill="both", expand=True, padx=border_width, pady=border_width)

        # Glossy "sheen" highlight: a slim, lighter strip near the very top
        # of the card interior, like light catching the top edge of glass.
        if sheen:
            sheen_bar = ctk.CTkFrame(
                self.inner,
                fg_color=blend(fg_color, "#ffffff", 0.06),
                height=2,
                corner_radius=max(corner_radius - 6, 1),
            )
            sheen_bar.pack(fill="x", side="top", padx=14, pady=(6, 0))


class GlowButton(ctk.CTkButton):
    """
    A button styled to look like it glows electric blue, with a brighter
    hover state and a thin bright top border to fake a glossy highlight,
    simulating a lighting effect that catches the top edge of the button.
    """

    def __init__(self, parent, text, command=None, fg_color=COLOR_GLOW,
                 hover_color=COLOR_GLOW_CYAN, text_color="#02070f",
                 font=None, height=48, corner_radius=16, glow=True, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            font=font or make_font(15, "bold"),
            height=height,
            corner_radius=corner_radius,
            border_width=0,
            **kwargs,
        )
        self._base_fg = fg_color
        self._glow_on = glow
        self._pulse_job = None
        self._pulse_t = 0.0
        self._pulse_dir = 1

    def start_pulse(self, low_color=None, high_color=None, step=0.06, delay_ms=45):
        """
        Start a lightweight 'breathing' glow animation on this button by
        smoothly cycling its fill color between a dim and a bright tone.
        Used sparingly on primary call-to-action buttons only, so the UI
        stays calm and the animation reads as a subtle premium detail
        rather than a distraction.
        """
        if self._pulse_job is not None:
            return  # Already pulsing.
        low_color = low_color or blend(self._base_fg, COLOR_BG, 0.35)
        high_color = high_color or blend(self._base_fg, "#ffffff", 0.25)

        def _tick():
            self._pulse_t += self._pulse_dir * step
            if self._pulse_t >= 1.0:
                self._pulse_t = 1.0
                self._pulse_dir = -1
            elif self._pulse_t <= 0.0:
                self._pulse_t = 0.0
                self._pulse_dir = 1
            try:
                self.configure(fg_color=blend(low_color, high_color, self._pulse_t))
            except Exception:
                return  # Widget was destroyed mid-animation; stop quietly.
            self._pulse_job = self.after(delay_ms, _tick)

        _tick()

    def stop_pulse(self):
        if self._pulse_job is not None:
            try:
                self.after_cancel(self._pulse_job)
            except Exception:
                pass
            self._pulse_job = None
            try:
                self.configure(fg_color=self._base_fg)
            except Exception:
                pass


class GhostButton(ctk.CTkButton):
    """A secondary, outlined button used for less prominent actions."""

    def __init__(self, parent, text, command=None, font=None, height=44,
                 corner_radius=16, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            fg_color="transparent",
            hover_color=COLOR_CARD_RAISED,
            text_color=COLOR_ACCENT_LIGHT,
            border_width=2,
            border_color=COLOR_BORDER,
            font=font or make_font(14, "bold"),
            height=height,
            corner_radius=corner_radius,
            **kwargs,
        )


class StatChip(GlowCard):
    """A small statistic card used on the Home dashboard (e.g. Total Questions)."""

    def __init__(self, parent, value, label, glow_color=COLOR_GLOW, **kwargs):
        super().__init__(parent, glow_color=glow_color, border_width=1, corner_radius=16, **kwargs)
        value_lbl = ctk.CTkLabel(
            self.inner, text=str(value), font=make_font(30, "bold"), text_color=COLOR_ACCENT_LIGHT
        )
        value_lbl.pack(pady=(18, 0))
        label_lbl = ctk.CTkLabel(
            self.inner, text=label.upper(), font=make_font(11, "bold"), text_color=COLOR_TEXT_DIM
        )
        label_lbl.pack(pady=(4, 16))


class GlowProgressBar(ctk.CTkFrame):
    """
    A progress bar with a soft two-step glow halo behind it and a
    gradient-look fill (blue fading into cyan) for a shinier, more
    dynamic appearance than a single flat color bar.
    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        outer = ctk.CTkFrame(self, fg_color=blend(COLOR_BG, COLOR_GLOW, 0.3), corner_radius=12)
        outer.pack(fill="x", padx=0, pady=0)
        self.glow_frame = ctk.CTkFrame(outer, fg_color=COLOR_GLOW_SOFT, corner_radius=10)
        self.glow_frame.pack(fill="x", padx=2, pady=2)
        self.bar = ctk.CTkProgressBar(
            self.glow_frame,
            height=16,
            corner_radius=8,
            progress_color=COLOR_GLOW_CYAN,
            fg_color=COLOR_CARD_ALT,
        )
        self.bar.pack(fill="x", padx=2, pady=2)
        self.bar.set(0)

    def set(self, value):
        """value should be a float between 0 and 1."""
        self.bar.set(value)


class GlowTitle(tk.Canvas):
    """
    Renders text with a genuine soft "bloom" glow behind it, built by
    stamping the same text several times in a dim glow color at small
    radial offsets (faking a blur), then drawing the crisp text on top.
    This is the technique used for the big "QUIZ MASTER BOT" headline so
    it visually pops like a neon/glass sign rather than flat text.

    Uses plain tkinter's Canvas (CustomTkinter has no canvas widget), so
    the background color is set to match the app's background exactly.
    """

    def __init__(self, parent, text, font_size=44, font_weight="bold", text_color=COLOR_TEXT,
                 glow_color=COLOR_GLOW, width=760, height=70, layers=10, radius=3,
                 bg=COLOR_BG, **kwargs):
        super().__init__(parent, width=width, height=height, bg=bg,
                          highlightthickness=0, **kwargs)
        # Use a plain tkinter font tuple (not a CTkFont) since this is a
        # regular tkinter Canvas, not a CustomTkinter widget.
        font = (FONT_FAMILY, font_size, font_weight)
        cx, cy = width // 2, height // 2

        # Soft bloom: many faint offset copies fanning outward, dimmer as
        # they go further out, approximating a gaussian blur glow.
        import math
        for ring in range(layers, 0, -1):
            r = radius * (ring / layers) * 2.2
            dim = blend(COLOR_BG, glow_color, 0.10 + 0.05 * (layers - ring))
            steps = 10
            for i in range(steps):
                angle = (2 * math.pi / steps) * i
                dx = math.cos(angle) * r
                dy = math.sin(angle) * r
                self.create_text(
                    cx + dx, cy + dy, text=text, font=font, fill=dim, anchor="center"
                )

        # A tighter, brighter halo right around the letters.
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            self.create_text(
                cx + dx, cy + dy, text=text, font=font,
                fill=blend(COLOR_BG, glow_color, 0.55), anchor="center"
            )

        # Crisp foreground text on top of the glow.
        self.create_text(cx, cy, text=text, font=font, fill=text_color, anchor="center")


# ============================================================
# MAIN APPLICATION
# ============================================================

class QuizApp(ctk.CTk):
    """
    Main application window. Manages navigation between screens using a
    single window with swappable frames, and coordinates the question,
    score, and leaderboard managers.
    """

    def __init__(self):
        super().__init__()

        self.title("Quiz Master Bot")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(1000, 650)
        self.configure(fg_color=COLOR_BG)

        # ---- Backend managers (unchanged core logic) ----
        self.question_manager = QuestionManager()
        self.score_manager = ScoreManager("scores.json")
        self.leaderboard_manager = LeaderboardManager(self.score_manager)

        # ---- Session state for the quiz currently in progress ----
        self.player_name = ""
        self.selected_category = "All Categories"
        self.selected_difficulty = "All"
        self.selected_num_questions = 10
        self.current_questions = []
        self.current_index = 0
        self.score = 0
        self.correct_count = 0
        self.wrong_count = 0
        self.answer_locked = False
        self.answer_buttons = []

        # ---- Container that holds whichever screen is currently visible ----
        self.container = ctk.CTkFrame(self, fg_color=COLOR_BG)
        self.container.pack(fill="both", expand=True)

        self.current_frame = None
        self.show_home_screen()

    # --------------------------------------------------------
    # Screen navigation helper
    # --------------------------------------------------------
    def _switch_to(self, frame_builder):
        """Destroy the current screen and build a new one in its place."""
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = ctk.CTkFrame(self.container, fg_color=COLOR_BG)
        self.current_frame.pack(fill="both", expand=True)
        frame_builder(self.current_frame)

    # --------------------------------------------------------
    # Shared header used across screens
    # --------------------------------------------------------
    def _build_topbar(self, parent, title, subtitle=None, show_back=True):
        topbar = ctk.CTkFrame(parent, fg_color="transparent")
        topbar.pack(fill="x", padx=40, pady=(30, 10))

        left = ctk.CTkFrame(topbar, fg_color="transparent")
        left.pack(side="left", fill="x", expand=True)

        title_lbl = ctk.CTkLabel(
            left, text=title, font=make_font(26, "bold"), text_color=COLOR_TEXT
        )
        title_lbl.pack(anchor="w")

        if subtitle:
            sub_lbl = ctk.CTkLabel(
                left, text=subtitle, font=make_font(13), text_color=COLOR_TEXT_DIM
            )
            sub_lbl.pack(anchor="w", pady=(2, 0))

        if show_back:
            back_btn = GhostButton(topbar, "⟵ Home", command=self.show_home_screen, height=38)
            back_btn.pack(side="right")

        return topbar

    # ==========================================================
    # HOME SCREEN
    # ==========================================================
    def show_home_screen(self):
        self._switch_to(self._build_home_screen)

    def _build_home_screen(self, parent):
        # Center column
        wrapper = ctk.CTkFrame(parent, fg_color="transparent")
        wrapper.pack(expand=True, fill="both")

        header = ctk.CTkFrame(wrapper, fg_color="transparent")
        header.pack(pady=(46, 10))

        # Glowing "neon sign" style title with a real bloom effect behind
        # the letters, instead of flat colored text.
        title_canvas = GlowTitle(
            header, text="QUIZ MASTER BOT", font_size=46, font_weight="bold",
            text_color=COLOR_TEXT, glow_color=COLOR_GLOW, width=820, height=76,
        )
        title_canvas.pack()

        subtitle_lbl = ctk.CTkLabel(
            header,
            text="✦  Test Your Knowledge.  Improve Your Skills.  ✦",
            font=make_font(15),
            text_color=COLOR_ACCENT_LIGHT2,
        )
        subtitle_lbl.pack(pady=(4, 0))

        # ---- Navigation buttons ----
        btn_frame = ctk.CTkFrame(wrapper, fg_color="transparent")
        btn_frame.pack(pady=30)

        buttons = [
            ("Start Quiz", self.show_setup_screen),
            ("Leaderboard", self.show_leaderboard_screen),
            ("Categories", self.show_categories_screen),
            ("How to Play", self.show_how_to_play_screen),
            ("Exit", self._confirm_exit),
        ]

        for i, (label, cmd) in enumerate(buttons):
            is_primary = (label == "Start Quiz")
            btn_cls = GlowButton if is_primary else GhostButton
            btn = btn_cls(btn_frame, label, command=cmd, height=52)
            btn.configure(width=220, font=make_font(15, "bold"))
            btn.grid(row=i // 3, column=i % 3, padx=12, pady=12)
            if is_primary:
                # A slow, subtle breathing glow draws the eye to the main
                # call-to-action without being distracting.
                btn.start_pulse(delay_ms=55, step=0.045)

        # ---- Stats section ----
        stats_label = ctk.CTkLabel(
            wrapper, text="APPLICATION STATISTICS", font=make_font(13, "bold"),
            text_color=COLOR_TEXT_DIM,
        )
        stats_label.pack(pady=(30, 10))

        stats_frame = ctk.CTkFrame(wrapper, fg_color="transparent")
        stats_frame.pack(pady=(0, 30))

        total_q = self.question_manager.total_questions()
        total_cats = len(self.question_manager.get_categories())
        total_diffs = len(self.question_manager.get_difficulties())
        total_players = self.leaderboard_manager.player_count()

        stat_data = [
            (total_q, "Total Questions"),
            (total_cats, "Categories"),
            (total_diffs, "Difficulty Levels"),
            (total_players, "Players"),
        ]

        for i, (value, label) in enumerate(stat_data):
            chip = StatChip(stats_frame, value, label)
            chip.grid(row=0, column=i, padx=10)
            chip.configure(width=160, height=110)
            chip.inner.pack_propagate(False)

        footer = ctk.CTkLabel(
            wrapper,
            text="A student project polished for a professional portfolio.",
            font=make_font(11),
            text_color=COLOR_TEXT_DIM,
        )
        footer.pack(side="bottom", pady=20)

    def _confirm_exit(self):
        if messagebox.askyesno("Exit Quiz Master Bot", "Are you sure you want to exit?"):
            self.destroy()

    # ==========================================================
    # PLAYER SETUP SCREEN
    # ==========================================================
    def show_setup_screen(self):
        self._switch_to(self._build_setup_screen)

    def _build_setup_screen(self, parent):
        self._build_topbar(parent, "Player Setup", "Configure your quiz before you begin")

        card = GlowCard(parent, border_width=1)
        card.pack(padx=60, pady=10, fill="x")
        inner = card.inner
        inner.grid_columnconfigure((0, 1), weight=1)

        pad = {"padx": 30, "pady": (18, 6)}

        # ---- Player name ----
        name_lbl = ctk.CTkLabel(inner, text="PLAYER NAME", font=make_font(12, "bold"), text_color=COLOR_TEXT_DIM)
        name_lbl.grid(row=0, column=0, columnspan=2, sticky="w", **pad)

        self.name_entry = ctk.CTkEntry(
            inner, placeholder_text="Enter your name...", height=44, font=make_font(14),
            fg_color=COLOR_CARD_ALT, border_color=COLOR_BORDER, border_width=1,
        )
        self.name_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=30, pady=(0, 10))
        if self.player_name:
            self.name_entry.insert(0, self.player_name)

        # ---- Category ----
        cat_lbl = ctk.CTkLabel(inner, text="CATEGORY", font=make_font(12, "bold"), text_color=COLOR_TEXT_DIM)
        cat_lbl.grid(row=2, column=0, sticky="w", **pad)

        categories = ["All Categories"] + self.question_manager.get_categories()
        self.category_var = ctk.StringVar(value=self.selected_category)
        cat_menu = ctk.CTkOptionMenu(
            inner, values=categories, variable=self.category_var,
            fg_color=COLOR_CARD_ALT, button_color=COLOR_GLOW_SOFT, button_hover_color=COLOR_GLOW,
            height=42, font=make_font(13),
        )
        cat_menu.grid(row=3, column=0, sticky="ew", padx=(30, 15), pady=(0, 10))

        # ---- Difficulty ----
        diff_lbl = ctk.CTkLabel(inner, text="DIFFICULTY", font=make_font(12, "bold"), text_color=COLOR_TEXT_DIM)
        diff_lbl.grid(row=2, column=1, sticky="w", **pad)

        difficulties = ["All"] + self.question_manager.get_difficulties()
        self.difficulty_var = ctk.StringVar(value=self.selected_difficulty)
        diff_menu = ctk.CTkOptionMenu(
            inner, values=difficulties, variable=self.difficulty_var,
            fg_color=COLOR_CARD_ALT, button_color=COLOR_GLOW_SOFT, button_hover_color=COLOR_GLOW,
            height=42, font=make_font(13),
        )
        diff_menu.grid(row=3, column=1, sticky="ew", padx=(15, 30), pady=(0, 10))

        # ---- Number of questions ----
        num_lbl = ctk.CTkLabel(inner, text="NUMBER OF QUESTIONS", font=make_font(12, "bold"), text_color=COLOR_TEXT_DIM)
        num_lbl.grid(row=4, column=0, columnspan=2, sticky="w", **pad)

        self.num_questions_var = ctk.StringVar(value=str(self.selected_num_questions))
        num_options_frame = ctk.CTkFrame(inner, fg_color="transparent")
        num_options_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=30, pady=(0, 20))

        for i, option in enumerate(["5", "10", "15", "All Available"]):
            rb = ctk.CTkRadioButton(
                num_options_frame, text=option, variable=self.num_questions_var, value=option,
                fg_color=COLOR_GLOW, hover_color=COLOR_ACCENT_LIGHT, font=make_font(13),
                text_color=COLOR_TEXT,
            )
            rb.grid(row=0, column=i, padx=15, sticky="w")

        # ---- Start button ----
        start_btn = GlowButton(parent, "START QUIZ", command=self._on_start_quiz, height=56)
        start_btn.configure(font=make_font(17, "bold"))
        start_btn.pack(pady=25, padx=60, fill="x")
        start_btn.start_pulse(delay_ms=55, step=0.045)

    def _on_start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Player Name Required", "Please enter your name before starting the quiz.")
            return

        self.player_name = name
        self.selected_category = self.category_var.get()
        self.selected_difficulty = self.difficulty_var.get()
        num_value = self.num_questions_var.get()
        self.selected_num_questions = num_value if num_value == "All Available" else int(num_value)

        questions = self.question_manager.get_filtered_questions(
            category=self.selected_category,
            difficulty=self.selected_difficulty,
            num_questions=self.selected_num_questions,
        )

        if not questions:
            messagebox.showerror(
                "No Questions Available",
                "No questions match the selected category and difficulty.\n"
                "Please try a different combination.",
            )
            return

        self.current_questions = questions
        self.current_index = 0
        self.score = 0
        self.correct_count = 0
        self.wrong_count = 0

        self.show_quiz_screen()

    # ==========================================================
    # CATEGORIES SCREEN
    # ==========================================================
    def show_categories_screen(self):
        self._switch_to(self._build_categories_screen)

    def _build_categories_screen(self, parent):
        self._build_topbar(parent, "Categories", "Browse available topics and difficulty levels")

        wrapper = ctk.CTkFrame(parent, fg_color="transparent")
        wrapper.pack(fill="both", expand=True, padx=60)

        for category in self.question_manager.get_categories():
            count = len(
                self.question_manager.get_filtered_questions(category, "All", "All Available")
            )
            card = GlowCard(wrapper, border_width=1)
            card.pack(fill="x", pady=8)
            row = ctk.CTkFrame(card.inner, fg_color="transparent")
            row.pack(fill="x", padx=24, pady=18)

            name_lbl = ctk.CTkLabel(row, text=category, font=make_font(18, "bold"), text_color=COLOR_ACCENT_LIGHT)
            name_lbl.pack(side="left")

            count_lbl = ctk.CTkLabel(
                row, text=f"{count} question{'s' if count != 1 else ''}",
                font=make_font(13), text_color=COLOR_TEXT_DIM,
            )
            count_lbl.pack(side="right")

    # ==========================================================
    # HOW TO PLAY SCREEN
    # ==========================================================
    def show_how_to_play_screen(self):
        self._switch_to(self._build_how_to_play_screen)

    def _build_how_to_play_screen(self, parent):
        self._build_topbar(parent, "How to Play", "Everything you need to know before you start")

        card = GlowCard(parent, border_width=1)
        card.pack(padx=60, pady=10, fill="both", expand=True)
        inner = card.inner

        steps = [
            "1. Enter your name on the Player Setup screen.",
            "2. Select a category, or choose All Categories.",
            "3. Select a difficulty level, or choose All.",
            "4. Choose how many questions you want to answer.",
            "5. Answer each multiple-choice question by clicking an option.",
            "6. Review your score, correct/wrong count, and percentage.",
            "7. Check the Leaderboard to see how you rank against others.",
        ]

        steps_frame = ctk.CTkFrame(inner, fg_color="transparent")
        steps_frame.pack(fill="x", padx=30, pady=(24, 10), anchor="w")
        for step in steps:
            lbl = ctk.CTkLabel(
                steps_frame, text=step, font=make_font(14), text_color=COLOR_TEXT, anchor="w", justify="left"
            )
            lbl.pack(fill="x", pady=6, anchor="w")

        divider = ctk.CTkFrame(inner, fg_color=COLOR_BORDER, height=2)
        divider.pack(fill="x", padx=30, pady=16)

        scoring_title = ctk.CTkLabel(
            inner, text="HOW SCORING WORKS", font=make_font(14, "bold"), text_color=COLOR_ACCENT_LIGHT
        )
        scoring_title.pack(anchor="w", padx=30)

        scoring_text = (
            "Each correct answer adds 1 point to your score. Your final percentage is "
            "calculated as (correct answers / total questions) x 100. The leaderboard ranks "
            "players by percentage first, and by raw score as a tiebreaker, so quizzes of "
            "different lengths remain fair to compare."
        )
        scoring_lbl = ctk.CTkLabel(
            inner, text=scoring_text, font=make_font(13), text_color=COLOR_TEXT_DIM,
            wraplength=900, justify="left", anchor="w",
        )
        scoring_lbl.pack(fill="x", padx=30, pady=(6, 24), anchor="w")

    # ==========================================================
    # QUIZ SCREEN
    # ==========================================================
    def show_quiz_screen(self):
        self._switch_to(self._build_quiz_screen)

    def _build_quiz_screen(self, parent):
        total = len(self.current_questions)
        question = self.current_questions[self.current_index]

        # ---- Info bar ----
        info_bar = ctk.CTkFrame(parent, fg_color="transparent")
        info_bar.pack(fill="x", padx=40, pady=(24, 6))

        left_info = ctk.CTkLabel(
            info_bar,
            text=f"Player: {self.player_name}    |    Category: {question['category']}    |    Difficulty: {question['difficulty']}",
            font=make_font(13), text_color=COLOR_TEXT_DIM,
        )
        left_info.pack(side="left")

        score_lbl = ctk.CTkLabel(
            info_bar, text=f"Score: {self.score}", font=make_font(15, "bold"), text_color=COLOR_ACCENT_LIGHT
        )
        score_lbl.pack(side="right")

        # ---- Question counter + progress bar ----
        progress_frame = ctk.CTkFrame(parent, fg_color="transparent")
        progress_frame.pack(fill="x", padx=40, pady=(4, 10))

        counter_lbl = ctk.CTkLabel(
            progress_frame, text=f"Question {self.current_index + 1} of {total}",
            font=make_font(13, "bold"), text_color=COLOR_TEXT,
        )
        counter_lbl.pack(anchor="w")

        progress_bar = GlowProgressBar(progress_frame)
        progress_bar.pack(fill="x", pady=(6, 0))
        progress_bar.set((self.current_index) / total if total else 0)

        # ---- Question card ----
        card = GlowCard(parent, border_width=2)
        card.pack(padx=40, pady=16, fill="both", expand=True)
        inner = card.inner

        question_lbl = ctk.CTkLabel(
            inner, text=question["question"], font=make_font(22, "bold"), text_color=COLOR_TEXT,
            wraplength=1000, justify="center",
        )
        question_lbl.pack(pady=(40, 30), padx=40)

        # ---- Answer buttons ----
        self.answer_buttons = []
        self.answer_locked = False
        options_frame = ctk.CTkFrame(inner, fg_color="transparent")
        options_frame.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        options_frame.grid_columnconfigure((0, 1), weight=1)

        for i, option_text in enumerate(question["options"]):
            letter = chr(65 + i)  # A, B, C, D
            btn = ctk.CTkButton(
                options_frame,
                text=f"  {letter}     {option_text}",
                font=make_font(15, "bold"),
                fg_color=COLOR_CARD_RAISED,
                hover_color=blend(COLOR_CARD_RAISED, COLOR_GLOW, 0.35),
                text_color=COLOR_TEXT,
                border_width=1,
                border_color=COLOR_BORDER,
                corner_radius=14,
                height=64,
                anchor="w",
                command=lambda idx=i: self._on_answer_selected(idx),
            )
            btn.grid(row=i // 2, column=i % 2, padx=12, pady=10, sticky="ew")
            self.answer_buttons.append(btn)

        # ---- Feedback label (shown after answering) ----
        self.feedback_lbl = ctk.CTkLabel(inner, text="", font=make_font(16, "bold"))
        self.feedback_lbl.pack(pady=(0, 10))

        # ---- Next button (hidden until an answer is chosen) ----
        self.next_btn = GlowButton(
            parent, "NEXT QUESTION", command=self._on_next_question, height=50
        )
        self.next_btn.configure(state="disabled", fg_color=COLOR_CARD_ALT, text_color=COLOR_TEXT_DIM)
        self.next_btn.pack(padx=40, pady=(0, 24), fill="x")

    def _on_answer_selected(self, selected_index):
        if self.answer_locked:
            return  # Prevent selecting multiple answers for the same question.
        self.answer_locked = True

        question = self.current_questions[self.current_index]
        correct_index = question["answer"]
        is_correct = (selected_index == correct_index)

        if is_correct:
            self.score += 1
            self.correct_count += 1
            self.answer_buttons[selected_index].configure(
                fg_color=COLOR_SUCCESS, text_color="#04150a",
                border_width=2, border_color=blend(COLOR_SUCCESS, "#ffffff", 0.4),
            )
            self.feedback_lbl.configure(text="✓  Correct! Well done.", text_color=COLOR_SUCCESS)
        else:
            self.wrong_count += 1
            self.answer_buttons[selected_index].configure(
                fg_color=COLOR_ERROR, text_color="#1a0405",
                border_width=2, border_color=blend(COLOR_ERROR, "#ffffff", 0.4),
            )
            self.answer_buttons[correct_index].configure(
                fg_color=COLOR_SUCCESS, text_color="#04150a",
                border_width=2, border_color=blend(COLOR_SUCCESS, "#ffffff", 0.4),
            )
            correct_text = question["options"][correct_index]
            self.feedback_lbl.configure(
                text=f"✕  Incorrect. Correct answer: {correct_text}", text_color=COLOR_ERROR
            )

        # Disable all answer buttons once one has been chosen.
        for btn in self.answer_buttons:
            btn.configure(state="disabled")

        self.next_btn.configure(state="normal", fg_color=COLOR_GLOW, text_color="#02070f")

    def _on_next_question(self):
        self.current_index += 1
        if self.current_index >= len(self.current_questions):
            self._finish_quiz()
        else:
            self.show_quiz_screen()

    def _finish_quiz(self):
        total = len(self.current_questions)
        percentage = (self.correct_count / total) * 100 if total else 0

        self.score_manager.save_score(
            player_name=self.player_name,
            score=self.correct_count,
            total=total,
            percentage=percentage,
            category=self.selected_category,
            difficulty=self.selected_difficulty,
        )

        self.show_results_screen()

    # ==========================================================
    # RESULTS SCREEN
    # ==========================================================
    def show_results_screen(self):
        self._switch_to(self._build_results_screen)

    @staticmethod
    def _performance_message(percentage):
        """Return (title, subtitle, color) feedback based on percentage."""
        if percentage >= 90:
            return "Outstanding Performance!", "You have demonstrated excellent knowledge.", COLOR_GOLD
        elif percentage >= 80:
            return "Excellent Work!", "You performed very well.", COLOR_SUCCESS
        elif percentage >= 60:
            return "Good Job!", "Keep practicing to improve even further.", COLOR_ACCENT_LIGHT
        elif percentage >= 40:
            return "Good Attempt!", "You are making progress. Keep practicing.", COLOR_GLOW
        else:
            return "Keep Learning!", "Do not give up. Every attempt helps you improve.", COLOR_ERROR

    def _build_results_screen(self, parent):
        total = len(self.current_questions)
        percentage = (self.correct_count / total) * 100 if total else 0
        title, subtitle, color = self._performance_message(percentage)

        wrapper = ctk.CTkFrame(parent, fg_color="transparent")
        wrapper.pack(expand=True, fill="both")

        heading = ctk.CTkLabel(wrapper, text="QUIZ COMPLETE", font=make_font(30, "bold"), text_color=COLOR_TEXT)
        heading.pack(pady=(40, 4))

        name_lbl = ctk.CTkLabel(wrapper, text=self.player_name, font=make_font(18), text_color=COLOR_TEXT_DIM)
        name_lbl.pack(pady=(0, 20))

        # ---- Score summary card ----
        card = GlowCard(wrapper, border_width=2, glow_color=color)
        card.pack(padx=200, pady=10, fill="x")
        inner = card.inner

        score_row = ctk.CTkFrame(inner, fg_color="transparent")
        score_row.pack(pady=(28, 10))

        big_score = ctk.CTkLabel(
            score_row, text=f"{self.correct_count} / {total}", font=make_font(46, "bold"), text_color=color
        )
        big_score.pack()

        score_caption = ctk.CTkLabel(score_row, text="FINAL SCORE", font=make_font(12, "bold"), text_color=COLOR_TEXT_DIM)
        score_caption.pack()

        stats_row = ctk.CTkFrame(inner, fg_color="transparent")
        stats_row.pack(pady=16)

        stats = [
            ("Correct", self.correct_count, COLOR_SUCCESS),
            ("Wrong", self.wrong_count, COLOR_ERROR),
            ("Percentage", f"{percentage:.0f}%", COLOR_ACCENT_LIGHT),
        ]
        for i, (label, value, stat_color) in enumerate(stats):
            box = ctk.CTkFrame(stats_row, fg_color=COLOR_CARD_ALT, corner_radius=12)
            box.grid(row=0, column=i, padx=10)
            v_lbl = ctk.CTkLabel(box, text=str(value), font=make_font(22, "bold"), text_color=stat_color)
            v_lbl.pack(padx=24, pady=(12, 0))
            l_lbl = ctk.CTkLabel(box, text=label, font=make_font(11), text_color=COLOR_TEXT_DIM)
            l_lbl.pack(padx=24, pady=(0, 12))

        title_lbl = ctk.CTkLabel(inner, text=title, font=make_font(22, "bold"), text_color=color)
        title_lbl.pack(pady=(20, 2))

        subtitle_lbl = ctk.CTkLabel(inner, text=subtitle, font=make_font(13), text_color=COLOR_TEXT_DIM)
        subtitle_lbl.pack(pady=(0, 28))

        # ---- Action buttons ----
        btn_row = ctk.CTkFrame(wrapper, fg_color="transparent")
        btn_row.pack(pady=30)

        view_btn = GlowButton(btn_row, "View Ranking", command=self.show_leaderboard_screen, height=48)
        view_btn.configure(width=180)
        view_btn.grid(row=0, column=0, padx=10)

        again_btn = GhostButton(btn_row, "Play Again", command=self.show_setup_screen, height=48)
        again_btn.configure(width=180)
        again_btn.grid(row=0, column=1, padx=10)

        home_btn = GhostButton(btn_row, "Home", command=self.show_home_screen, height=48)
        home_btn.configure(width=180)
        home_btn.grid(row=0, column=2, padx=10)

    # ==========================================================
    # LEADERBOARD SCREEN
    # ==========================================================
    def show_leaderboard_screen(self):
        self._switch_to(self._build_leaderboard_screen)

    def _build_leaderboard_screen(self, parent):
        self._build_topbar(parent, "QUIZ MASTER BOT — LEADERBOARD",
                            "Ranked by percentage first, then score, for fairness across quiz lengths")

        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=50, pady=(0, 20))

        ranked = self.leaderboard_manager.get_ranked_scores()

        if not ranked:
            empty_lbl = ctk.CTkLabel(
                scroll, text="No scores recorded yet. Play a quiz to appear on the leaderboard!",
                font=make_font(15), text_color=COLOR_TEXT_DIM,
            )
            empty_lbl.pack(pady=60)
            return

        # ---- Column headers ----
        header_row = ctk.CTkFrame(scroll, fg_color="transparent")
        header_row.pack(fill="x", pady=(0, 6))
        headers = ["Rank", "Player", "Score", "Percentage", "Category", "Difficulty"]
        weights = [1, 2, 1, 1, 2, 1]
        for i, (h, w) in enumerate(zip(headers, weights)):
            header_row.grid_columnconfigure(i, weight=w)
            lbl = ctk.CTkLabel(header_row, text=h.upper(), font=make_font(11, "bold"), text_color=COLOR_TEXT_DIM)
            lbl.grid(row=0, column=i, sticky="w", padx=10)

        rank_labels = {1: ("1st", COLOR_GOLD), 2: ("2nd", COLOR_SILVER), 3: ("3rd", COLOR_BRONZE)}

        for position, entry in enumerate(ranked, start=1):
            is_top_three = position in rank_labels
            rank_text, rank_color = rank_labels.get(position, (f"{position}th", COLOR_TEXT_DIM))

            row_card = GlowCard(
                scroll, border_width=2 if is_top_three else 1,
                glow_color=rank_color if is_top_three else COLOR_BORDER,
                corner_radius=12,
            )
            row_card.pack(fill="x", pady=5)
            row = ctk.CTkFrame(row_card.inner, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=10)
            for i, w in enumerate(weights):
                row.grid_columnconfigure(i, weight=w)

            rank_lbl = ctk.CTkLabel(row, text=rank_text, font=make_font(14, "bold"), text_color=rank_color)
            rank_lbl.grid(row=0, column=0, sticky="w", padx=10)

            player_lbl = ctk.CTkLabel(row, text=entry.get("player", "-"), font=make_font(14), text_color=COLOR_TEXT)
            player_lbl.grid(row=0, column=1, sticky="w", padx=10)

            score_text = f"{entry.get('score', 0)}/{entry.get('total', 0)}"
            score_lbl = ctk.CTkLabel(row, text=score_text, font=make_font(14), text_color=COLOR_TEXT)
            score_lbl.grid(row=0, column=2, sticky="w", padx=10)

            pct_lbl = ctk.CTkLabel(
                row, text=f"{entry.get('percentage', 0):.0f}%", font=make_font(14, "bold"), text_color=COLOR_ACCENT_LIGHT
            )
            pct_lbl.grid(row=0, column=3, sticky="w", padx=10)

            cat_lbl = ctk.CTkLabel(row, text=entry.get("category", "-"), font=make_font(14), text_color=COLOR_TEXT_DIM)
            cat_lbl.grid(row=0, column=4, sticky="w", padx=10)

            diff_lbl = ctk.CTkLabel(row, text=entry.get("difficulty", "-"), font=make_font(14), text_color=COLOR_TEXT_DIM)
            diff_lbl.grid(row=0, column=5, sticky="w", padx=10)


# ============================================================
# ENTRY POINT
# ============================================================

def main():
    app = QuizApp()
    app.mainloop()


if __name__ == "__main__":
    main()