# =============================================================================
# EXERCISE 03: NULL NOT FOUND
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Identity vs Equality (is vs ==): "is" compares memory addresses while "=="
#    compares values. None and False are unique singletons, so they must be
#    detected with "is" - using "==" would also catch 0, which is a different
#    kind of emptiness and needs its own message.
# 2. NaN Is Not Equal To Itself (object != object): the IEEE-754 standard says
#    every comparison involving NaN is false, including NaN == NaN. That makes
#    this odd-looking test the cleanest way to spot a NaN without any import.
# 3. Order Matters: False is checked before 0 because False == 0 is true in
#    Python, so the reverse order would label False as a "Zero".
# =============================================================================


def NULL_not_found(object: any) -> int:
    """Print which flavour of "Null" was received, 0 on success 1 on error."""
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        print(f"Cheese: {object} {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == "":
        print(f"Empty: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
