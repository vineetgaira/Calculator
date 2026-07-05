# 🧮 CLI Calculator

A simple, colorful command-line calculator built with Python and `colorama`. Supports addition, subtraction, multiplication, and division — with input validation and friendly error handling.

> 📚 **Note:** This is a practice/learning project built to strengthen fundamentals in Python — loops, functions, exception handling, and basic CLI UX with `colorama`. Not intended for production use.

---

```
   ┌────────────────────────────────┐
   │        CLI CALCULATOR         │
   ├────────────────────────────────┤
   │  1 : ADD                      │
   │  2 : SUB                      │
   │  3 : MULTIPLY                 │
   │  4 : DIVIDE                   │
   │  5 : EXIT                     │
   └────────────────────────────────┘
        Enter your choice: _
```

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Addition** | Add any number of values, separated by spaces |
| ➖ **Subtraction** | Subtract one number from another |
| ✖️ **Multiplication** | Multiply any number of values, separated by spaces |
| ➗ **Division** | Divide two numbers, with divide-by-zero protection |
| 🎨 **Colored Output** | Uses `colorama` to color prompts, errors, and results |
| 🛡️ **Input Validation** | Handles invalid input gracefully with retry loops |
| 🔁 **Menu Loop** | Returns to the main menu after every operation until exit |

---

## 🗂️ Project Structure

```
cli-calculator/
│
├── main.py     # Main script (menu + operations)
└── README.md         # You are here
```

---

## ⚙️ Requirements

- Python 3.x
- `colorama` package

Install the dependency:

```bash
pip install colorama
```

---

## ▶️ How to Run

```bash
python main.py
```

You'll be greeted with a menu. Enter a number (1–5) to choose an operation, follow the prompts, and see your result printed in color.

---

## 🔍 Function Breakdown

### `user_menu()`
Displays the main menu with all available operations in green text.

### `user_input()`
Prompts the user for a menu choice (1–5). Loops until a valid integer within the valid choice set is entered — catches non-numeric input via `ValueError`.

### `addition()`
Accepts multiple space-separated numbers, sums them using `sum()`, and prints the total. Re-prompts if input is empty or invalid.

### `subtraction()`
Takes two numbers and prints the result of `number1 - number2`, formatted to 5 decimal places.

### `multiplication()`
Accepts multiple space-separated numbers, multiplies them together using a running product, and prints the result.

### `division()`
Takes two numbers and prints `number1 / number2`, formatted to 5 decimal places. Catches `ZeroDivisionError` and `ValueError` separately for clear error messages.

### `calculator()`
The main driver loop — shows the menu, gets the user's choice, dispatches to the correct operation function, and exits cleanly when option 5 is chosen.

---

## 🎯 Learning Goals

This project was built to practice:

- [x] Writing modular functions for a CLI application
- [x] Using `while` loops for input validation and retries
- [x] Handling exceptions (`ValueError`, `ZeroDivisionError`)
- [x] Parsing space-separated user input into lists (`map()` + `split()`)
- [x] Using `colorama` for colored terminal output
- [x] Structuring a simple menu-driven program with `if`/`elif`
- [x] Using f-strings for formatted numeric output

---

## 🚀 Possible Improvements (Future Practice Ideas)

- [ ] Add support for more operations (modulus, exponentiation, square root)
- [ ] Add a calculation history log
- [ ] Refactor operations to reduce code duplication
- [ ] Add unit tests for each operation
- [ ] Support chained expressions (e.g. `2 + 3 * 4`)

---

## 📄 License

This project is for personal learning and practice purposes. Feel free to fork and experiment!
