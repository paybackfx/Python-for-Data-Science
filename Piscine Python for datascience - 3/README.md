# 👑 Oriented Object Programming: Classes, Inheritance and the Diamond (Module 03)

> **Course Summary:** Model Westeros to learn object design. Abstract base classes that refuse to exist, families that inherit their traits, a false king born of two bloodlines at once, and operators taught to speak vector.

---

## 🎯 Educational Philosophy & OOP Masterclass

Object-oriented programming is not about grouping functions under a class name. It is about deciding **what varies, what stays, and who is allowed to know**. This module walks that decision four times, each time with a sharper edge.

### 1. Abstract Base Classes: Declaring Without Existing
`Character` describes what every character shares — a first name, a health state, the ability to die — but no one is ever "just a character". Inheriting from `ABC` and marking a method `@abstractmethod` is what makes `Character("hodor")` raise a `TypeError` while still letting the method carry the shared implementation that children reach through `super()`.

### 2. `super()` Is Not "The Parent"
`super()` calls **the next class in the resolution order**, which is not the same thing. With single inheritance the distinction is invisible; with the diamond of Exercise 02 it is the whole exercise. Writing `Character.__init__(self, ...)` instead would break the chain and initialise `Character` twice.

### 3. `__str__` vs `__repr__`
`__str__` is what `print()` shows a human; `__repr__` is what the interpreter shows a developer. Returning a string from both is what turns `<S1E7.Baratheon object at 0x7f...>` into something readable. The subject's expected output proves it in a subtle way: printing `Robert.__str__` *without calling it* renders `<bound method Baratheon.__str__ of ...>`, and the part after `of` is `repr(instance)` — so the `Vector: (...)` line can only appear there if `__repr__` returns it.

### 4. `@classmethod`: The Alternative Constructor
A class method receives the class itself as `cls` rather than an instance, so it can build objects without the caller ever writing `Lannister(...)` directly. Because it uses `cls` and not the hard-coded name, a subclass inherits a factory that produces *its own* type.

### 5. The Diamond Problem and C3 Linearization
`King` inherits from `Baratheon` and `Lannister`, which both inherit from `Character`. Which `__init__` wins? Since Python 2.3 the answer is deterministic: the **C3 linearization** produces the order `King → Baratheon → Lannister → Character → ABC → object`. Each `super().__init__()` walks one step down that chain, so `Character` is initialised exactly once, `Lannister` sets its traits, and `Baratheon` — being earlier in the order — overwrites them last and wins.

### 6. Properties Are Data Descriptors
A class-level `property` takes precedence over the instance dictionary. That is the trap: writing `self.eyes = value` inside the `eyes` setter calls the setter again, forever. The value is therefore stored directly in `self.__dict__`, which also keeps `__dict__` printing exactly as the subject expects.

### 7. Operator Overloading
Defining `__add__`, `__mul__`, `__sub__` and `__truediv__` teaches Python what `+`, `*`, `-` and `/` mean for your own type, so a calculator object reads like plain arithmetic.

---

## 📚 General Engineering Standards

- All implementations target **Python 3.10**, the version the subject mandates.
- Code formatting complies with **flake8** at 79 columns. `python -m flake8 .` on this directory returns nothing.
- Imports are **explicit** and there is no global state.
- Every class, method and function carries a `__doc__`, and every file ships a `main()` behind an `if __name__ == "__main__":` guard so it can be executed on its own.
- Naming follows the subject, not PEP 8, where the two disagree: the class in Exercises 03 and 04 is spelled `calculator` in lower case because that is the prototype the subject gives.
- Per the subject's turn-in lists, `ex01/` also contains `S1E9.py`, and `ex02/` contains both `S1E9.py` and `S1E7.py`.

> ⚠️ **Note on Exercise 02:** the subject's expected output prints the key `'hair'` in the first dictionary and `'hairs'` in the second. That is a typo in the PDF — the attribute is `hairs` throughout `S1E7.py`, so this implementation prints `'hairs'` consistently in both.

> ⚠️ **Note on Exercise 00:** the exact wording of the `TypeError` raised when instantiating an abstract class changed in CPython 3.12. On the mandated 3.10 it reads `Can't instantiate abstract class Character with abstract method __init__`; on newer interpreters it reads `...without an implementation for abstract method '__init__'`. The behaviour — refusing to instantiate — is identical.

---

## 🛠️ Complete Module Curriculum

### Exercise 00: GOT S1E9
- **Turn-in Directory:** `ex00/`
- **Files:** `S1E9.py`
- **Core Concepts:** `ABC`, `@abstractmethod`, `super()`, `__dict__`

**Objective:**
Create an abstract class `Character` taking a `first_name` and an optional `is_alive` defaulting to `True`, with a method flipping the health state, and a `Stark` class inheriting from it. Instantiating `Character` directly must fail.

**Demonstration:**
```text
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Representing the Stark family.
Initialize a Stark with a first name and a health state.
Turn the health state of the character from alive to dead.
---
{'first_name': 'Lyanna', 'is_alive': False}
---
TypeError: Can't instantiate abstract class Character with abstract method __init__
$>
```

---

### Exercise 01: GOT S1E7
- **Turn-in Directory:** `ex01/`
- **Files:** `S1E9.py`, `S1E7.py`
- **Core Concepts:** `__str__`, `__repr__`, `@classmethod`

**Objective:**
Create two families inheriting from `Character`, instantiable without going through it, whose `__str__` and `__repr__` return strings rather than objects, plus a class method that creates characters in a chain.

**Demonstration:**
```text
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>
```

---

### Exercise 02: Now It's Weird!
- **Turn-in Directory:** `ex02/`
- **Files:** `S1E9.py`, `S1E7.py`, `DiamondTrap.py`
- **Core Concepts:** Multiple inheritance, C3 linearization, `property`

**Objective:**
Create `King(Baratheon, Lannister)` — Joffrey, the monster born of both families — and use properties to change his physical characteristics.

**Demonstration:**
```text
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$> python DiamondTrap.py
...
MRO: ['King', 'Baratheon', 'Lannister', 'Character', 'ABC', 'object']
$>
```

---

### Exercise 03: Calculate My Vector
- **Turn-in Directory:** `ex03/`
- **Files:** `ft_calculator.py`
- **Core Concepts:** `__add__`, `__mul__`, `__sub__`, `__truediv__`, in-place semantics

**Objective:**
Write a calculator class combining a vector with a scalar. Each operation prints the result — and stores it, which is what makes `v3 / 5` operate on the result of `v3 - 5`. Only division by zero needs error handling.

**Demonstration:**
```text
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
```

---

### Exercise 04: Calculate My Dot Product
- **Turn-in Directory:** `ex04/`
- **Files:** `ft_calculator.py`
- **Core Concepts:** `@staticmethod`, `zip`, the dot product

**Objective:**
Write a calculator class doing vector-to-vector arithmetic whose methods are callable **without instantiating the class** — that is the decorator the subject hints at.

**Demonstration:**
```text
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
```
