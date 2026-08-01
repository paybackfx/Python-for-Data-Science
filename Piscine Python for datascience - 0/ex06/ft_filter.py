# =============================================================================
# EXERCISE 06: RECODE THE FILTER BUILT-IN
# =============================================================================
# Educational Notes for Beginners:
#
# 1. List Comprehension ([item for item in iterable if ...]): the subject
#    explicitly requires this form. It builds the result list in one pass, so
#    no accumulator variable and no append() call are needed.
# 2. Callables Are Values: function is an ordinary parameter holding another
#    function, which is what lets the caller inject a lambda at the call site.
# 3. Faithful To The Original: the built-in filter treats a None function as a
#    plain truthiness test, so the same special case is handled here first -
#    otherwise ft_filter(None, ...) would crash on a NoneType call.
#
# NOTE: the docstring below is reproduced character for character from
#    print(filter.__doc__) on CPython 3.10, the version the subject mandates.
#    CPython 3.12 and later dropped the leading signature line, so the two
#    strings only compare equal on 3.10/3.11. The continuation lines are
#    deliberately flush left: indenting them would push the third line past
#    the 79 column limit and change the text the evaluator compares.
# =============================================================================


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
