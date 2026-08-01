#!/usr/bin/env python3
# =============================================================================
# EXERCISE 01: GOT S1E7
# =============================================================================
# Educational Notes for Beginners:
#
# 1. __str__ vs __repr__: __str__ is what print() shows a human, __repr__ is
#    what the interpreter shows a developer. Returning a string from both is
#    what turns "<S1E7.Baratheon object at 0x...>" into readable output.
# 2. Bound Methods Reveal __repr__: printing Robert.__str__ without calling
#    it displays "<bound method ... of {repr(instance)}>", which is why the
#    subject's expected output shows the Vector line inside that wrapper.
# 3. @classmethod: receives the class itself as cls instead of an instance,
#    so it can act as an alternative constructor and build objects in a chain
#    without the caller ever writing Lannister(...) directly.
# =============================================================================

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Baratheon with the family physical traits."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Return the family traits of the character as a string."""
        return (f"Vector: ('{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """Return the same readable string as __str__."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Lannister with the family physical traits."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Return the family traits of the character as a string."""
        return (f"Vector: ('{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """Return the same readable string as __str__."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> "Lannister":
        """Build a Lannister without instantiating the class directly."""
        return cls(first_name, is_alive)


def main() -> None:
    """Demonstrate both families and the alternative constructor."""
    robert = Baratheon("Robert")
    print(robert.__dict__)
    print(robert)
    robert.die()
    print(robert.is_alive)
    print("---")
    cersei = Lannister("Cersei")
    print(cersei.__dict__)
    print(cersei)
    print("---")
    jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {jaine.first_name, type(jaine).__name__}, "
          f"Alive : {jaine.is_alive}")


if __name__ == "__main__":
    main()
