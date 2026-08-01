#!/usr/bin/env python3
# =============================================================================
# EXERCISE 04: CALCULATE MY DOT PRODUCT
# =============================================================================
# Educational Notes for Beginners:
#
# 1. @staticmethod: the decorator the subject hints at. It groups a function
#    under the class namespace without needing an instance, which is what
#    lets the tester write calculator.dotproduct(a, b) directly.
# 2. zip(V1, V2): walks two sequences in lockstep and yields pairs, so the
#    three operations are one expression each instead of an index loop.
# 3. Dot Product: the sum of the pairwise products. It measures how much two
#    vectors point in the same direction and is the single most used
#    operation in machine learning.
# =============================================================================


class calculator:
    """Vector to vector operations, usable without any instance."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of the two vectors."""
        print(f"Dot product is: {sum(a * b for a, b in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element wise sum of the two vectors."""
        print(f"Add Vector is : {[float(a + b) for a, b in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element wise difference of the two vectors."""
        print(f"Sous Vector is: {[float(a - b) for a, b in zip(V1, V2)]}")


def main() -> None:
    """Demonstrate the three vector to vector operations."""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
