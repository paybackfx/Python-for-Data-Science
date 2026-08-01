# 🧱 Starting: The Python Language Foundations (Module 00)

> **Course Summary:** Master the raw Python language before any data library enters the picture. Containers and their mutability, string formatting, type introspection, command line handling, comprehensions and lambdas, generators, and finally the packaging of your own installable distribution.

---

## 🎯 Educational Philosophy & Language Masterclass

This module is where the habits are formed. A data pipeline that mishandles `None`, silently miscounts a stream, or crashes on a malformed argument is worthless no matter how good the model on top of it is. Here is the reasoning behind every concept this module introduces.

### 1. Mutability: The Line Between `list`, `set`, `dict` and `tuple`
A `list`, a `set` and a `dict` can be modified **in place** — the object in memory changes and every name pointing to it sees the change. A `tuple` cannot: the only way to "modify" it is to build a new tuple and rebind the name. A set additionally stores its values by **hash rather than by position**, which is why the print order of a set is not guaranteed to match the insertion order.

### 2. Format Specifiers: The Grammar After the Colon
Inside an f-string, everything after the `:` is a rendering instruction, not data:
- **`{value:,.4f}`** — thousand separators, four decimals.
- **`{value:.2e}`** — scientific notation with two decimals.
- **`{text:<{width}}`** — left-align and pad to a width computed at runtime.
- **`strftime("%b %d %Y")`** — the same idea for dates: abbreviated month, zero-padded day, four-digit year.

### 3. Identity vs Equality — and the NaN Trick
`is` compares memory addresses, `==` compares values. `None` and `False` are unique singletons, so they must be caught with `is`; using `==` would also catch `0`, which is a different kind of emptiness. And because IEEE-754 declares every comparison involving `NaN` false — *including `NaN == NaN`* — the expression `object != object` is the cleanest NaN detector in the language, with no import at all.

> The ordering of the checks is itself a design decision: `False` must be tested **before** `0`, because `False == 0` is true in Python and the reverse order would mislabel `False` as a zero.

### 4. Import-Only Modules vs Standalone Programs
The subject makes this distinction explicit — "*Running your function alone does nothing*". A file is one of two things, never both:
- **An import-only module** (`find_ft_type.py`, `NULL_not_found.py`, `ft_filter.py`, `Loading.py`): it defines and stops. No shebang, no `if __name__` block, no output when executed directly.
- **A standalone program** (`whatis.py`, `building.py`, `filterstring.py`, `sos.py`): shebang on line 1, all logic inside `main()`, and `if __name__ == "__main__": main()` as the last block.

### 5. Reading the Command Line, and Reading the Stream
`sys.argv` is a list of **strings** where index `0` is the script name — a program called with one argument therefore sees a list of length 2. Reading standard input is a separate decision with a real consequence:
- **`input()`** strips the terminating newline.
- **`sys.stdin.read()`** keeps every byte until EOF, and returns `""` on ctrl+D instead of raising `EOFError`.

The subject counts the carriage return as a space, so only the raw stream produces the 13 characters it expects for `Hello World!`.

### 6. Comprehensions, Lambdas and Closures
A **list comprehension** builds a list in one pass with no accumulator and no `append()`. A **lambda** is a single-expression anonymous function used as a value — passed to another function at the call site. When that lambda reads a variable from the function enclosing it, it forms a **closure**: the variable is captured, not copied.

### 7. Generators: Functions That Pause
Any function containing `yield` returns a **generator**. Each `yield` hands one item to the caller and freezes the function until the next iteration resumes it. That suspension is precisely what makes a progress bar possible: the bar is redrawn *between* items, from inside the loop the caller thinks it controls.

### 8. Packaging: Turning Code Into a Distribution
`pyproject.toml` declares the build backend and the project metadata. `python -m build` reads it and produces two artifacts — a **source archive** (`.tar.gz`) and a **wheel** (`.whl`) — and `pip install` accepts either. The `__init__.py` of the package is its public face: re-exporting a symbol there is what turns `from ft_package.count_in_list import count_in_list` into `from ft_package import count_in_list`.

---

## 📚 General Engineering Standards

