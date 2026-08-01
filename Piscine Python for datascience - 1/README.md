# 🔢 Array: Vectorized Computation and Image Manipulation (Module 01)

> **Course Summary:** Leave Python lists behind and start thinking in arrays. Discover how NumPy turns a loop into a single expression, why an image is nothing more than a three-dimensional array of bytes, and how slicing, transposing and channel arithmetic are the same operation seen from different angles.

---

## 🎯 Educational Philosophy & Array Masterclass

Data science does not iterate, it *vectorizes*. The moment a dataset grows past a few thousand rows, a Python `for` loop stops being an implementation detail and becomes the bottleneck. This module is where that habit is replaced.

### 1. The Array Is The Unit Of Work
A NumPy array is a contiguous block of memory with a known type and a known **shape**. Dividing two arrays does not run Python code per element — it runs one optimized C loop. `weights / heights ** 2` computes the BMI of an entire population in a single expression, and it stays a single expression whether the population is two people or two million.

### 2. Shape Is The First Thing To Check
`array.shape` is a tuple describing every dimension. `(4, 2)` reads "four rows of two columns"; `(768, 1024, 3)` reads "768 rows of 1024 pixels of 3 channels". Note the order: **height comes first**, which is the opposite of the `(width, height)` convention Pillow uses in `image.size`. Most array bugs are shape bugs.

### 3. Slicing Selects, It Does Not Copy
`array[start:end]` and `array[y0:y1, x0:x1]` produce a **view** onto the same memory. That makes cropping free — but it also means writing into a slice writes into the original. Every filter in this module therefore works on an explicit `.copy()`, so the caller's image is never silently corrupted.

### 4. An Image Is Just An Array
Pillow decodes the JPEG, NumPy exposes the result as `(height, width, channels)`, and from that point on everything is arithmetic:
- **Cropping** is slicing on the first two axes.
- **Greyscale** is collapsing the third axis. The eye is far more sensitive to green than to blue, so the luminance is `0.299 R + 0.587 G + 0.114 B` rather than a plain mean.
- **A colour filter** is zeroing or inverting a channel.

### 5. Transpose Is Not Rotation
Transposing swaps the two indices: the output pixel `(x, y)` is read from the input pixel `(y, x)`. The result is mirrored along the main diagonal. A true 90° rotation would additionally reverse one axis — the subject asks for the transpose, and it must be written by hand, without any library helper.

### 6. Errors Are Reported, Never Raised
The subject invalidates any exercise that lets an exception escape. Every public function therefore validates its input, catches its own failures, prints a clear message and returns `None`. A traceback in front of an evaluator is a failed exercise, however correct the happy path is.

---

## 📚 General Engineering Standards

- All implementations target **Python 3.10**, the version the subject mandates.
- Code formatting complies with **flake8** at 79 columns. `python -m flake8 .` on this directory returns nothing.
- Imports are **explicit** (`import numpy as np`) — never `from x import *` — and there is no mutable global state; the only module-level names are uppercase constants.
- Every function carries a `__doc__`, and every runnable program has a `main()` behind an `if __name__ == "__main__":` guard.
- Library modules imported by another file (`give_bmi.py`, `array2D.py`, `load_image.py`, `pimp_image.py`) also ship a `main()` demonstrating their behaviour, so every file can be executed on its own.
- Every expected output listed below was reproduced by **running the code**.

> ⚠️ **Note on Exercises 03 and 04:** the zoom window is anchored at `(TOP, LEFT) = (284, 187)`. That is not an arbitrary choice — it is the single 400×400 crop of `animal.jpeg` whose luminance reproduces the subject's own `167 / 180 / 194` values exactly, so the printed arrays match the PDF character for character.

> ⚠️ **Note on Exercise 04:** `rotate.py` prints two shape lines, because `ft_load` announces the original `(768, 1024, 3)` before the square is cut and the subject's expected block starts after that cut. The required `The shape of image is: (400, 400, 1)` line is present verbatim; the extra line is strictly additional information.

---

## 🛠️ Complete Module Curriculum

### Exercise 00: Give My BMI
- **Turn-in Directory:** `ex00/`
- **Files:** `give_bmi.py`
- **Function Signatures:** `def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:` and `def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:`
- **Core Concepts:** Vectorized division, `.tolist()`, input validation

