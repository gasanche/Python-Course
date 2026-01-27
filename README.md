# Python Learning Projects

**Purpose**

This repository collects my everyday Python projects while I develop my Python skills🖥️. It’s intended both as a personal learning record and as a beginner-friendly resource for people who want to start learning Python😊.

---

## What you will find here

* Short, focused projects and exercises completed during practice sessions.
* Clear, commented code suitable for beginners.
* Guided weekly plans and small assignments to build core Python skills.
* Links (where relevant) to external practice platforms (HackerRank, Codewars) and setup tips.

---

## Who is this for?

* Absolute beginners who want a practical, hands-on way to start learning Python.
* Learners who prefer a weekly, step-by-step plan rather than a long theoretical course.
* Anyone looking for small exercises to practice syntax, data structures, and basic algorithms.

---

## Weekly learning roadmap (3 weeks)

This repository follows a compact 3-week learning roadmap designed to cover the essentials: syntax, data structures, modularity, and defensive programming.

### Week 1 — Syntax and Basic Logic

**Goal:** Get comfortable with the terminal and understand how Python stores information.

* **Day 1 — Hello World & environment**

  * Theory: What an interpreter is, variables and assignment, `print()`.
  * Practice: Configure VS Code, write a script that asks for your name (`input()`) and greets you. Practice basic arithmetic (`+`, `-`, `*`, `/`, `//`, `%`).

* **Day 2 — Primitive data types**

  * Theory: `str`, `int`, `float`, `bool`.
  * Practice: Convert between types with `str()` and `int()`. Intentionally produce a type error (e.g., add a string and a number) and read the traceback.

* **Day 3 — String manipulation**

  * Theory: Indexing `text[0]`, slicing `text[1:4]`, `.upper()`, `.lower()`, `.strip()`, `.replace()`, f-strings `f"Hello {name}"`.
  * Practice: Build a script that cleans a messy string (example: `" DaTa ScIeNcE "` → `"Data Science"`).

* **Day 4 — Boolean logic and comparators**

  * Theory: `==`, `!=`, `>`, `<`, `and`, `or`, `not`.
  * Practice: Write logical expressions on paper and test them in code (e.g., `(5 > 3) and (2 < 1)` → `False`).

* **Day 5 — Control flow (conditionals)**

  * Theory: `if`, `elif`, `else` and the importance of indentation in Python.
  * Practice: Create an IMC/BMI calculator that classifies weight category using `if/else`.

* **Day 6 — Intensive practice (HackerRank)**

  * Task: Sign up on HackerRank (Python track) and solve 3 problems from the "Introduction" section.

* **Day 7 — Review & basic Git**

  * Theory: What a repository is, `git init`, `git add`, `git commit`.
  * Practice: Initialize a local repo for your exercises and make your first commit.

### Week 2 — Data Structures (Containers)

**Goal:** Store and manage collections of data—fundamental for data work.

* **Day 8 — Lists (part 1)**

  * Theory: Create lists, indexing, `append()`, `remove()`, `pop()`.
  * Practice: Build a shopping list script that adds and removes items.

* **Day 9 — Lists (part 2)**

  * Theory: Advanced slicing, `sort()`, `reverse()`, `len()`, `in` operator.
  * Practice: Sort an unsorted list of numbers and compute the average manually.

* **Day 10 — For loops**

  * Theory: `for item in list`, using `range()`.
  * Practice: Print each shopping item in uppercase; print even numbers from 1 to 100.

* **Day 11 — Tuples and Sets**

  * Theory: Difference between mutable lists and immutable tuples; sets for unique values.
  * Practice: Clean duplicates from `[1, 2, 2, 3, 4, 4]` using `set()`.

* **Day 12 — Dictionaries**

  * Theory: Key:value mapping, `.keys()`, `.values()`.
  * Practice: Model a person with a dictionary (name, age, city), update the city and add profession.

* **Day 13 — Combining structures**

  * Theory: Lists of dictionaries (similar to JSON or a pandas DataFrame).
  * Practice: Create a student database (list of dicts) and print names of passing students.

* **Day 14 — Practice on Codewars**

  * Task: Solve three `8kyu` (beginner) problems focused on lists and strings.

### Week 3 — Modularity and More Complex Logic

**Goal:** Move beyond linear scripts and produce reusable, safe code.

* **Day 15 — While loops**

  * Theory: `while condition:`; avoid infinite loops; `break`, `continue`.
  * Practice: Build a number-guessing game that runs until the player guesses correctly.

* **Day 16 — Functions (part 1)**

  * Theory: `def function():`, parameters and arguments, DRY principle.
  * Practice: Turn the BMI calculator into `calculate_bmi(weight, height)`.

* **Day 17 — Functions (part 2)**

  * Theory: `return` vs `print`, local vs global scope.
  * Practice: Implement pure math functions that return values for reuse.

* **Day 18 — List comprehensions**

  * Theory: Pythonic syntax `[x for x in list]`.
  * Practice: Given a list of prices, create a new list with VAT applied in one line.

* **Day 19 — Error handling**

  * Theory: `try`, `except` to prevent crashes.
  * Practice: Improve the calculator so non-numeric input triggers a user-friendly message.

* **Day 20 — Modules & standard library**

  * Theory: `import math`, `import random`, `import datetime`.
  * Practice: Script that calculates how many days remain until your birthday using `datetime`.

* **Day 21 — Algorithm practice**

  * Task: Solve `FizzBuzz` and other beginner algorithm problems on Codewars or HackerRank.

---

## Project structure (suggested)

```
├─ week1/
│  ├─ day1_hello_world/
│  ├─ day2_types/
│  └─ ...
├─ week2/
└─ week3/
```

Each folder should include a `README.md` with instructions and one or more `.py` scripts with examples and comments.

---

## Contributing

Contributions are welcome. If you want to suggest improvements, open an issue or a pull request. Keep changes focused, add tests or example usage when possible, and document new exercises clearly.

---

## License

This repository is available under the MIT License. See the `LICENSE` file for details.

---

## Contact

If you want to give feedback or collaborate, open an issue or contact me at `gsanchezespinoza0112@gmail.com`.

Good luck and enjoy learning Python! 🚀