- All implementations target **Python 3.10**, the version the subject mandates for evaluation.
- Code formatting complies with **flake8** at 79 columns (`pip install flake8`, `alias norminette=flake8`). `python -m flake8 .` on this directory returns nothing.
- Imports are **explicit** — never `from x import *` — and there is no mutable global state. The only module-level names are the constants the subject asks for (`NESTED_MORSE`, `FALLBACK_WIDTH`).
- Every function carries a `__doc__`, and every file opens with an educational banner explaining the *why* before the *how*.
- From Exercise 05 onward every program has a `main()` and **must never crash**: error paths are designed, not patched.
- Every expected output listed below was reproduced by **running the code**, not by reading it.

> ⚠️ **Note on Exercise 06:** `ft_filter.__doc__` reproduces `print(filter.__doc__)` character for character **as it exists on CPython 3.10** — the version the subject imposes. CPython 3.12 and later dropped the leading signature line from that docstring, so the two strings compare equal on 3.10/3.11 only. Its continuation lines are deliberately flush left: indenting them would push a line past 79 columns and alter the text the evaluator compares.

---

## 🛠️ Complete Module Curriculum

### Exercise 00: First Python Script
- **Turn-in Directory:** `ex00/`
- **Files:** `Hello.py`
- **Core Concepts:** Mutability of `list` / `set` / `dict`, immutability of `tuple`, unordered sets

**Objective:**
Modify the string of each data object so the four containers spell out the greetings `Hello World!`, `Hello <country>!`, `Hello <city>!` and `Hello <campus>!`. Only the four `print` calls placed after the `# your code here` marker may produce output — the file prints exactly four lines.

**Demonstration:**
```text
$> python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'Morocco!')$
{'Hello', 'Benguerir!'}$
{'Hello': '1337Benguerir!'}$
$>
```

---

### Exercise 01: First Use of Package
- **Turn-in Directory:** `ex01/`
- **Files:** `format_ft_time.py`
- **Core Concepts:** Explicit imports, the Unix epoch (`time.time()`), format specifiers, `strftime`

**Objective:**
Display the number of seconds elapsed since January 1, 1970 twice — once with thousand separators and four decimals, once in scientific notation — then display today's date as an abbreviated month, a zero-padded day and a four-digit year.

**Demonstration:**
```text
$> python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,785,543,149.8697 or 1.79e+09 in scientific notation$
Aug 01 2026$
$>
```

---

### Exercise 02: First Function Python
- **Turn-in Directory:** `ex02/`
- **Files:** `find_ft_type.py`
- **Function Signature:** `def all_thing_is_obj(object: any) -> int:`
- **Core Concepts:** `type()` as a dictionary key, `isinstance()`, dispatch tables, import-only modules

**Objective:**
Print the type of the object received and always return `42`. The four container types print their label followed by their class; a string prints `<value> is in the kitchen` followed by its class; anything else prints `Type not found`. Executing the file on its own must print nothing.

**Demonstration:**
```text
$> python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
$> python find_ft_type.py | cat -e
$>
```

---

### Exercise 03: NULL Not Found
- **Turn-in Directory:** `ex03/`
- **Files:** `NULL_not_found.py`
- **Function Signature:** `def NULL_not_found(object: any) -> int:`
- **Core Concepts:** `is` vs `==`, the `NaN != NaN` identity, ordering of conditional branches

**Objective:**
Identify every flavour of "Null" Python offers — `None`, `NaN`, `False`, `0` and the empty string — printing a distinct label and the exact class for each. Return `0` when a flavour was recognized and `1` otherwise. Executing the file on its own must print nothing.

**Demonstration:**
```text
$> python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty:  <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

---

### Exercise 04: The Even and the Odd
- **Turn-in Directory:** `ex04/`
- **Files:** `whatis.py`
- **Core Concepts:** `sys.argv`, guard clauses, EAFP (`int()` raises, it does not return `None`)

**Objective:**
Take a single number as an argument and report whether it is even or odd. With no argument at all, print nothing. With more than one argument, or with an argument that is not an integer, print the corresponding `AssertionError` message.

**Demonstration:**
```text
$> python whatis.py 14
I'm Even.
$> python whatis.py -5
I'm Odd.
$> python whatis.py 0
I'm Even.
$> python whatis.py
$> python whatis.py Hi!
AssertionError: argument is not an integer
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

---

