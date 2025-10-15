import math
import math

def NULL_not_found(obj: any) -> int:
    def is_nan(x):
        return x != x 

    dispatch = {
        None: lambda x: print(f"Nothing: {x} {type(x)}"),
        0: lambda x: print(f"Zero: {x} {type(x)}"),
        '': lambda x: print(f"Empty: {x} {type(x)}"),
        False: lambda x: print(f"Fake: {x} {type(x)}")
    }

    if obj in dispatch:
        dispatch[obj](obj)
        return 0
    elif is_nan(obj):
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1

