#!/usr/bin/env python3
# =============================================================================
# EXERCISE 00: CALCULATE MY STATISTICS
# =============================================================================
# Educational Notes for Beginners:
#
# 1. *args and **kwargs: *args collects the positional values into a tuple
#    and **kwargs collects the named ones into a dict. Here the keys of
#    kwargs are ignored - only their values name the statistic to compute.
# 2. A Dispatch Table Of Functions: functions are values in Python, so the
#    requested name is looked up in a dict to get the function to call. An
#    unknown name simply is not in the table and is silently skipped.
# 3. Linear Interpolation For Quartiles: with n values the 25% quartile sits
#    at position 0.25 * (n - 1). When that position falls between two values
#    the result is interpolated, which is what NumPy does by default.
# 4. Population, Not Sample: the variance divides by n and not by n - 1, the
#    convention the subject's expected numbers were produced with.
# =============================================================================

from typing import Any


def mean(values: list) -> float:
    """Return the arithmetic mean of the values."""
    return sum(values) / len(values)


def median(values: list) -> float:
    """Return the middle value, averaging the two middles if even."""
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def percentile(values: list, ratio: float) -> float:
    """Return the interpolated value sitting at the given ratio."""
    ordered = sorted(values)
    position = ratio * (len(ordered) - 1)
    low = int(position)
    high = min(low + 1, len(ordered) - 1)
    return float(ordered[low] + (ordered[high] - ordered[low])
                 * (position - low))


def quartile(values: list) -> list:
    """Return the 25% and 75% quartiles of the values."""
    return [percentile(values, 0.25), percentile(values, 0.75)]


def var(values: list) -> float:
    """Return the population variance of the values."""
    average = mean(values)
    return sum((value - average) ** 2 for value in values) / len(values)


def std(values: list) -> float:
    """Return the population standard deviation of the values."""
    return var(values) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print every statistic named in kwargs, ERROR when impossible."""
    operations = {"mean": mean, "median": median, "quartile": quartile,
                  "std": std, "var": var}
    values = [value for value in args
              if isinstance(value, (int, float))
              and not isinstance(value, bool)]
    for wanted in kwargs.values():
        if not isinstance(wanted, str) or wanted not in operations:
            continue
        try:
            print(f"{wanted} : {operations[wanted](values)}")
        except (ZeroDivisionError, IndexError, TypeError, ValueError):
            print("ERROR")


def main() -> None:
    """Reproduce the four scenarios described by the subject."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
