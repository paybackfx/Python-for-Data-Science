#!/usr/bin/env python3
# =============================================================================
# EXERCISE 00: GIVE MY BMI
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Vectorization (np.array): dividing two arrays applies the operation to
#    every pair of elements at C speed, so the BMI of a whole population is
#    one expression instead of a Python loop.
# 2. .tolist() Is Not Optional: a NumPy array yields np.float64 objects, and
#    NumPy 2 prints them as "np.float64(22.5)". .tolist() converts them back
#    to native Python floats so the output matches the subject exactly.
# 3. bool Is A Subclass Of int: isinstance(True, int) is True, so the type
#    check has to exclude bool explicitly or True would pass as a height.
# 4. Errors Are Reported, Never Raised: the subject invalidates any uncaught
#    exception, so the validation raises internally and the public function
#    catches, prints a clear message and returns None.
# =============================================================================

import numpy as np


def check_lists(height: list, weight: list) -> None:
    """Raise TypeError or ValueError when the two lists are unusable."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must both be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same length")
    if len(height) == 0:
        raise ValueError("height and weight must not be empty")
    for value in height + weight:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("every measure must be an int or a float")
    if any(value <= 0 for value in height):
        raise ValueError("every height must be strictly positive")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Return the BMI of each individual, or None if the input is invalid."""
    try:
        check_lists(height, weight)
        heights = np.array(height, dtype=float)
        weights = np.array(weight, dtype=float)
        return (weights / heights ** 2).tolist()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for every BMI strictly above limit, None if invalid."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        if isinstance(limit, bool) or not isinstance(limit, int):
            raise TypeError("limit must be an int")
        for value in bmi:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("every bmi must be an int or a float")
        return [value > limit for value in bmi]
    except TypeError as error:
        print(f"Error: {error}")
        return None


def main() -> None:
    """Demonstrate the nominal case and the guarded error cases."""
    print("=== Nominal ===")
    bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    print("=== Error cases ===")
    give_bmi([2.71, 1.15], [165.3])
    give_bmi([2.71, "1.15"], [165.3, 38.4])
    give_bmi([0, 1.15], [165.3, 38.4])
    give_bmi("2.71", [165.3])
    apply_limit([22.5, 29.0], "26")


if __name__ == "__main__":
    main()
