#!/usr/bin/env python3
# =============================================================================
# EXERCISE 00: LOAD MY DATASET
# =============================================================================
# Educational Notes for Beginners:
#
# 1. DataFrame: pandas represents a CSV as a table with labelled columns and
#    an index, so a column is reached by name instead of by position and the
#    whole file is queried without a single loop.
# 2. encoding="utf-8-sig": these Gapminder exports start with a byte order
#    mark, and reading them as plain utf-8 would name the first column
#    "﻿country" instead of "country" - every later lookup would fail.
# 3. shape: a (rows, columns) tuple, printed here as the dimensions of the
#    dataset so a truncated or malformed file is spotted immediately.
# 4. Errors Are Reported, Never Raised: a missing or unreadable path prints a
#    clear message and returns None, as the subject requires.
# =============================================================================

import sys

import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Print the dimensions of the CSV at path and return it, None if bad."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if not path.lower().endswith(".csv"):
            raise ValueError(f"{path}: only .csv files are supported")
        dataset = pd.read_csv(path, encoding="utf-8-sig")
    except FileNotFoundError:
        print(f"Error: {path}: no such file or directory")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: {path}: the file is empty")
        return None
    except pd.errors.ParserError as error:
        print(f"Error: {path}: malformed csv ({error})")
        return None
    except (TypeError, ValueError, OSError, UnicodeDecodeError) as error:
        print(f"Error: {error}")
        return None
    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset


def main() -> None:
    """Load the CSV given on the command line and print it."""
    path = sys.argv[1] if len(sys.argv) == 2 else "life_expectancy_years.csv"
    print(load(path))


if __name__ == "__main__":
    main()
