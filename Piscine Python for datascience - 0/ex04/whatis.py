#!/usr/bin/env python3
# =============================================================================
# EXERCISE 04: THE EVEN AND THE ODD
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Command Line Arguments (sys.argv): a list of strings where index 0 is the
#    script name itself, so a program called with one argument sees a list of
#    length 2. That is why the guards below compare against 1 and 2.
# 2. Guard Clauses: checking the invalid cases first and leaving the function
#    early keeps the happy path unindented and easy to read.
# 3. int() Raises, It Does Not Return None: converting "Hi!" raises a
#    ValueError, so the conversion is wrapped in a try block instead of being
#    tested beforehand - asking forgiveness is more Pythonic than asking
#    permission.
# =============================================================================

import sys


def main() -> None:
    """Print whether the single command line argument is even or odd."""
    try:
        if len(sys.argv) == 1:
            return
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
