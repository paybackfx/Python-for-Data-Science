# 🏗️ Data Oriented Design: Closures, Decorators and Data Classes (Module 04)

> **Course Summary:** The last module trades objects for functions. Variadic signatures, statistics implemented from first principles with no library at all, closures that remember, decorators that police, and data classes that write their own boilerplate.

---

## 🎯 Educational Philosophy & Structure Masterclass

Python treats functions as values, and this module is where that stops being trivia and starts being architecture. A function that returns a function, a function that wraps a function, a class that generates its own methods — each is a way of moving a decision from run time to definition time.

### 1. `*args` and `**kwargs`: Signatures That Do Not Commit
`*args` collects positional values into a tuple, `**kwargs` collects named ones into a dict. Exercise 00 pushes this to its logical end: the **keys** of `kwargs` are meaningless — `toto`, `tutu`, `tata` — and only their **values** name the statistic to compute.

### 2. Functions Are Values: The Dispatch Table
Looking a name up in a `{"mean": mean, "median": median, ...}` dictionary and calling the result replaces a chain of `if/elif` with a single lookup. An unknown name is simply not in the table and is silently skipped, which is exactly the behaviour the subject's third test case expects.

### 3. Statistics From First Principles
`Allowed functions: None` — no `statistics`, no `numpy`, no `math`. Two details decide whether the numbers match:
- **Quartiles interpolate.** With *n* values the 25% quartile sits at position `0.25 × (n − 1)`. When that position falls between two values the result is interpolated linearly, which is what NumPy does by default.
- **The variance is the population one.** It divides by *n*, not by *n − 1*. Dividing by *n − 1* would give a different number from the subject's expected output.

### 4. Closures: State Without Globals
`inner()` keeps a live reference to `x`, `count` and `function` long after `outer()` has returned. The state lives in the **enclosing scope** — not in a global, which the subject explicitly forbids. `nonlocal` is what makes it work: without it, `x = function(x)` would create a brand new local variable and every call would restart from the initial value.

### 5. Decorators: Three Nested Levels
`callLimit(3)` is a **decorator factory**. It captures the limit and returns `callLimiter`, which captures the function and returns `limit_function`, the object that finally replaces the original name. Because `count` lives in the scope of `callLimit`, every `@callLimit(n)` gets its own independent counter — `f()` exhausting its budget never affects `g()`.

### 6. Data Classes: Boilerplate That Writes Itself
`@dataclass` generates `__init__`, `__repr__` and `__eq__` from the annotated attributes, which is why the class never defines `__str__` or `__repr__` and still prints readably. Two field options carry the whole exercise:
- **`field(init=False)`** removes the attribute from the generated `__init__`, so passing `id="toto"` raises a `TypeError` — exactly the protection the subject asks for.
- **`default_factory`** is called *per instance*. A plain default would be evaluated once at class creation and every student would share the same identifier.

`__post_init__` runs right after the generated `__init__` and is the only place a computed field such as the login can be built.

---

## 📚 General Engineering Standards

- All implementations target **Python 3.10**, the version the subject mandates.
- Code formatting complies with **flake8** at 79 columns. `python -m flake8 .` on this directory returns nothing.
- Imports are **explicit** and there is no global state — Exercise 01 explicitly replaces `global` with `nonlocal`.
- Every function carries a `__doc__`, and every file ships a `main()` behind an `if __name__ == "__main__":` guard.
- Naming follows the subject, not PEP 8, where the two disagree: `callLimit`, `callLimiter`, `sous_vec` and the shadowing `pow` are the prototypes the subject gives.

> ⚠️ **Note on Exercise 00:** the file is named `statistics.py`, which shadows the standard library module of the same name for anything running from that directory. That is the subject's requirement, and it is the reason the implementation imports nothing but `typing.Any`.

---

## 🛠️ Complete Module Curriculum

### Exercise 00: Calculate My Statistics
- **Turn-in Directory:** `ex00/`
- **Files:** `statistics.py`
- **Function Signature:** `def ft_statistics(*args: Any, **kwargs: Any) -> None:`
- **Core Concepts:** Variadic signatures, dispatch tables, hand-written statistics

**Objective:**
Take an unknown quantity of values in `*args` and compute the mean, median, quartiles, standard deviation or variance according to what `**kwargs` asks for. An unknown statistic is skipped; a statistic that cannot be computed prints `ERROR`.

**Demonstration:**
```text
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
$>
```

---

### Exercise 01: Outer_inner
- **Turn-in Directory:** `ex01/`
- **Files:** `in_out.py`
- **Function Signatures:** `def square(x: int | float) -> int | float:`, `def pow(x: int | float) -> int | float:`, `def outer(x: int | float, function) -> object:`
- **Core Concepts:** Closures, `nonlocal`, higher-order functions

**Objective:**
Write a function returning the square of its argument, one returning the argument raised to itself, and one taking a number and a function and returning an **object that, when called, returns the result of the calculation** — accumulating across calls.

**Demonstration:**
```text
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
$>
```

---

### Exercise 02: My First Decorating
- **Turn-in Directory:** `ex02/`
- **Files:** `callLimit.py`
- **Function Signature:** `def callLimit(limit: int):`
- **Core Concepts:** Decorator factories, wrappers, per-decoration state

**Objective:**
Write a decorator taking a call limit and blocking the execution of the decorated function above it. Two differently limited functions must keep independent counters.

**Demonstration:**
```text
$> python tester.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>
```

---

### Exercise 03: Data Class
- **Turn-in Directory:** `ex03/`
- **Files:** `new_student.py`
- **Core Concepts:** `@dataclass`, `field(init=False)`, `default_factory`, `__post_init__`

**Objective:**
Write a data class taking a name and a surname, setting `active` to `True`, building the login from the first letter of the name plus the surname, and generating a random identifier. `__str__` and `__repr__` must not be defined, and neither `login` nor `id` may be passed to the constructor.

**Demonstration:**
```text
$> python tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='wngvbxuxlrkjsjm')
$> python new_student.py
...
TypeError: Student.__init__() got an unexpected keyword argument 'id'
$>
```
