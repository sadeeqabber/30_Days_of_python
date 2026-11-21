#   30 Days of Python

My solutions to the [30 Days of Python](https://github.com/asabeneh/30-days-of-python) challenge by Asabeneh Yetayeh, worked through as part of the [Arewa Data Science Academy](https://arewadatascience.github.io) *Python Programming for Data Science* programme.

Each day has its own folder containing a Python script with my answers to that day's exercises, organised by level (Level 1, Level 2, Level 3) and numbered to match the exercise questions.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Progress](https://img.shields.io/badge/Progress-Day%2010%20of%2030-orange)

---

## 📚 Progress

| Day | Topic | Folder | Main file(s) |
|-----|-------|--------|--------------|
| 1 | Introduction, Python version, basic operations | [`Day_1`](Day_1) | `helloworld.py` |
| 2 | Variables and built-in functions | [`Day_2`](Day_2) | `variables.py` |
| 3 | Operators | [`Day_3`](Day_3) | `operators.py` |
| 4 | Strings | [`Day_4`](Day_4) | `Strings.py` |
| 5 | Lists, tuples and sets | [`Day_5`](Day_5) | `list_tuples_set.py`, `countries.py` |
| 6 | Dictionaries | [`Day_6`](Day_6) | `Dictionary.py` |
| 7 | Conditionals | [`Day_7`](Day_7) | `conditionals.py` |
| 8 | Loops | [`Day_8`](Day_8) | `Loops.py`, `countries_data.py` |
| 9 | Functions, list comprehensions and lambda | [`Day_9`](Day_9) | `functions.py`, `list_comprehensions.py`, `countries_data.py` |
| 10 | Higher-order functions (`map`, `filter`, `reduce`) | [`Day_10`](Day_10) | `Higher_order_function.py`, `countries_data.py` |
| 11–30 | Coming soon | — | — |

---

## 📁 Repository Structure

```
30_Days_of_python/
├── Day_1/    helloworld.py
├── Day_2/    variables.py
├── Day_3/    operators.py
├── Day_4/    Strings.py
├── Day_5/    countries.py, list_tuples_set.py
├── Day_6/    Dictionary.py
├── Day_7/    conditionals.py
├── Day_8/    Loops.py, countries_data.py
├── Day_9/    functions.py, list_comprehensions.py, countries_data.py
├── Day_10/   Higher_order_function.py, countries_data.py
├── LICENSE
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/sadeeqabber/30_Days_of_python.git
   cd 30_Days_of_python
   ```

3. Move into a day's folder and run its script from there:

   ```bash
   cd Day_8
   python Loops.py
   ```

### Things to know

- **Run each script from inside its own day folder.** Days 5, 8, 9 and 10 import data files (`countries.py` or `countries_data.py`) that sit next to the script, so they will not be found if you run from the repository root.
- **Some scripts ask for input.** `Day_2/variables.py`, `Day_3/operators.py` and `Day_7/conditionals.py` use `input()`, so the script will pause and wait for you to type a value.
- **Country data.** `countries_data.py` is the course's country dataset, saved as a Python list called `countries_data` so it can be imported.

---

## 🧠 What I Practised

- Printing, variables, data types and built-in functions
- Arithmetic, comparison and logical operators
- String methods and formatting
- Lists, tuples, sets and dictionaries
- `if` / `elif` / `else` decision making
- `for` and `while` loops
- Defining functions, default arguments and return values
- List comprehensions and `lambda`
- Higher-order functions: `map`, `filter` and `reduce`

---

## 🙏 Credits

- **Course:** [30 Days of Python](https://github.com/asabeneh/30-days-of-python) by [Asabeneh Yetayeh](https://github.com/asabeneh)
- **Programme:** [Arewa Data Science Academy](https://arewadatascience.github.io), *Python Programming for Data Science*

The exercises belong to the original course. The solutions in this repository are my own.

---

## 👤 Author

**Muhammad Abubakar Sadiq**
GitHub: [@sadeeqabber](https://github.com/sadeeqabber)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
