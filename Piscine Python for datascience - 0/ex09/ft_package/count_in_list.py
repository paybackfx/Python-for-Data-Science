# =============================================================================
# EXERCISE 09: MY FIRST PACKAGE CREATION
# =============================================================================
# Educational Notes for Beginners:
#
# 1. A Package Is A Directory: any folder holding an __init__.py is importable
#    as a package, and every module inside it becomes a submodule.
# 2. Do Not Reinvent The Wheel (list.count): the standard library already
#    counts occurrences in a single C-level pass, so the function is a thin,
#    documented wrapper rather than a hand-written loop.
# 3. Generic Type Hints (list[str], str, int): they document the contract of a
#    published package, which is the first thing a consumer reads.
# =============================================================================


def count_in_list(lst: list[str], target: str) -> int:
    """Return how many times target appears in lst."""
    return lst.count(target)