### Exercise 05: First Standalone Program Python
- **Turn-in Directory:** `ex05/`
- **Files:** `building.py`
- **Core Concepts:** `str.isupper` / `islower` / `isdigit` / `isspace`, `string.punctuation`, `sys.stdin.read()` vs `input()`

**Objective:**
Build a real autonomous program with a `main()` that takes a single string argument and prints the number of upper-case, lower-case, punctuation, digit and space characters it contains. With no argument, prompt the user and read the text from standard input — the carriage return counts as a space, so the raw stream is read rather than a stripped line. More than one argument prints an `AssertionError`.

**Demonstration:**
```text
$> python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$> python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

---

### Exercise 06: Recode Filter
- **Turn-in Directory:** `ex06/`
- **Files:** `ft_filter.py`, `filterstring.py`
- **Core Concepts:** List comprehensions, `lambda`, closures, reproducing a built-in contract

**Objective:**
**Part 1** — Recode the `filter` built-in as `ft_filter`, using a list comprehension and reproducing the original `__doc__`. Using the real `filter` is forbidden, and a `None` function must behave like the original: a plain truthiness test.
**Part 2** — Write a program taking a string `S` and an integer `N` that prints the words of `S` strictly longer than `N`. It must contain at least one list comprehension and one lambda. Any other argument shape prints an `AssertionError`.

**Demonstration:**
```text
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$> python filterstring.py 'Hello the World' 99
[]
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

```python
>>> from ft_filter import ft_filter
>>> ft_filter(None, [0, 1, '', 'a', []])
[1, 'a']
```

---

### Exercise 07: Dictionaries SoS
- **Turn-in Directory:** `ex07/`
- **Files:** `sos.py`
- **Core Concepts:** Dictionaries as O(1) lookup tables, membership testing, separation of concerns

**Objective:**
Encode a string into Morse code using a dictionary. Letters and digits become dots and dashes, complete characters are separated by a single space, and a space character becomes a slash. Any argument count other than one, or any unsupported character, prints an `AssertionError`.

**Demonstration:**
```text
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py "hello world" | cat -e
.... . .-.. .-.. --- / .-- --- .-. .-.. -..$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

---

### Exercise 08: Loading ...
- **Turn-in Directory:** `ex08/`
- **Files:** `Loading.py`
- **Function Signature:** `def ft_tqdm(lst: range) -> None:`
- **Core Concepts:** Generators (`yield`), carriage return rendering, `os.get_terminal_size()`

**Objective:**
Reimplement `tqdm` with the `yield` operator. The bar is redrawn in place between items and adapts to the terminal width, falling back to 80 columns when standard output is redirected — `get_terminal_size()` raises `OSError` on a pipe, so the call is guarded.

**Demonstration:**
```text
$> python tester.py
100%|[===============================================================>]| 333/333
100%|██████████| 333/333 [00:01<00:00, 191.61it/s]
$>
```

---

### Exercise 09: My First Package Creation
- **Turn-in Directory:** `ex09/`
- **Files:** `ft_package/`, `pyproject.toml`, `requirements.txt`, `README.md`, `LICENSE`, `tester.py`
- **Core Concepts:** `pyproject.toml` metadata, source archive vs wheel, `__init__.py` as a public API

**Objective:**
Create an installable package named `ft_package` version `0.0.1` that exposes `count_in_list`, builds to both a `.tar.gz` and a `.whl`, and reports its characteristics through `pip show -v`.

**Demonstration:**
```text
$> python -m build
Successfully built ft_package-0.0.1.tar.gz and ft_package-0.0.1-py3-none-any.whl
$> pip install ./dist/ft_package-0.0.1-py3-none-any.whl
$> pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/paybackfx/ft_package
Author: payback_fx
Author-email: sirfennoune@gmail.com
License: MIT
Location: ...
Requires:
Required-by:
Metadata-Version: 2.4
Installer: pip
Classifiers:
  Programming Language :: Python :: 3
  License :: OSI Approved :: MIT License
  Operating System :: OS Independent
Entry-points:
$>
```

```python
>>> from ft_package import count_in_list
>>> count_in_list(["toto", "tata", "toto"], "toto")
2
>>> count_in_list(["toto", "tata", "toto"], "tutu")
0
```
