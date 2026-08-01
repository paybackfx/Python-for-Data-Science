#!/usr/bin/env python3
# =============================================================================
# EXERCISE 03: DATA CLASS
# =============================================================================
# Educational Notes for Beginners:
#
# 1. @dataclass: generates __init__, __repr__ and __eq__ from the annotated
#    attributes. That is why the class below never defines __str__ or
#    __repr__ and still prints as Student(name='Edward', ...).
# 2. field(init=False): removes the attribute from the generated __init__,
#    so passing id="toto" raises a TypeError - exactly the protection the
#    subject asks for on login and id.
# 3. default_factory: a plain default would be evaluated once at class
#    creation and every student would share the same id. A factory is called
#    per instance, so each student gets a fresh random identifier.
# 4. __post_init__: runs right after the generated __init__ and is the only
#    place where a computed field such as the login can be built.
# =============================================================================

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a random 15 character lowercase identifier."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student, with a login and an identifier generated on creation."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Build the login from the first letter of name plus surname."""
        self.login = self.name[0] + self.surname


def main() -> None:
    """Create a student and prove login and id cannot be initialised."""
    student = Student(name="Edward", surname="agle")
    print(student)
    print("---")
    try:
        Student(name="Edward", surname="agle", id="toto")
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
