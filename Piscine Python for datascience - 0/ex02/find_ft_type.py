# =============================================================================
# EXERCISE 02: FIRST FUNCTION PYTHON
# =============================================================================
# Educational Notes for Beginners:
#
# 1. No Shebang, No Main Block: the subject states that running this file alone
#    must print nothing. It is an import-only library consumed by tester.py,
#    not a standalone program, so it defines a function and stops there.
# 2. type(object) vs isinstance(): type() returns the exact class and is used
#    here as a dictionary key, while isinstance() also accepts subclasses,
#    which is what we want when catching every flavour of string.
# 3. Dispatch Table (type_names): mapping the four container classes to their
#    display label replaces a chain of if/elif and keeps the lookup O(1).
# =============================================================================


def all_thing_is_obj(object: any) -> int:
    """Print the type of the given object and always return 42."""
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }
    label = type_names.get(type(object))
    if label is not None:
        print(f"{label} : {type(object)}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
