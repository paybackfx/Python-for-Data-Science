# =============================================================================
# EXERCISE 09: PACKAGE ENTRY POINT
# =============================================================================
# Educational Notes for Beginners:
#
# 1. __init__.py Is The Public Face: re-exporting count_in_list here is what
#    makes "from ft_package import count_in_list" work, instead of forcing the
#    caller to write "from ft_package.count_in_list import count_in_list".
# 2. Relative Import (from .count_in_list): the leading dot means "the module
#    next to me inside this package", so the import never collides with a
#    same-named module installed elsewhere.
# 3. __all__: declares the official public API of the package and is the list
#    used by "from ft_package import *".
# =============================================================================

from .count_in_list import count_in_list

__all__ = ["count_in_list"]
