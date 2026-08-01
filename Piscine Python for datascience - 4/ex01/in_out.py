#!/usr/bin/env python3
# =============================================================================
# EXERCISE 01: OUTER_INNER
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Closure: inner() keeps a live reference to x, count and function long
#    after outer() has returned. The state lives in the enclosing scope, not
#    in a global, which is exactly what the subject forbids.
# 2. nonlocal: without it, "x = function(x)" would create a brand new local
#    variable inside inner() and every call would restart from the initial
#    value. nonlocal rebinds the name of the enclosing scope instead.
# 3. Functions Are Values: outer() receives square or pow as an argument and
#    returns another function, which is what makes the counter reusable with
#    any transformation.
# =============================================================================


def square(x: int | float) -> int | float:
    """Return the square of the given number."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return the given number raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a callable applying function to its own result each call."""
    count = 0

    def inner() -> float:
        """Apply the function once more and return the running result."""
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner


def main() -> None:
    """Demonstrate the accumulating counter with both transformations."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
