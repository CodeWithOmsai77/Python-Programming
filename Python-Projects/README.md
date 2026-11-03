# 🐍 Python Mini Projects

<div align="center">

<img src="https://img.shields.io/badge/Python-Standard%20Library-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python standard library" />
<img src="https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-0F766E?style=for-the-badge" alt="Beginner to intermediate" />
<img src="https://img.shields.io/badge/Projects-9-6D28D9?style=for-the-badge" alt="Nine Python projects" />

**Small, runnable projects that build on the concepts in the chapter-wise learning folders.**

[⬅ Back to the main Python Learning README](../README.md)

</div>

---

## 🧩 Project Index

| # | Project | Main concepts | Data saved? |
|---:|---|---|---|
| 01 | [Calculator](Calc2.py) | Tkinter GUI, event handling, arithmetic | No |
| 02 | [Snake Water Gun Game](snake_water_gun.py) | Random choice, conditions, user input | No |
| 03 | [The Perfect Guess](the_perfect_guess.py) | Loops, comparisons, random numbers | No |
| 04 | [Student Marks Analyzer](student_marks_analyzer.py) | Lists, functions, averages, grade boundaries | No |
| 05 | [Expense Tracker](expense_tracker.py) | Dictionaries, loops, JSON file handling | Yes — `expenses.json` |
| 06 | [Contact Book](contact_book.py) | Dictionaries, search, update and delete | No — memory only |
| 07 | [Python Quiz Game](quiz_game.py) | Lists, dictionaries, loops and scoring | No |
| 08 | [Password Generator](password_generator.py) | Strings, modules, secure random selection | No |
| 09 | [Face Detector](Face_Detector.py) | OpenCV, webcam capture, Haar Cascade, image preprocessing, real-time face detection | No |

Projects 01–08 primarily use Python's standard library. The Calculator uses `tkinter`, which must be available in your Python installation. The Face Detector requires the third-party `opencv-python` package and a working webcam.

## 🚀 Run a Project

Run commands from the **repository root**.

### 04 · Student Marks Analyzer

```bash
python Python-Projects/student_marks_analyzer.py
```

Enter a name and marks for three subjects. The program validates the marks, prints the total and average, and assigns a grade.

### 05 · Expense Tracker

```bash
python Python-Projects/expense_tracker.py
```

Add expenses, list them, and view the total, average, and largest expense. Entries are saved in `Python-Projects/expenses.json` so they remain available the next time you run the program.

### 06 · Contact Book

```bash
python Python-Projects/contact_book.py
```

Add or update contacts, search by name, list saved-in-memory contacts, or delete a contact. Contacts are kept in memory and reset when the program exits.

### 07 · Python Quiz Game

```bash
python Python-Projects/quiz_game.py
```

Answer five multiple-choice questions and see your score at the end.

### 08 · Password Generator

```bash
python Python-Projects/password_generator.py
```

Choose a password length and whether to include digits and symbols. The program uses Python's `secrets` module for secure random selection.

### 09 · Face Detector

Install OpenCV:

```bash
python -m pip install opencv-python
```

Run the webcam-based face detector:

```bash
python Python-Projects/Face_Detector.py
```

The program uses OpenCV's pre-trained Haar Cascade classifier to detect faces in the webcam feed, draw bounding boxes, and display the number of detected faces. Press **Q** to exit. Allow camera access when prompted.

### Original projects

```bash
python Python-Projects/snake_water_gun.py
python Python-Projects/the_perfect_guess.py
python Python-Projects/Calc2.py
```

The last command opens a small GUI and requires `tkinter`; if Tkinter isn't installed with your Python distribution, that existing GUI project may need the corresponding OS package.

## ✅ Suggested Practice Order

Try **Student Marks Analyzer → Python Quiz Game → Contact Book → Password Generator → Expense Tracker → Face Detector**. This moves from lists and functions to dictionaries, modules, persistent file handling, and then practical computer vision with OpenCV.

Before considering a project complete:
1. Run it with valid input and at least one boundary or invalid input.
2. Read and explain every function.
3. Change one feature independently.
4. For the Expense Tracker, close and reopen the program to confirm that saved data loads.
5. For the Face Detector, test with different lighting conditions and face positions; Haar Cascade is a basic detector and may miss angled or partially covered faces.
6. Keep the lesson programs and independent projects as separate practice areas.

---

[⬅ Back to the full learning roadmap](../README.md)
