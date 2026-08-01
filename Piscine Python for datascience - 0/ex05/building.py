#!/usr/bin/env python3
# =============================================================================
# EXERCISE 05: FIRST STANDALONE PROGRAM PYTHON
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Do Not Reinvent The Wheel: str.isupper(), str.islower(), str.isdigit(),
#    str.isspace() and string.punctuation already classify every character, so
#    counting is a one-line sum() over a generator instead of a manual loop.
# 2. sys.stdin.read() vs input(): input() strips the terminating newline while
#    read() keeps every byte until EOF. The subject counts the carriage return
#    as a space, so the raw stream is the only reading that gives 13 characters
#    for "Hello World!" - and read() returns "" on ctrl+D instead of raising.
# 3. Exception Discipline: from this exercise on, the subject invalidates any
#    program that lets an exception escape, so the whole body of main() sits
#    inside a try block that converts failures into the expected message.
# =============================================================================

import string
import sys


def count_chars(text: str) -> None:
    """Print how many characters of each category the text contains."""
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punct = sum(1 for char in text if char in string.punctuation)
    space = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


def main() -> None:
    """Read the text from the arguments or from stdin, then count it."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 2:
            count_chars(sys.argv[1])
        else:
            print("What is the text to count?")
            count_chars(sys.stdin.read())
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
