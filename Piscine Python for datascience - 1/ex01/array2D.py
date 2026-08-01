#!/usr/bin/env python3
# =============================================================================
# EXERCISE 01: 2D ARRAY
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Shape (array.shape): a tuple describing the array in every dimension, so
#    (4, 2) reads "four rows of two columns". It is the first thing to check
#    when a computation silently produces the wrong numbers.
# 2. Slicing (array[start:end]): selects a range of rows without copying the
#    data element by element, and supports negative bounds counting from the
#    end - array[1:-2] keeps row 1 only on a four-row table.
# 3. Rectangularity: NumPy refuses a ragged table, so rows of different
#    lengths are rejected up front with an explicit message rather than
#    letting NumPy build an opaque array of Python objects.
# =============================================================================

import numpy as np


def check_family(family: list) -> None:
    """Raise TypeError or ValueError when family is not a 2D table."""
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if len(family) == 0:
        raise ValueError("family must not be empty")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")
    if len({len(row) for row in family}) != 1:
        raise ValueError("every row of family must have the same length")
    for row in family:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("every value must be an int or a float")


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shapes and return the rows of family from start to end."""
    try:
        check_family(family)
        if isinstance(start, bool) or not isinstance(start, int):
            raise TypeError("start must be an int")
        if isinstance(end, bool) or not isinstance(end, int):
            raise TypeError("end must be an int")
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        truncated = array[start:end]
        print(f"My new shape is : {truncated.shape}")
        return truncated.tolist()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return None


def main() -> None:
    """Demonstrate the nominal case and the guarded error cases."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print("=== Nominal ===")
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print("=== Error cases ===")
    slice_me([[1.80, 78.4], [2.15]], 0, 2)
    slice_me("not a list", 0, 2)
    slice_me([], 0, 2)
    slice_me(family, "0", 2)


if __name__ == "__main__":
    main()
