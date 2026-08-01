# 📊 DataTable: Loading, Reshaping and Plotting Real Data (Module 02)

> **Course Summary:** Move from arrays to labelled tables. Load a real Gapminder dataset with pandas, survive its encoding and its human-readable numbers, then turn three centuries of demographic history into graphs that actually answer a question.

---

## 🎯 Educational Philosophy & DataTable Masterclass

An array knows its positions; a **DataFrame** knows its names. That difference is what turns a matrix of numbers into a dataset you can interrogate. This module is about the unglamorous half of data science — getting the data in, and getting it right — followed by the half everyone sees.

### 1. The DataFrame: Columns Have Names
`pandas` reads a CSV into a table with labelled columns and an index. A column is reached by name, a subset of rows by a boolean mask (`dataset[dataset["country"] == "Morocco"]`), and the whole file is queried without a single loop. Comparing a column to a value produces a mask; indexing the frame with that mask keeps only the rows where it is `True`.

### 2. Real Data Fights Back
These files come from Gapminder, and they are a catalogue of the traps real datasets set:
- **A byte order mark.** Reading them as plain UTF-8 names the first column `﻿country` instead of `country`, and every later lookup fails with a `KeyError` that points nowhere. `encoding="utf-8-sig"` is not optional.
- **Human-readable numbers.** Populations are stored as `"3.28M"` and `"1.16B"`, incomes as `"1.05k"`. Every cell is a **string** and has to be parsed back into a float before anything can be plotted.
- **Missing values.** Some countries have no data for some years. They are `NaN`, and they must be dropped rather than silently coerced to zero.

### 3. Wide Format
These datasets store **one column per year**, so the years are the column *labels*, not a column of values. Reading a country's history therefore means reading one row across, and the labels have to be cast to `int` to become a real numeric x axis instead of a sequence of strings.

### 4. Choosing The Right Plot
- **A line** implies continuity — correct for one country's life expectancy through time.
- **Two lines on one axes** invite comparison, which is why each needs a `label=` and why `plt.legend()` is mandatory.
- **A scatter** is for independent observations. Each point in Exercise 03 is a different country in the same year; joining them would suggest a progression that does not exist.
- **A logarithmic axis** turns a multiplicative spread into a linear one. Incomes in 1900 span three orders of magnitude, and a linear axis would crush every poor country into the left margin.

### 5. A Graph Without Labels Is Noise
The subject requires a title and a legend on each axis for every graph, and a per-curve legend where several series share the axes. A curve nobody can read proves nothing.

---

## 📚 General Engineering Standards

- All implementations target **Python 3.10**, the version the subject mandates.
- Code formatting complies with **flake8** at 79 columns. `python -m flake8 .` on this directory returns nothing.
- Imports are **explicit** (`import pandas as pd`, `import matplotlib.pyplot as plt`) — never `from x import *` — and there is no mutable global state.
- Every function carries a `__doc__`, and every program has a `main()` behind an `if __name__ == "__main__":` guard.
- `load()` never raises: a bad path, an empty file or a malformed CSV prints a clear message and returns `None`, and every caller checks for it.
- `load_csv.py` is **byte-identical** in all four exercise directories, as the subject's turn-in lists require.
- The campus country is **Morocco** (1337 Benguerir), compared against **France** in Exercise 02.

> 💡 **Data source:** free school materials from GAPMINDER.ORG, CC-BY license.

---

## 🛠️ Complete Module Curriculum

### Exercise 00: Load My Dataset
- **Turn-in Directory:** `ex00/`
- **Files:** `load_csv.py`, `life_expectancy_years.csv`
- **Function Signature:** `def load(path: str) -> pd.DataFrame:`
- **Core Concepts:** `pd.read_csv`, the UTF-8 BOM, `DataFrame.shape`

**Objective:**
Take a path, print the dimensions of the dataset and return it. A bad path, a non-CSV file or a malformed file prints a clear message and returns `None`.

**Demonstration:**
```text
$> python tester.py
Loading dataset of dimensions (195, 302)
                  country  1800  1801  ...  2099  2100
0             Afghanistan  28.2  28.2  ...  76.6  76.8
1                  Angola  27.0  27.0  ...  79.9  80.0
2                 Albania  35.4  35.4  ...  88.3  88.4
...
$>
```

---

### Exercise 01: Draw My Country
- **Turn-in Directory:** `ex01/`
- **Files:** `load_csv.py`, `aff_life.py`, `life_expectancy_years.csv`
- **Core Concepts:** Boolean row selection, wide format, `plt.plot`

**Objective:**
Load `life_expectancy_years.csv` and draw the life expectancy of the campus country over time. The graph carries a title and a label on both axes.

**Demonstration:**
```text
$> python aff_life.py
Loading dataset of dimensions (195, 302)
[a window opens: "Morocco Life expectancy Projections", x = Year, y = Life expectancy]
$>
```

---

### Exercise 02: Compare My Country
- **Turn-in Directory:** `ex02/`
- **Files:** `load_csv.py`, `aff_pop.py`, `population_total.csv`
- **Core Concepts:** Suffix parsing (`k` / `M` / `B`), two series on one axes, `FuncFormatter`

**Objective:**
Load `population_total.csv` and compare the campus country against another one from 1800 to 2050. The graph carries a title, a label on both axes and a legend naming each curve; the y axis is relabelled in millions to stay readable.

**Demonstration:**
```text
$> python aff_pop.py
Loading dataset of dimensions (197, 302)
[a window opens: "Population Projections", Morocco and France from 1800 to 2050,
 y axis ticks in M, legend in the lower right corner]
$>
```

---

### Exercise 03: Draw My Year
- **Turn-in Directory:** `ex03/`
- **Files:** `load_csv.py`, `projection_life.py`, `income_per_person_gdppercapita_ppp_inflation_adjusted.csv`, `life_expectancy_years.csv`
- **Core Concepts:** Pairing two datasets on a shared key, scatter plots, logarithmic scales

**Objective:**
Load both datasets and project life expectancy against gross domestic product for the year **1900**, one point per country present in both files. The graph carries a title, a label on both axes and a legend naming the series; the x axis is logarithmic with ticks at 300, 1k and 10k.

**Demonstration:**
```text
$> python projection_life.py
Loading dataset of dimensions (195, 252)
Loading dataset of dimensions (195, 302)
[a window opens: title "1900", x = Gross domestic product (log), y = Life Expectancy]
$>
```

**Do you see a correlation between life span and gross domestic product?**
Yes — and it is a *logarithmic* one. On the log axis the cloud rises in a broad straight band: countries around 300 $/year cluster near 25–30 years of life expectancy, those around 3 000 $/year near 40–50. Because the axis is logarithmic, that straight band means each **doubling** of income buys roughly the same number of extra years, not each extra dollar. The returns are real but they diminish sharply — which is exactly why the wealthiest countries of 1900 are bunched at the top right with only a few years between them, while the spread among the poorest is enormous.
