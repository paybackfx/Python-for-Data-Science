#!/usr/bin/env python3
# =============================================================================
# EXERCISE 02: MY FIRST DECORATING
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Three Nested Levels: callLimit(3) is a decorator factory - it captures
#    the limit and returns callLimiter, which captures the function and
#    returns limit_function, the object that finally replaces it.
# 2. One Counter Per Decoration: count lives in the scope of callLimit, so
#    @callLimit(3) and @callLimit(1) each get their own independent counter
#    and f() exhausting its budget never affects g().
# 3. *args and **kwds Pass Through: the wrapper accepts any signature and
#    forwards it untouched, so decorating a function never changes how the
#    rest of the code calls it.
# =============================================================================

from typing import Any


def callLimit(limit: int):
    """Return a decorator blocking a function above limit calls."""
    count = 0

    def callLimiter(function):
        """Wrap the function with the shared call counter."""
        def limit_function(*args: Any, **kwds: Any):
            """Run the function while the limit is not reached."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter


def main() -> None:
    """Demonstrate two independently limited functions."""
    @callLimit(3)
    def f() -> None:
        """Print its own name."""
        print("f()")

    @callLimit(1)
    def g() -> None:
        """Print its own name."""
        print("g()")

    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
