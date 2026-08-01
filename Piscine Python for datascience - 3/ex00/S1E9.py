#!/usr/bin/env python3
# =============================================================================
# EXERCISE 00: GOT S1E9
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Abstract Base Class (ABC): a class that declares what its children must
#    provide but refuses to be instantiated itself. Character models what
#    every character has in common without ever existing on its own.
# 2. @abstractmethod: marking __init__ abstract is what makes
#    Character("hodor") raise a TypeError, while still letting the method
#    carry the shared implementation that children reach through super().
# 3. super(): calls the next class in the resolution order rather than a
#    hard-coded parent, which is what keeps multiple inheritance working
#    later on in this module.
# =============================================================================

from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract blueprint shared by every character of the show."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a character with a first name and a health state."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Turn the health state of the character from alive to dead."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Stark with a first name and a health state."""
        super().__init__(first_name, is_alive)


def main() -> None:
    """Demonstrate a Stark dying and the abstract class refusing to exist."""
    ned = Stark("Ned")
    print(ned.__dict__)
    print(ned.is_alive)
    ned.die()
    print(ned.is_alive)
    print("---")
    lyanna = Stark("Lyanna", False)
    print(lyanna.__dict__)
    print("---")
    try:
        Character("hodor")
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
