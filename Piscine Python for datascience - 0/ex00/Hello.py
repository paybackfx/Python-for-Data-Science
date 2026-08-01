#!/usr/bin/env python3
# =============================================================================
# EXERCISE 00: FIRST PYTHON SCRIPT
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Mutable Containers (list, set, dict): these three can be modified in
#    place. A list element is replaced through its index, a set value is
#    swapped with remove()/add(), a dict value is reassigned through its key.
# 2. Immutable Container (tuple): a tuple can never be modified in place. The
#    only way to "change" it is to rebind the name to a brand new tuple, which
#    is why the line below rebuilds both elements at once.
# 3. Sets Are Unordered: a set stores values by hash, not by position, so the
#    order Python prints them in is not guaranteed to match the source order.
# =============================================================================

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
ft_list[1] = "World!"
ft_tuple = ("Hello", "Morocco!")
ft_set.remove("tutu!")
ft_set.add("Benguerir!")
ft_dict["Hello"] = "1337Benguerir!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
