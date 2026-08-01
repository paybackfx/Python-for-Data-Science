#!/usr/bin/env python3
# =============================================================================
# EXERCISE 03: CALCULATE MY VECTOR
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Operator Overloading (__add__, __mul__, __sub__, __truediv__): defining
#    these methods teaches Python what "+", "*", "-" and "/" mean for your
#    own type, so a calculator object reads like plain arithmetic.
# 2. In-Place Semantics: the subject's expected output shows v3 / 5 working
#    on the result of v3 - 5, so each operation stores the new vector back
#    into the object instead of returning a fresh one.
# 3. Guarding The Only Real Failure: the subject asks for no error handling
#    except division by zero, which is the one operation the language itself
#    cannot define.
# =============================================================================


class calculator:
    """A vector that can be combined with a scalar."""

    def __init__(self, vector: list) -> None:
        """Store the vector this calculator operates on."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add the scalar to every value, then print the new vector."""
        self.vector = [value + object for value in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply every value by the scalar, then print the new vector."""
        self.vector = [value * object for value in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract the scalar from every value, then print the vector."""
        self.vector = [value - object for value in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide every value by the scalar, then print the new vector."""
        if object == 0:
            print("Error: division by zero is not allowed")
            return
        self.vector = [value / object for value in self.vector]
        print(self.vector)


def main() -> None:
    """Demonstrate the four scalar operations and the zero division."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print("---")
    v4 = calculator([10.0, 15.0, 20.0])
    v4 / 0


if __name__ == "__main__":
    main()
