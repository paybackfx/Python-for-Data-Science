#!/usr/bin/env python3
# =============================================================================
# EXERCISE 02: NOW IT'S WEIRD!
# =============================================================================
# Educational Notes for Beginners:
#
# 1. The Diamond Problem: King inherits from Baratheon and Lannister, which
#    both inherit from Character. Since Python 2.3 the C3 linearization gives
#    one deterministic order - King, Baratheon, Lannister, Character - so
#    Character is initialised exactly once and Baratheon wins the traits.
# 2. Properties Are Data Descriptors: a class-level property takes precedence
#    over the instance dictionary, so "self.eyes = value" inside the setter
#    would call the setter again forever. The value is therefore stored
#    directly in self.__dict__, which also keeps __dict__ printing normally.
# 3. Accessors As Gatekeepers: get_eyes / set_eyes route every read and write
#    through the class, which is where validation would live in real code.
# =============================================================================

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the false king, born of two families at once."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize the king through the whole inheritance chain."""
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        """Return the eyes color of the king."""
        return self.__dict__["eyes"]

    def set_eyes(self, value: str) -> None:
        """Set the eyes color of the king."""
        self.__dict__["eyes"] = value

    def get_hairs(self) -> str:
        """Return the hairs color of the king."""
        return self.__dict__["hairs"]

    def set_hairs(self, value: str) -> None:
        """Set the hairs color of the king."""
        self.__dict__["hairs"] = value

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)


def main() -> None:
    """Demonstrate the diamond inheritance and the two properties."""
    joffrey = King("Joffrey")
    print(joffrey.__dict__)
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)
    print("---")
    print(f"MRO: {[cls.__name__ for cls in King.__mro__]}")


if __name__ == "__main__":
    main()
