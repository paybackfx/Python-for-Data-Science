#!/usr/bin/env python3
# =============================================================================
# EXERCISE 06: FILTER THE WORDS LONGER THAN N
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Lambda (lambda word: len(word) > length): an anonymous one-expression
#    function created on the spot and handed to ft_filter as a value. The
#    subject requires at least one lambda in this program.
# 2. List Comprehension: the subject also requires at least one here, so the
#    word list is built with one. Filtering out the empty strings makes it a
#    real transformation, not a decorative copy of split().
# 3. Closure: the lambda reads "length" from the enclosing scope of main()
#    without receiving it as a parameter - it captures the variable.
# 4. Catching Two Failures At Once: a wrong argument count raises
#    AssertionError while a non-numeric N raises ValueError, and the subject
#    asks for the very same message in both cases.
# =============================================================================

import sys

from ft_filter import ft_filter


def main() -> None:
    """Print the words of the first argument longer than the second one."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        words = [word for word in sys.argv[1].split(" ") if word]
        length = int(sys.argv[2])
        print(ft_filter(lambda word: len(word) > length, words))
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
