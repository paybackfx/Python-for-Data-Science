#!/usr/bin/env python3
# =============================================================================
# EXERCISE 07: DICTIONARIES SOS
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Dictionary As A Lookup Table (NESTED_MORSE): a dict gives O(1) access by
#    key, so translating a character is a single lookup instead of a scan. It
#    is an uppercase module constant, not a mutable global state.
# 2. Membership Testing (char in NESTED_MORSE): on a dict this tests the keys,
#    which validates the input and drives the translation with the same table.
# 3. Separation Of Concerns: encode_morse() knows only about Morse code while
#    main() knows only about the command line, so each function has one reason
#    to change and can be tested on its own.
# =============================================================================

import sys

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def encode_morse(text: str) -> str:
    """Return the Morse translation of an alphanumeric uppercase string."""
    if not all(char in NESTED_MORSE for char in text):
        raise AssertionError("the arguments are bad")
    return " ".join(NESTED_MORSE[char] for char in text)


def main() -> None:
    """Encode the single command line argument into Morse code."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        print(encode_morse(sys.argv[1].upper()))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