**Objective:**
Compute the BMI of a population from two parallel lists, then flag every value above a limit. Mismatched lengths, non-numeric measures and non-positive heights are reported with a clear message instead of a traceback.

**Demonstration:**
```text
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
$> python give_bmi.py
=== Error cases ===
Error: height and weight must have the same length
Error: every measure must be an int or a float
Error: every height must be strictly positive
$>
```

---

### Exercise 01: 2D Array
- **Turn-in Directory:** `ex01/`
- **Files:** `array2D.py`
- **Function Signature:** `def slice_me(family: list, start: int, end: int) -> list:`
- **Core Concepts:** `array.shape`, row slicing, negative bounds, rectangularity

**Objective:**
Print the shape of a 2D table, return the rows between `start` and `end` using slicing, and print the shape of the result. Ragged tables and non-list inputs are rejected with an explicit message.

**Demonstration:**
```text
$> python tester.py
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
$>
```

---

### Exercise 02: Load My Image
- **Turn-in Directory:** `ex02/`
- **Files:** `load_image.py`, `landscape.jpg`
- **Function Signature:** `def ft_load(path: str) -> np.ndarray:`
- **Core Concepts:** Pillow decoding, `convert("RGB")`, the `(h, w, c)` layout

**Objective:**
Load a JPG or JPEG, print its shape and return its RGB pixel array. A missing file, an unreadable file or an unsupported format prints a clear message and returns `None`.

**Demonstration:**
```text
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
  [23 42 84]
  [28 43 84]
  ...
  [ 0  0  0]
  [ 1  1  1]
  [ 1  1  1]]]
$>
```

---

### Exercise 03: Zoom On Me
- **Turn-in Directory:** `ex03/`
- **Files:** `load_image.py`, `zoom.py`, `animal.jpeg`
- **Core Concepts:** Two-dimensional slicing, luminance, `np.newaxis`, `matplotlib` axes

**Objective:**
Load `animal.jpeg`, print its size, channel count and pixels, then cut a 400×400 square, collapse it to a single luminance channel and display it with a pixel scale on both axes.

**Demonstration:**
```text
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
  [139 130 151]
  [155 146 167]
  ...
New shape after slicing: (400, 400, 1)
[[[167]
  [180]
  [194]
  ...
$>
```

---

### Exercise 04: Rotate Me
- **Turn-in Directory:** `ex04/`
- **Files:** `load_image.py`, `rotate.py`, `animal.jpeg`
- **Core Concepts:** Hand-written transposition, nested comprehensions

**Objective:**
Cut the same square from `animal.jpeg` and transpose it **without any library helper** — the output pixel `(x, y)` is read from the input pixel `(y, x)`. Print the new shape and the transposed data, then display the result.

**Demonstration:**
```text
$> python rotate.py
The shape of image is: (400, 400, 1)
[[[167]
  [180]
  [194]
  ...
New shape after Transpose: (400, 400)
[[167 177 188 ...  83  78  72]
 [180 191 200 ...  61  60  58]
 [194 205 210 ...  66  67  67]
 ...
$>
```

---

### Exercise 05: Pimp My Image
- **Turn-in Directory:** `ex05/`
- **Files:** `load_image.py`, `pimp_image.py`, `landscape.jpg`
- **Core Concepts:** Channel arithmetic under operator restrictions, `.copy()` discipline

**Objective:**
Write five colour filters that all preserve the image shape, each using only the operators the subject allows:

| Filter | Allowed operators | Implementation |
|---|---|---|
| `ft_invert` | `=` `+` `-` `*` | `255 - array` |
| `ft_red` | `=` `*` | green and blue channels multiplied by 0 |
| `ft_green` | `=` `-` | red and blue channels subtracted from themselves |
| `ft_blue` | `=` | red and green channels assigned 0 |
| `ft_grey` | `=` `/` | the green channel copied over the other two |

**Demonstration:**
```text
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
  ...
Inverts the color of the image received.
Keeps only the red channel of the image received.
Keeps only the green channel of the image received.
Keeps only the blue channel of the image received.
Turns the image received into shades of grey.
$>
```

Running `python pimp_image.py` displays the original next to the five filtered versions in a single 2×3 figure.
