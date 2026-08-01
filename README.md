# 🐍 Python for Data Science: From Language Foundations to Data Engineering

> **42 / 1337 Training Piscine:** A five-module engineering path that starts with the raw Python language and ends with array computing, tabular analysis, object modeling and structural design patterns — every exercise solved to the letter of the subject, linted, documented and demonstrated.

---

## 🌟 Vision & Educational Philosophy (Masterclass)

This repository is not a dump of accepted answers. Each solution is written as a **teaching artifact**: the code that passes the evaluation, plus the reasoning that made it the right code.

- **The Subject Is The Specification:** every expected output in the PDF is treated as a contract and verified by actually running the program, not by reading it. Where the subject and personal taste disagree, the subject wins — and the deviation is documented in the file.
- **Never Crash:** from Exercise 05 onward the subject invalidates any program that lets an exception escape. Error paths are therefore designed, not patched: `AssertionError` for contract violations, guarded conversions, and stream reads that return empty instead of raising.
- **The Norm Is Not Optional:** all code is `flake8` clean at 79 columns, with explicit imports, no wildcard imports and no mutable global state.
- **Self-Documenting Code:** every file opens with an educational banner explaining the *why*, and every function carries a `__doc__` the way the subject demands.

---

## 🗺️ Curriculum & Modules

### 🧱 Module 00: Starting (Language Fundamentals) — ✅ complete
The raw language: containers, formatting, functions, argument handling, comprehensions, generators and packaging. Navigate into **Piscine Python for datascience - 0** to explore the course and the solutions.
- **Key Concepts Covered:** Mutable vs immutable containers, f-string format specifiers (`:,.4f`, `:.2e`), type introspection (`type()`, `isinstance()`), the `is` / `==` distinction and the NaN identity trick, `sys.argv` handling, `sys.stdin` vs `input()`, list comprehensions, `lambda` and closures, dictionaries as lookup tables, generators (`yield`) and terminal rendering, PyPI packaging with `pyproject.toml`.
- **Flagship Project:** A from-scratch reimplementation of the `filter` built-in, a terminal progress bar cloning `tqdm`, and `ft_package` — a real installable distribution built to both a source archive and a wheel.

### 🔢 Module 01: Array (NumPy & Images) — ✅ complete
Vectorized computation over arrays and pixel matrices. Navigate into **Piscine Python for datascience - 1**.
- **Key Concepts Covered:** NumPy arrays and the `(h, w, c)` layout, `.tolist()` and the NumPy 2 repr trap, 2D slicing as a view, luminance vs plain mean, `np.newaxis`, hand-written transposition, channel arithmetic under operator restrictions, `matplotlib` axes.
- **Flagship Project:** A 400×400 zoom on `animal.jpeg` reproducing the subject's own pixel values, a transpose written without a single library helper, and five colour filters each restricted to a different operator set.

### 📊 Module 02: DataTable (pandas & matplotlib) — ✅ complete
Loading, reshaping and plotting real Gapminder datasets. Navigate into **Piscine Python for datascience - 2**.
- **Key Concepts Covered:** `pandas` DataFrames, the UTF-8 BOM trap, wide format, parsing human-readable numbers (`3.28M`, `1.16B`, `1.05k`), boolean row masks, line vs scatter, logarithmic axes, tick formatters and mandatory legends.
- **Flagship Project:** Morocco's life expectancy through three centuries, a Morocco/France population comparison from 1800 to 2050, and the 1900 income-versus-longevity scatter that answers the subject's correlation question.

### 👑 Module 03: Oriented Object Programming (Game of Thrones) — ✅ complete
Object modeling, abstract bases and the diamond problem. Navigate into **Piscine Python for datascience - 3**.
- **Key Concepts Covered:** `ABC` and `@abstractmethod`, cooperative `super()`, `__str__` vs `__repr__` and what a bound method reveals, `@classmethod` as an alternative constructor, C3 linearization, properties as data descriptors, operator overloading and `@staticmethod`.
- **Flagship Project:** Joffrey Baratheon — a diamond-inheritance monster whose traits are governed by properties that store into `__dict__` to avoid infinite recursion.

### 🏗️ Module 04: Data Oriented Design — ✅ complete
Higher-order functions and declarative data modeling. Navigate into **Piscine Python for datascience - 4**.
- **Key Concepts Covered:** `*args` / `**kwargs`, dispatch tables of functions, statistics implemented with no library at all (interpolated quartiles, population variance), closures and `nonlocal`, three-level decorator factories, `@dataclass` with `field(init=False)`, `default_factory` and `__post_init__`.
- **Flagship Project:** A call-limiting decorator whose counters are per-decoration, and a `Student` data class whose login and identifier are computed yet impossible to pass to the constructor.

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10** — the version the subject mandates for evaluation.
- **flake8** as the norm checker: `pip install flake8` then `alias norminette=flake8`.

### Running & Verifying Exercises
Each exercise is run from inside its own turn-in directory:

```bash
# Example: a standalone program taking arguments
cd "Piscine Python for datascience - 0/ex05" && python building.py "Hello World!"

# Example: an import-only module driven by the subject's tester
cd "Piscine Python for datascience - 0/ex03" && python tester.py

# Norm check across a whole module
python -m flake8 "Piscine Python for datascience - 0"
```

---
*Built to be defended: every expected output in this repository was reproduced by execution before being committed.*
